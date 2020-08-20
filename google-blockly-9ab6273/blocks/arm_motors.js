Blockly.Blocks['arm_motors'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("ARM MOTORS");
    this.setPreviousStatement(true, "takeoff");
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("Arm the motors, ready to take off");
 this.setHelpUrl("");
  }
};