
function ToggleSidebar(targetId, clicked, other1, other2, other3){
    var clicked = document.getElementById(clicked);
    var other1 = document.getElementById(other1);
    var other2 = document.getElementById(other2);
    var other3 = document.getElementById(other3);

    var allOtherElements = [other1, other2, other3]

    var menu = document.getElementById("menu");
    var current_order = document.getElementById("current_order");
    var order_history = document.getElementById("order_history");
    var notif = document.getElementById("notification");
    var targetElement = document.getElementById(targetId);

    var allMiddleElements = [menu, current_order, order_history, notif]


    allOtherElements.forEach(function(element){

        if(element.classList.contains("selected")){
            element.classList.remove("selected");
            document.getElementById(other3)
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


function ToggleMenu(catererId, imgId, menuId) {
    var caterer = document.getElementById(catererId);
    var image = document.getElementById(imgId);
    var menu = document.getElementById(menuId);

    var class_hidden = menu.classList[1];
    console.log(menu.classList[1]);
    if (class_hidden == "hidden") {
        image.src = "icons/minus.png";
        menu.classList.remove("hidden");
    }
    else if(class_hidden == undefined){
        image.src = "icons/plus.png"
        menu.classList.add("hidden");
    }

}





