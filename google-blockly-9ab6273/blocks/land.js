Blockly.Blocks['land'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("LAND");
    this.setPreviousStatement(true, null);
    this.setColour(230);
 this.setTooltip("land the drone in the current position");
 this.setHelpUrl("");
  }
};
