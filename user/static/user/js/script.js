function addClassStyle() {
    $("input").addClass('form-control');
    $("textarea").addClass('form-control');
    $("select").addClass('form-control');
}


function createFoodsArray() {
    const foodsBalise = $("#allFoods").children();
    
    let foods = [];

    for (const food of foodsBalise) {
        const data = {
            name: $(food).data('name'),
            id: $(food).data('id')
        };
        foods.push(data);
    }

    return foods;
}


function searchFood(text, foods) {
    return foods.filter((val) => val.name.toLowerCase().includes(text.toLowerCase()));
}


function displayResult(foods) {
    const selectArea = $("#foodsResult");
    selectArea.empty();

    for (const food of foods) {
        const data = `<option value="${food.id}:${food.name}">${food.name}</option>`;
        $(data).appendTo(selectArea);
    }
}


function displayQuantityForm(foods) {
    const parentNode = $("#quantityFormBloc");

    for (const food of foods) {
        const formatedFood = food.split(':');
        const newForm = `<label for="food-${formatedFood[0]}">${formatedFood[1]}</label>\n
        <input type="text" class="form-control mb-3" name="quantity" id="food-${formatedFood[0]}">`;

        $(newForm).appendTo(parentNode);
    }

}


$(document).ready(() => {
    addClassStyle();

    const allFoods = createFoodsArray();
    const inputSearch = $("#searchInput"); // Pour récupérer la valeur de l'input faire => inputSearch.val()
    const listingFood = $("#selectedFoods");
    const btnAddFood = $("#btnAddFood");
    const btnClearFoodSelected = $("#btnClear");
    const btnValideSearch = $("#btnValideSearch");
    const btnValideFormQuantity = $("#btnValideFormQuantity");
    const quantityFormBloc = $("#quantityFormBloc");
    const selectArea = $("#foodsResult");
    const fomrQuantity = $("#quantityFormBloc");


    selectArea.focus(() => {
        btnAddFood.removeAttr('disabled');
    });


    inputSearch.keyup(() => {
        if (inputSearch.val().length >= 3) {
            const results = searchFood(inputSearch.val(), allFoods);
            displayResult(results);
        }
    });


    inputSearch.blur(() => {
        inputSearch.val("");
    });


    btnAddFood.on('click', () => {
        displayQuantityForm(selectArea.val());
        btnAddFood.attr('disabled', 'true');
        btnValideFormQuantity.removeAttr('disabled');
    });


    btnClearFoodSelected.on('click', () => {
        listingFood.empty();
        fomrQuantity.empty();
        selectArea.empty();
    });

});