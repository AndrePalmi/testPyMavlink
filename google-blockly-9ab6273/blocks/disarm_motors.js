Blockly.Blocks['disarm_motors'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("DISARM MOTORS");
    this.setPreviousStatement(true, 'DISARM MOTORS');
    this.setColour(315);
    this.setTooltip("Disarm the motors of the drone");
    this.setHelpUrl("");
  }
};