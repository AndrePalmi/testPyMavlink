Blockly.Blocks['gps_move'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("GPS MOVE");
    this.appendDummyInput()
        .appendField("LATITUDE")
        .appendField(new Blockly.FieldNumber(0, -90, 90), "lat");
    this.appendDummyInput()
        .appendField("LONGITUDE")
        .appendField(new Blockly.FieldNumber(0, -180, 180), "lng");
    this.appendDummyInput()
        .appendField("ALTITUDE")
        .appendField(new Blockly.FieldNumber(0, 0), "alt");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("Move following GPS coordinates");
 this.setHelpUrl("");
  }
};