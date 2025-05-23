import numpy as np
import operator
from xml.dom.minidom import parse
from fontTools.ttLib import TTFont


def get_offset_font(filename):
    data = parse(filename)
    collection = data.documentElement
    labels = collection.getElementsByTagName("TTGlyph")
    data_list = []
    max_len = 0
    for label in labels:
        contour = label.getElementsByTagName("contour")
        offset = [[label.getAttribute("name"),
                   label.getAttribute("yMax"),
                   label.getAttribute("yMin"),
                   label.getAttribute("xMax"),
                   label.getAttribute("xMin")]]
        for item in contour:
            pt = item.getElementsByTagName("pt")
            for xy in pt:
                if xy.hasAttribute("y"):
                    offset.append(int(xy.getAttribute("y")))
                if xy.hasAttribute("x"):
                    offset.append(int(xy.getAttribute("x")))
        else:
            data_list.append(offset)
            max_len = max_len if max_len > len(offset) else len(offset)
    for i in range(len(data_list)):
        data_list[i] = data_list[i] + [0]*(max_len-len(data_list[i]))
    return data_list


def get_label_font(labels_np: list or np.ndarray):
    label_list = []
    for item in labels_np:
        label_list.append(item[0][0])
    return label_list


def classify_knn(input_x: np.ndarray or list, dataSet: np.ndarray or list, labels: np.ndarray or list, k:int)->list:
    '''
    :param input_x:     data for predicting
    :param dataSet:     dataset for training
    :param labels:   The labels of dataset
    :param k:   The range of a point of input_x
    :return list:  A list of probability which have minimum distance

    Either input_x or dataSet, they're should to normalize at first
    '''
    dataSet = np.array(dataSet,dtype=object)
    labels = np.array(labels,dtype=object).flatten()  # flattening
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(input_x, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)  # Turning the sum of every rows to 1*dataSetSize matrix
    distances = sqDistances**0.5
    # Return a sorted(fr min to huge) index list of the value of 1*dataSetSize matrix
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):  # Place k numbers of labels/type to classCount keys, and add the values of classCount[label[k]]
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) # sorted by values(the labels times)
    return sortedClassCount[0][0]


def normalize_dataset_01(dataset: list or np.ndarray, mindata: list or np.ndarray=[], maxdata: list or np.ndarray=[]):
    '''
    :param dataset: dataset for normalizing
    :param mindata: The matrix of minimum values
    :param maxdata: The matrix of maximum values
    :return:
    '''
    dataset = np.array(dataset)
    # When sample unstable probably, means that sample over max or less than minimum, U need to set values by yourself
    if not (mindata and maxdata):
        mindata = dataset.min(0)    # 0 for figuring the minimum of every columns (the same as max)
        maxdata = dataset.max(0)    # 1 for figuring the minimum of every rows (the same as max)
    else:
        maxdata = np.array(maxdata)
        mindata = np.array(mindata)
    rangedata = maxdata - mindata
    # the same as ↓↓↓(dataset - mindata) / np.tile(rangedata, (dataset.shape[0], 1)↓↓↓
    # due to python auto turn X1 = 1*n matrix to n*n matrix when X1 divide by X2(n*n)
    dataset = (dataset - mindata) / rangedata  # )
    return dataset, mindata, rangedata


def normalize_data_01(data: list or np.ndarray, mindata: list or np.ndarray, rangedata: list or np.ndarray):
    '''
    :param data: dataset for normalizing
    :param mindata: The matrix of minimum values
    :param rangedata: The matrix of max subtraction min of every columns
    :return:
    '''
    data = np.array(data)
    return (data - mindata)/rangedata


def normalize_dataset_z_score(dataset: list or np.ndarray):
    '''
    :param dataset: dataset for normalizing
    :return:
    '''
    dataset = np.array(dataset)
    meansMat = dataset.sum(axis=0)/dataset.shape[0] # get means
    diffMat = dataset - meansMat
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=0)/dataset.shape[0]
    standardDeviation = sqDistances ** 0.5  # get standard deviation
    dataset = (dataset - meansMat) / standardDeviation
    return meansMat, standardDeviation, dataset


def normalize_data_z_score(dataset: list or np.ndarray, meansMat: list or np.ndarray, standardDeviation: list or np.ndarray):
    '''
    :param dataset: dataset for normalizing
    :param meansMat: meansMat of training dataset
    :param standardDeviation: standardDeviation of training dataset
    :return:
    '''
    dataset = np.array(dataset)
    return (dataset - meansMat) / standardDeviation


def normalize_data_z_score_arctan(dataset: list or np.ndarray):
    '''
    :param dataset: dataset for normalizing
    :return:
    '''
    dataset = np.array(dataset)
    dataSet = np.arctan(dataset)*(2/np.pi)
    return dataSet


def knn(train_font, data_annotations, distinguish_font):
    """
    :param train_font:          训练字体相对路径
    :param data_annotations:    标注的数据【字典类型】
    :param distinguish_font:    识别字体的相对路径
    :return:                    返回传入的字体的映射表
    """
    try:
        font_message = TTFont(train_font)
        font_message.saveXML('font_train.xml')
    except FileNotFoundError:
        raise FileNotFoundError('训练字体文件未发现，请检查路径')

    # 训练，处理基准值
    data_train = get_offset_font('font_train.xml')
    group = np.array(data_train,dtype=object)[:, 1:].tolist()
    labels = get_label_font(np.array(data_train,dtype=object)[:, :1])
    normalize_group = normalize_data_z_score_arctan(group)

    # 真实的字体数据
    font_message = TTFont(distinguish_font)
    font_message.saveXML('distinguish_font.xml')
    data_list = get_offset_font('distinguish_font.xml')
    group = np.array(data_list,dtype=object)[:, 1:].tolist()
    data_labels = get_label_font(np.array(data_list,dtype=object)[:, :1])
    index = 0
    really_table = {}

    try:
        for item in np.array(group,dtype=object).tolist():
            # 通过相似度算法，获取到最接近的，并吐出结果
            result = classify_knn(item, dataSet=normalize_group, labels=labels, k=3)
            really_table[data_labels[index]] = data_annotations[result]
            index += 1
        return really_table
    except KeyError:
        raise KeyError('数据标注异常，请检查数据是否标注完整 / 训练文件是否与标注数据匹配')
