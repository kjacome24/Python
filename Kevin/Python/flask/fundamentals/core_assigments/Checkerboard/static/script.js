function invertcolor(element){
    /*For first par without extra colors*/
    if (element.classList.value == "cola"){
        element.classList.value = "colb"
    } else {
        element.classList.value = "cola"
    }
        /*For rebeccapurple and peachpuff */
    if (element.style.backgroundColor == "rebeccapurple"){
        element.style.backgroundColor = "peachpuff"
    } else if (element.style.backgroundColor == "peachpuff") {
        element.style.backgroundColor = "rebeccapurple"
    }
}

function revertcolor(element){
    /*For first par without extra colors*/ 
    if (element.classList.value == "cola"){
        element.classList.value = "colb"
    } else {
        element.classList.value = "cola"
    }
    /*For rebeccapurple and peachpuff */
    // element.style.removeProperty('background-color');Test
    if (element.style.backgroundColor == "peachpuff"){
        element.style.backgroundColor = "rebeccapurple"
    } else if (element.style.backgroundColor == "rebeccapurple") {
        element.style.backgroundColor = "peachpuff"
    }
    }
