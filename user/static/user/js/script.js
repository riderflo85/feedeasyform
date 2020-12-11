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
    let inputFields = [];

    for (const food of foods) {
        const formatedFood = food.split(':');
        const newForm = `<label for="food-${formatedFood[0]}">${formatedFood[1]}</label>\n
        <input type="text" class="form-control mb-3" name="quantity" id="food-${formatedFood[0]}" data-id="${formatedFood[0]}">`;

        $(newForm).appendTo(parentNode);
        inputFields.push({
            label: formatedFood[1],
            input: $(`#food-${formatedFood[0]}`)
        });
    }
    parentNode.slideDown(500);

    return inputFields;
}


function displayFoodsAndQuantity(parentNode, fieldsInput) {
    for (const field of fieldsInput) {
        const parsedData = field.input.val().split(';');
        const item = `
        <tr id="${field.input.data('id')}" data-id="${field.input.data('id')}">
            <td>${field.label}</td>
            <td>${parsedData[0].trim()}</td>
            <td>${parsedData[1].trim()}</td>
            <td>
                <button class="btn btn-danger btn-sm" id="clearFoodTable-${field.input.data('id')}">
                    <i class="fas fa-minus"></i>
                </button>
            </td>
        </tr>`;

        $(item).appendTo(parentNode);
        field.input.attr('disabled', 'true');

        const btnClearFoodTable = $(`#clearFoodTable-${field.input.data('id')}`);

        btnClearFoodTable.on('click', () => {
            const thisField = $(`#${field.input.data('id')}`);
            thisField.fadeOut(500, () => {
                thisField.remove();
            }); 
        });
    }
    parentNode.fadeIn(500);
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
    let quantityInput;


    selectArea.focus(() => {
        btnAddFood.removeAttr('disabled');
        fomrQuantity.fadeOut(500, () => {
            fomrQuantity.empty();
        });
    });


    inputSearch.keyup(() => {
        if (inputSearch.val().length >= 3) {
            const results = searchFood(inputSearch.val(), allFoods);
            displayResult(results);
        }
    });

    
    inputSearch.focus(() => {
        fomrQuantity.fadeOut(500, () => {
            fomrQuantity.empty();
        });
    });


    inputSearch.blur(() => {
        inputSearch.val("");
    });


    btnAddFood.on('click', () => {
        quantityInput = displayQuantityForm(selectArea.val());
        btnAddFood.attr('disabled', 'true');
        btnValideFormQuantity.removeAttr('disabled');
    });


    btnClearFoodSelected.on('click', () => {
        fomrQuantity.fadeOut(500, () => {
            fomrQuantity.empty();
            selectArea.empty();
        });
        listingFood.fadeOut(500, () => {
            listingFood.empty();
        });
    });


    btnValideFormQuantity.on('click', (event) => {
        displayFoodsAndQuantity(listingFood, quantityInput);
        btnAddFood.attr('disabled', 'true');
        $(event.target).attr('disabled', 'true');
    });

});