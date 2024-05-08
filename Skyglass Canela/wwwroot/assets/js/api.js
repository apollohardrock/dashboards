
async function fetchDashboardData () {
    const url = 'assets/data/dashboard.json';
    const fetching = await fetch(url)
    return await fetching.json()
}


function updateDashboardData(dashboardData) {
    
    const parque = document.getElementById('atracao.parque')
    parque.innerText = dashboardData[0].atracao

    const plataforma = document.getElementById('atracao.plataforma')
    plataforma.innerText = dashboardData[1].atracao

    const abusado = document.getElementById('atracao.abusado')
    abusado.innerText = dashboardData[2].atracao

    const pagantes = document.getElementById('atracao.pagantes')
    pagantes.innerText = dashboardData[3].atracao

    const clientesParque = document.getElementById('quantidade.parque')
    clientesParque.innerText = dashboardData[0].quantidade

    const clientesPlataforma = document.getElementById('quantidade.plataforma')
    clientesPlataforma.innerText = dashboardData[1].quantidade

    const clientesAbusado = document.getElementById('quantidade.abusado')
    clientesAbusado.innerText = dashboardData[2].quantidade

    const clientesPagantes = document.getElementById('quantidade.pagantes')
    clientesPagantes.innerText = dashboardData[3].quantidade

    const fating = document.getElementById('fating')
    fating.innerHTML = `<p>R$ ${dashboardData[4].quantidade}`

    const fatest = document.getElementById('fatest')
    fatest.innerHTML = `<p>R$ ${dashboardData[5].quantidade}`

    const fatloj = document.getElementById('fatloj')
    fatloj.innerHTML = `<p>R$ ${dashboardData[6].quantidade}`

    const previs0 = document.getElementById('previs0')
    previs0.innerText = dashboardData[7].quantidade

    const previs1 = document.getElementById('previs1')
    previs1.innerText = dashboardData[8].quantidade

    const previs2 = document.getElementById('previs2')
    previs2.innerText = dashboardData[9].quantidade

    const previs3 = document.getElementById('previs3')
    previs3.innerText = dashboardData[10].quantidade

    const previs4 = document.getElementById('previs4')
    previs4.innerText = dashboardData[11].quantidade

    const previs5 = document.getElementById('previs5')
    previs5.innerText = dashboardData[12].quantidade

}

(async () => {
    const dashboardData = await fetchDashboardData ()
    updateDashboardData(dashboardData)
})()