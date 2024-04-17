document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Obter os valores do nome de usuário e senha
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Fazer uma requisição AJAX para carregar os dados do arquivo JSON
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'credenciais.json', true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);
            var users = data.users;

            // Verificar as credenciais
            var isValidUser = users.some(function(user) {
                return user.username === username && user.password === password;
            });

            // Redirecionar para a página de boas-vindas ou exibir mensagem de erro
            if (isValidUser) {
                window.location.href = 'welcome.html';
            } else {
                document.getElementById('error-message').textContent = 'Usuário ou senha incorretos!';
            }
        } else {
            console.error('Erro ao carregar o arquivo JSON');
        }
    };
    xhr.send();
});
