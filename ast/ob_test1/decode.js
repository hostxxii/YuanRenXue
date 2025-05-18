const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default; // 注意 .default
const generator = require("@babel/generator").default; // 注意 .default
const t = require("@babel/types"); // Babel 类型，用来创建新的 AST 节点
const fs = require("fs");
const path = require("path");

// 读取 demo.js 文件内容
const demoCode = fs.readFileSync(path.resolve(__dirname, "demo.js"), "utf-8");

// 假设 demoCode 是你 demo.js 文件的内容字符串
// const demoCode = `var hexString = '\x48\x65\x6c\x6c\x6f'; var obj = {}; obj['val' + 'ue'] = 1; obj['another'] = 2;`;

// 1. 解析
const ast = parser.parse(demoCode);

// 2. 遍历和转换
traverse(ast, {
  // 访问者对象
  StringLiteral(path) {
    const node = path.node;
    // 检查是否存在 extra.raw 并且它与 value 的直接表示不同
    // (更精确的检查是看 extra.raw 是否包含 \x 等编码)
    if (
      node.extra &&
      node.extra.raw &&
      node.extra.raw !== `"${node.value}"` &&
      node.extra.raw !== `'${node.value}'`
    ) {
      // 如果 value 本身已经是解码后的正确字符串
      // 用一个新的 StringLiteral 节点替换，这个新节点不会有之前的 extra.raw
      path.replaceWith(t.stringLiteral(node.value));
    }
  },
  MemberExpression(path) {
    const node = path.node;

    // 步骤 2: Date['\\x70\\x61\\x72'+'\\x73\\x65'] -> Date['parse']
    if (
      node.computed &&
      t.isBinaryExpression(node.property) &&
      node.property.operator === "+"
    ) {
      const left = node.property.left;
      const right = node.property.right;
      if (t.isStringLiteral(left) && t.isStringLiteral(right)) {
        const combinedString = left.value + right.value;
        path.get("property").replaceWith(t.stringLiteral(combinedString));
      }
    }

    // 步骤 3: Date['parse'] -> Date.parse
    // 需要在步骤 2 之后执行，或者在一个新的遍历中执行，以确保属性已经是单个字符串
    if (node.computed && t.isStringLiteral(node.property)) {
      const propName = node.property.value;
      // 检查是否是合法的标识符名称
      if (/^[a-zA-Z$_][a-zA-Z0-9$_]*$/.test(propName)) {
        path.node.computed = false;
        path.get("property").replaceWith(t.identifier(propName));
      }
    }
  },
});

// 3. 生成
const output = generator(ast, {}, demoCode);
console.log(output.code);

// 写入解码后的代码到新文件
fs.writeFileSync(
  path.resolve(__dirname, "decoded_output.js"),
  output.code,
  "utf-8"
);
