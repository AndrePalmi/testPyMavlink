Blockly.Blocks['inserisci_numero'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("Number")
        .appendField("ins numero:");
    this.setColour(300);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};
