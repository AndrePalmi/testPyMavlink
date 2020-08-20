Blockly.Python['stampa_numero'] = function(block) {
  var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
  var code = 'print("hello world")';
  return code
};
