Blockly.Blocks['takeoff'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("TAKEOFF, reach altitude of")
        .appendField(new Blockly.FieldNumber(0, 0), "altitude")
        .appendField("meters");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(270);
 this.setTooltip("Reach the choosen altitude in meters");
 this.setHelpUrl("");
  }
};