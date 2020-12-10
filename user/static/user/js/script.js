function addClassStyle() {
    $("input").addClass('form-control');
    $("textarea").addClass('form-control');
    $("select").addClass('form-control');
}


function searchFood() {
    const foodsBalise = $("#allFoods").children();
    const inputSearch = $("#searchInput"); // Pour récupérer la valeur de l'input faire => inputSearch.val()
    let foods = [];

    for (const food of foodsBalise) {
        const data = {
            name: $(food).data('name'),
            id: $(food).data('id')
        };
        foods.push(data);
    }
    
    inputSearch.keyup(() => {
        if (inputSearch.val().length >= 3) {
            console.log(inputSearch.val());
        }
    });

    inputSearch.blur(() => {
        inputSearch.val("");
    });
    
    return foods;
}


$(document).ready(() => {
    addClassStyle();

    searchFood();
});