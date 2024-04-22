// index5.js

// Função para buscar a previsão do tempo com base na cidade
function buscarPrevisaoTempo(cidade) {
  // Aqui você pode usar APIs de previsão do tempo, como OpenWeatherMap, Weatherstack, etc.
  // Por exemplo:
  // const apiKey = 'sua-chave-de-api';
  // const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${cidade}&appid=${apiKey}`;

  // Simulando uma resposta de API para fins de exemplo
  const previsaoTempo = {
      temperatura: '21°C',
      icone: 'https://www.svgrepo.com/show/106705/clouds.svg',
      umidade: 'Umidade: 70%'
  };

  // Exibir a previsão do tempo na página HTML
  document.querySelector('.cidade').textContent = `Tempo em ${cidade}`;
  document.querySelector('.temp').textContent = previsaoTempo.temperatura;
  document.querySelector('.icone').src = previsaoTempo.icone;
  document.querySelector('.umidade').textContent = previsaoTempo.umidade;
}

// Evento de clique no botão de busca
document.querySelector('button').addEventListener('click', function() {
  const cidade = document.querySelector('input').value;
  buscarPrevisaoTempo(cidade);
});

/*
Clica no BOTÃO 
  -> CHAMA A FUNÇÃO cliqueiNoBotao()
  -> Vai no INPUT e pega o que está lá dentro

  -> PASSAR a cidade para o servidor
  Math.floor -> Ferramenta do JavaScript para Arredondar valores
*/
