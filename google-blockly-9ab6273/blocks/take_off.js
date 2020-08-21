Blockly.Blocks['takeoff'] = {
  init: function() {
    this.appendDummyInput()
        .appendField('TAKEOFF')
        .appendField("reach altitude of: ")
        .appendField(new Blockly.FieldNumber(0, 0), "altitude")
        .appendField("meters");
    this.setPreviousStatement(true, 'TAKEOFF');
    this.setNextStatement(true, ['GPS MOVE', 'LAND', 'RTL']);
    this.setColour(270);
    this.setTooltip("Reach the choosen altitude in meters");
    this.setHelpUrl("");
  }
};