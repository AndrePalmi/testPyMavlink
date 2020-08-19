Blockly.Blocks['stampa_numero'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("Number")
        .appendField("inserisci numero:");
    this.setOutput(true, "Number");
    this.setColour(270);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};