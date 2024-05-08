
let dataAtual = new Date();

let amanha = new Date(dataAtual);
amanha.setDate(dataAtual.getDate() + 1);

let emDoisDias = new Date(dataAtual);
emDoisDias.setDate(dataAtual.getDate() + 2);

let emTresDias = new Date(dataAtual);
emTresDias.setDate(dataAtual.getDate() + 3);

let emQuatroDias = new Date(dataAtual);
emQuatroDias.setDate(dataAtual.getDate() + 4);

let emCincoDias = new Date(dataAtual);
emCincoDias.setDate(dataAtual.getDate() + 5);

const hoje = document.getElementById('hoje')
hoje.innerText = dataAtual.toLocaleDateString().slice(0, 10)

const data1 = document.getElementById('data1')
data1.innerText = amanha.toLocaleDateString().slice(0, 10)

const data2 = document.getElementById('data2')
data2.innerText = emDoisDias.toLocaleDateString().slice(0, 10)

const data3 = document.getElementById('data3')
data3.innerText = emTresDias.toLocaleDateString().slice(0, 10)

const data4 = document.getElementById('data4')
data4.innerText = emQuatroDias.toLocaleDateString().slice(0, 10)

const data5 = document.getElementById('data5')
data5.innerText = emCincoDias.toLocaleDateString().slice(0, 10)

