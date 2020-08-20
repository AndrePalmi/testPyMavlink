Blockly.Blocks['rtl'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("RTL");
    this.setPreviousStatement(true, null);
    this.setColour(195);
 this.setTooltip("Return To Launch");
 this.setHelpUrl("");
  }
};