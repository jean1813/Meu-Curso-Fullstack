// 1 -  DESTRUTURANDO E ATRBUINDO EM VARIAVEIS
const pessoa = ["Gabriel", 24, "desenvolvedor"]
const [nome,idade,profissao] = pessoa 
console.log(nome)
// Retorno: "Gabriel"


// 2 -  ENCONTRAR UM OBJETO ESPECIFICO DENTRO DE UM ARRAY
const usuarios = [
    {id: 1, nome: "joaozinho"},
    {id: 2, nome: "maria"},
    {id: 3, nome: "pedro"},
];
const usuario = usuarios.find((usuario) => usuario.nome === "pedro");
console.log(nome)
// Retorno: {id: 3, nome: "pedro"}


// 3 -  PERCORRER TODAS AS CHAVES E VALORES DENTRO DE UM OBJETO

const objeto = { um: 1, dois: 2, tres: 3};
Object.keys(objeto).forEach((key, value) => {
    // seu codigo aqui
    console.log(key, value);
})


// 4 - FILTRAR UM ARRAY BASEADO EM UMA CONDIÇÃO
const listaArquivos = [
    "files/dir1/file",
    "files/dir1/file2",
    "files/dir2/file",
    "files/dir2/file2",
];
const filtro = listaArquivos.filter(
    (arquivo) =>arquivo.includes("dir2"));
console.log(filtro)
//Returno: [ "files/dir2/file", "files/dir2/files2"]


// 5 - ATRIBUIÇÃO DE CHAVES A UM OBJETO COM O MESMO NOME
const ntn = "joaquina";
const forca = 12;
const ocupacao = "estudante";
// ao invés de:
const usuario1 = {ntn: ntn, forca: forca, ocupacao: ocupacao};

// faça
const usuario2 = {ntn, forca, ocupacao};
console.log(usuario2);
// { nome"joaquina", forca: 12, ocupacao: ocupacao }


