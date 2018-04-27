function ToggleSidebar(targetId, clicked, other){
    var clicked = document.getElementById(clicked);
    var other = document.getElementById(other);


    var allOtherElements = [other]

    var edit_menu = document.getElementById("menu");
    var add_meal = document.getElementById("add_meal");
    var targetElement = document.getElementById(targetId);


    var allMiddleElements = [edit_menu, add_meal]


    allOtherElements.forEach(function(element){

        if(element.classList.contains("selected")){
            element.classList.remove("selected");
            // document.getElementById(other3)
        }
    });

    allMiddleElements.forEach(function(element){
        if(element.classList.contains("hidden")){}
        else {
            element.classList.add("hidden");
        }
    });

    clicked.classList.add("selected");
    targetElement.classList.remove("hidden");
}