Blockly.Blocks['rtl'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("RTL")
        .appendField("Return to launch");
    this.setPreviousStatement(true, 'RTL');
    this.setColour(195);
    this.setTooltip("Return To Launch");
    this.setHelpUrl("");
  }
};