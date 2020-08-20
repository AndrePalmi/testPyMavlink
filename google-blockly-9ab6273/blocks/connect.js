Blockly.Blocks['connect'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("CONNECT");
    this.setNextStatement(true, null);
    this.setColour(20);
 this.setTooltip("Connect ");
 this.setHelpUrl("");
  }
};