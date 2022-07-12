let form = document.querySelector("#formSearch")
let inputForm = document.querySelector("#formSearch input")
let inputFilters = document.querySelectorAll(".divFilters input")
let divVols = document.querySelector(".divVols")

let CURRENT_PAGE = 1
let PER_PAGE = 10


let generateVols = (data) => {
    divVols.innerHTML = ''
    

    if(data.data.length === 0){
        let p = document.createElement('p')
        p.classList.add("paragraph")
        p.innerText = "Aucune information pour cette recherche !"

        divVols.appendChild(p)
    }



    for(let flight of data.data){

        let divItem = document.createElement('div')
        divItem.classList.add('divVolItem')

        let content = `
                <div class="divImage">
                    <img src="static/images/${flight['_source']['AIRLINE_PHOTO']}" alt="${"test"}">
                </div>
                <div class="volInformations">
                    <h2>${flight['_source']['AIRLINE']}</h2>
                    
                    <div class="divTravel">
                        <span>${flight['_source']['ORIGIN_AIRPORT']}</span>
                        <img src="static/images/plane.svg" alt="vols">
                        <span>${flight['_source']['DESTINATION_AIRPORT']}</span>
                    </div>

                    <div class="timers">
                        <div class="timer">
                            <div>
                                <h4>Départ Prévu</h4>
                                <span>${flight['_source']['DEPART_PREVU']}</span>
                            </div>
                            <div>
                                <h4>Heure de Départ</h4>
                                <span>${flight['_source']['DEPART']}</span>
                            </div>
                        </div>

                        <div class="timer">
                            <div>
                                <h4>Arrivée Prévue</h4>
                                <span>${flight['_source']['ARRIVE_PREVU']}</span>
                            </div>
                            <div>
                                <h4>Heure d'Arrivée</h4>
                                <span>${flight['_source']['ARRIVE']}</span>
                            </div>
                        </div>
                    </div>
                    <p>${flight['_source']['DATE_FORMATED']}</p> 
                </div>
        `

        divItem.innerHTML += content
        divVols.appendChild(divItem)
    }
}


form.addEventListener('submit', (e) => {
    e.preventDefault()
})

inputForm.addEventListener('keyup', async(e) => {

    let response = await fetch('/search?value='+e.target.value)
    let data = await response.json()
    generateVols(data)

})



document.addEventListener("click", async()=>{
    let  checkers = []
    for(let input of inputFilters){
        if(input.checked){
            checkers.push(input.value)
        }
    }
    let letters = checkers.join(' ')
    let response = await fetch('/search?value='+letters)
    let data = await response.json()
    generateVols(data)
})



window.addEventListener('load', async() => {
    let res = await fetch('/data')
    let data = await res.json()
    generateVols(data)

})