//form element events
document.getElementById("fname").addEventListener("blur", function() {
    if (profile.firstName.value !== "") {
       fnameWarning.innerHTML = "";
    }
});

document.getElementById("lname").addEventListener("blur", function() {
    if (profile.lastName.value !== "") {
       lnameWarning.innerHTML = "";
    }
});

document.getElementById("course").addEventListener("click", function() {
    if (profile.course.options.selectedIndex !== "") {
        courseWarning.innerHTML = "";
    }
});

document.getElementById("workType").addEventListener("click", function() {
    if (profile.workType.options.selectedIndex !== "") {
        workTypeWarning.innerHTML = "";
    }
});

document.getElementById("grades").addEventListener("blur", function() {
    if (profile.grades.value !== "") {
       fnameWarning.innerHTML = "";
    }
});

document.profile.addEventListener("submit",function(){
     if(validate.validateProfile(event)){
        document.getElementById("profile").submit();
}
});
document.getElementById("displayBtn").addEventListener("click", function(){
    window.location = "display.html";
});

