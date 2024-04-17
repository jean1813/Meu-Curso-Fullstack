document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    if (username === 'admin' && password === 'password') {
        // Simulando um login bem-sucedido redirecionando para uma página de boas-vindas
        window.location.href = 'detalhestst2.html';
    } else {
        document.getElementById('error-message').textContent = 'Usuário ou senha incorretos!';
    }
});