function myFunction(element){
    if(!element.authorization.checked) {
        alert("Please indicate that you accept the Terms and Conditions");
        form.authorization.focus();
        return false;
    }
    if (element.GenderIdentity.value == "Male" || element.GenderIdentity.value == "female" || element.GenderIdentity.value == "I-prefer-not-to-answer"|| element.GenderIdentity.value == "Non-binary" ){
        return false;
    } else {
        alert("Please define Gender Identity ");
        form.GenderIdentity.focus();
        return false;}


}