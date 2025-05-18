const {parse} = require('@babel/parser');
const generator = require('@babel/generator').default;
const traverse = require('@babel/traverse').default;  
// js代码转ast
const js_code=`function hi(){console['\x6c\x6f\x67']('\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21');}hi();`
const ast_code=parse(js_code);
console.log(ast_code);
console.log("**********************");

// 遍历标签
const visitor = {
  StringLiteral(path) {
    console.log(path.node.value);
  },
};

traverse(ast_code,visitor);
console.log("**********************");


// ast转js代码
const js_code_out=generator(ast_code)
console.log(js_code_out.code)
