//validate module
var validate = (function() {
    //create private and public functions/objects/variables to validate the form
    function validateProfile(e) {
       var valid = true;

       e.preventDefault();

       if (profile.firstName.value == "") {
          document.getElementById('fnameWarning').innerHTML =
          "*Please enter a first name*";

          valid = false;
       }

       if (profile.lastName.value == "") {
          document.getElementById('lnameWarning').innerHTML =
          "*Please enter a last name*";

          valid = false;
       }

       if (profile.course.options.selectedIndex == "") {
         document.getElementById("courseWarning").innerHTML =
         "*Select one course*";

         valid = false;
       }

       if (profile.workType.options.selectedIndex == "") {
         document.getElementById("workTypeWarning").innerHTML =
         "*Select one work type*";

         valid = false;
       }

       if (profile.grades.value == "") {
          document.getElementById('gradesWarning').innerHTML =
          "*Please enter your grades*";

          valid = false;
       }

      
       if (valid) {
           alert("Thank you");

       }

       return valid;
    }
    
       return {
           validateProfile: validateProfile
       };
}());
