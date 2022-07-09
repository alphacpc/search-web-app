let form = document.querySelector("#formSearch")
let inputForm = document.querySelector("#formSearch input")
let inputFilters = document.querySelectorAll(".divFilters input")


form.addEventListener('submit', (e) => {
    e.preventDefault()
})

inputForm.addEventListener('keyup', async(e) => {

    let response = await fetch('/search?value='+e.target.value)
    let data = await response.json()
    console.log("Valeur de data",data)

})



document.addEventListener("click", ()=>{
    let  checkers = []
    for(let input of inputFilters){
        if(input.checked){
            checkers.push(input.value)
        }
    }
    console.log("Checkers :", checkers)
})