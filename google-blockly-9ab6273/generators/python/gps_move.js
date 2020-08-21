Blockly.Python['gps_move'] = function(block) {
  var number_lat = block.getFieldValue('lat');
  var number_lng = block.getFieldValue('lng');
  var number_alt = block.getFieldValue('alt');
  // TODO: Assemble Python into code variable.
  var code = '\n' + 'drone.cmd_move_to_gps('+ number_lat + ',' + number_lng + ',' + number_alt + ')';
  return code;
};