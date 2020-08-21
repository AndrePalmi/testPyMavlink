Blockly.Python['connect'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = 'import time' + '\n' + 'from pymavlink import mavutil' + '\n' + 'from prova import Copter' + '\n' + 'drone = Copter()'+ '\n' + 'drone.connect()';
  alert(code)
  return code;
};