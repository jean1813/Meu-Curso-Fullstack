// MANIPULAR DATAS
// DICAS QUE VOCÊ PRECISA CONHECER

// 1 - VERIFIQUE SE HOJE É UM FIM DE SEMANA

const isweekend = (date = new Date()) = date .getDay() % 6 === 0;

// 2 - VERIFIQUE SE A DATA É HOJE
const isToday = (date) => date.toISOString().slice(0, 10) ===
new Date().toISOString().slice(0, 10);

isToday (new Date(2024, 2, 4))
// SE A DATA FORNECIDA DENTRO DO isToday for igual ao dia de hoje retornara true se não false.


// 3 - VERIFIQUE SE UMA DATA ESTA ENTRE DUAS DATAS

const isBetween = (date, min, max) => max.getTime() >=
min.getTime() && date.getTime() <= max.getTime()

isBetween (
    new Date(), // Data que desejar passar
    new Date(2024, 1, 4), // Data minima
    new Date(2024, 2, 6), // Data minima
)
// VAI VERIFICAR SE A DATA PASSADA ESTA ENTRE DUAS DATAS (MIN E MAX) SE ESTIVER RETORNARA TRUE SE NÃO FALSE




