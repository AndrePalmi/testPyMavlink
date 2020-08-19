Blockly.Python['inserisci_numero'] = function(block) {
  var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
  var code = 'print(' + value_name + ')';
  return code;
};
