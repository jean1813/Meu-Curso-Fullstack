function mostrarTabuada() {
    // Limpa a div onde a tabuada será exibida
    document.getElementById('tabuada').innerHTML = '';
  
    // Obtém os valores dos números
    var n1 = parseInt(document.getElementById('n1').value);
    var n2 = parseInt(document.getElementById('n2').value);
  
    // Cria uma tabela para exibir a tabuada
    var table = document.createElement('table');
  
    // Loop para gerar as linhas da tabela (tabuada)
    for (var i = 1; i <= n2; i++) {
      var row = table.insertRow();
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      cell1.textContent = n1 + ' x ' + i;
      cell2.textContent = n1 * i;
    }
  
    // Adiciona a tabela à div
    document.getElementById('tabuada').appendChild(table);
  }
  