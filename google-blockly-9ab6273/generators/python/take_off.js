Blockly.Python['takeoff'] = function(block) {
  var number_altitude = block.getFieldValue('altitude');
  // TODO: Assemble Python into code variable.
  var code = '\n' + 'drone.cmd_takeoff(' + number_altitude + ')';
  return code;
};