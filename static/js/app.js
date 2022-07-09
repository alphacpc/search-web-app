let form = document.querySelector("#formSearch")
let inputForm = document.querySelector("#formSearch input")

form.addEventListener('submit', (e) => {
    e.preventDefault()
})

inputForm.addEventListener('keyup', async(e) => {

    let response = await fetch('/search?value='+e.target.value)
    let data = await response.json()
    console.log("Valeur de data",data)

})