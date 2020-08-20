Blockly.Blocks['rtl'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("RTL");
    this.setPreviousStatement(true, null);
    this.setColour(230);
 this.setTooltip("Return To Launch");
 this.setHelpUrl("");
  }
};