
async function fetchDashboardData () {
    const url = 'assets/data/dashboard.json';
    const fetching = await fetch(url)
    return await fetching.json()
}


function updateDashboardData(dashboardData) {
    
    const parque = document.getElementById('atracao.bondinhos')
    parque.innerText = dashboardData[0].name

    const eagle_tirolesa = document.getElementById('atracao.eagle_tirolesa')
    eagle_tirolesa.innerText = dashboardData[1].name

    // const atracao_nova = document.getElementById('atracao.nova')
    // atracao_nova.innerText = dashboardData[2].name

   const pagantes = document.getElementById('atracao.pagantes')
   pagantes.innerText = dashboardData[3].name

    const clientesBondinhos = document.getElementById('quantidade.bondinhos')
    clientesBondinhos.innerText = dashboardData[0].number

    const clienteseagle_tirolesa = document.getElementById('quantidade.eagle_tirolesa')
    clienteseagle_tirolesa.innerText = dashboardData[1].number

    const clientesPagantes = document.getElementById('quantidade.pagantes')
    clientesPagantes.innerText = dashboardData[3].number

    const fating = document.getElementById('fating')
    fating.innerHTML = `<p>R$ ${dashboardData[4].number}`

    // const fatloj = document.getElementById('fatloj')
    // fatloj.innerHTML = `<p>R$ ${dashboardData[5].quantidade}`

    const previs0 = document.getElementById('previs0')
    previs0.innerText = dashboardData[6].number

    const previs1 = document.getElementById('previs1')
    previs1.innerText = dashboardData[7].number

    const previs2 = document.getElementById('previs2')
    previs2.innerText = dashboardData[8].number

    const previs3 = document.getElementById('previs3')
    previs3.innerText = dashboardData[9].number

    const previs4 = document.getElementById('previs4')
    previs4.innerText = dashboardData[10].number

    const previs5 = document.getElementById('previs5')
    previs5.innerText = dashboardData[11].number

}

(async () => {
    const dashboardData = await fetchDashboardData ()
    updateDashboardData(dashboardData)
})()