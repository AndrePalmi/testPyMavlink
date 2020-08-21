Blockly.Blocks['arm_motors'] = {
  init: function() {
    this.appendDummyInput().appendField('ARM MOTORS');
    this.setPreviousStatement(true, 'ARM MOTORS');
    this.setNextStatement(true,  ['TAKEOFF', 'DISARM MOTORS']);
    this.setColour(315);
    this.setTooltip("Arm the motors, ready to take off");
    this.setHelpUrl("");
  }
};