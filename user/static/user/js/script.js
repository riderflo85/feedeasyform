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
        const newForm = `
        <label for="food-${formatedFood[0]}">${formatedFood[1]}</label>\n
        <div class="border border-primary rounded-lg mt-2 mb-3 pt-1 pb-3 px-3">
        <p class="pb-2">Quantité et unité pour la recette</p>
        <input type="number" class="form-control mb-3" name="recipe-quantity" id="quantFoodRecipe-${formatedFood[0]}" data-id="${formatedFood[0]}" placeholder="quantité">\n
        <select name="unity" class="form-control" id="unityFoodRecipe-${formatedFood[0]}" require>\n
        <option value="null" selected disabled>Choisissez une unité pour la recette</option>\n
        <option value="CL">Centilitre</option>\n
        <option value="GR">Gramme</option>\n
        <option value="CaS">Cuillère à soupe</option>\n
        <option value="CaC">Cuillère à café</option>\n
        <option value="Pincee">Pincée</option>\n
        <option value="U">Unité</option>\n
        </select>
        </div>
        <div class="border border-info rounded-lg pt-1 pb-3 px-3 mb-3">
        <p class="pb-2">Quantité et unité pour la liste d'achat</p>
        <input type="number" class="form-control mb-3" name="purchase-quantity" id="quantFoodPurchase-${formatedFood[0]}" data-id="${formatedFood[0]}" placeholder="quantité">\n
        <select name="unity" class="form-control" id="unityFoodPurchase-${formatedFood[0]}" require>\n
        <option value="null" selected disabled>Choisissez une unité pour la liste d'achat</option>\n
        <option value="CL">Centilitre</option>\n
        <option value="GR">Gramme</option>\n
        <option value="U">Unité</option>\n
        </select>
        </div>
        `;

        $(newForm).appendTo(parentNode);
        inputFields.push({
            idFood: formatedFood[0],
            label: formatedFood[1],
            inputQuantRecipe: $(`#quantFoodRecipe-${formatedFood[0]}`),
            inputQuantPurchase: $(`#quantFoodPurchase-${formatedFood[0]}`),
            selectUnitRecipe: $(`#unityFoodRecipe-${formatedFood[0]}`),
            selectUnitPurchase: $(`#unityFoodPurchase-${formatedFood[0]}`)
        });
    }
    parentNode.slideDown(500);

    return inputFields;
}


function displayFoodsAndQuantity(parentNode, fieldsInput) {
    for (const field of fieldsInput) {
        const quantRecipe = field.inputQuantRecipe.val();
        const quantPurchase = field.inputQuantPurchase.val();
        const unitRecipe = field.selectUnitRecipe.val();
        const unitPurchase = field.selectUnitPurchase.val();
        const item = `
        <tr id="${field.idFood}" data-id="${field.idFood}">
            <td data-name="${field.label}">${field.label}</td>
            <td data-recipe-quantity="${quantRecipe.trim()}">${quantRecipe.trim()}</td>
            <td data-recipe-unity="${unitRecipe.trim()}">${unitRecipe.trim()}</td>
            <td data-purchase-quant="${quantPurchase.trim()}">${quantPurchase.trim()}</td>
            <td data-purchase-unity="${unitPurchase.trim()}">${unitPurchase.trim()}</td>
            <td>
                <button class="btn btn-danger btn-sm" id="clearFoodTable-${field.idFood}">
                    <i class="fas fa-minus"></i>
                </button>
            </td>
        </tr>`;

        $(item).appendTo(parentNode);
        field.inputQuantPurchase.attr('disabled', 'true');
        field.inputQuantRecipe.attr('disabled', 'true');
        field.selectUnitPurchase.attr('disabled', 'true');
        field.selectUnitRecipe.attr('disabled', 'true');

        const btnClearFoodTable = $(`#clearFoodTable-${field.idFood}`);

        btnClearFoodTable.on('click', () => {
            const thisField = $(`#${field.idFood}`);
            thisField.fadeOut(500, () => {
                thisField.remove();
            }); 
        });
    }
    parentNode.fadeIn(500);
}


function saveSearchFoods() {
    const dataTable = $("#selectedFoods");
    let foods = []; // ex: {id: 1, name: foodName, quantity: 1, unity: g}

    for (const tr of dataTable.children()) {
        let foodInformations = {
            id: $(tr).data('id'),
        };

        for (const td of $(tr).children().slice(0,5)) {
            const dataAttr = Object.entries($(td).data())[0];
            foodInformations[dataAttr[0]] = dataAttr[1];
        }
        foods.push(foodInformations);
    }

    return foods;
}


function displayResultSearchFood(parentNode, foods) {
    for (const food of foods) {
        const item = `
        <tr id="recap-${food.id}" data-id="${food.id}">
            <td data-name="${food.name}">${food.name}</td>
            <td data-recipe-quantity="${food.recipeQuantity}">${food.recipeQuantity}</td>
            <td data-recipe-unity="${food.recipeUnity}">${food.recipeUnity}</td>
            <td data-purchase-quant="${food.purchaseQuant}">${food.purchaseQuant}</td>
            <td data-purchase-unity="${food.purchaseUnity}">${food.purchaseUnity}</td>
            <td>
                <button type="button" class="btn btn-danger btn-sm" id="clearFoodTableRecap-${food.id}">
                    <i class="fas fa-minus"></i>
                </button>
            </td>
        </tr>`;
        $(item).appendTo(parentNode);

        const btnClearFoodTableRecap = $(`#clearFoodTableRecap-${food.id}`);

        btnClearFoodTableRecap.on('click', () => {
            const thisField = $(`#recap-${food.id}`);
            thisField.fadeOut(500, () => {
                thisField.remove();
            }); 
        });
    }
}


function clearForms(form, area, table) {
    form.fadeOut(500, () => {
        form.empty();
        area.empty();
    });
    table.fadeOut(500, () => {
        table.empty();
    });
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
    const selectArea = $("#foodsResult");
    const formQuantity = $("#quantityFormBloc");
    let quantityAndUnitFields;


    selectArea.focus(() => {
        btnAddFood.removeAttr('disabled');
        formQuantity.fadeOut(500, () => {
            formQuantity.empty();
        });
    });


    inputSearch.keyup(() => {
        if (inputSearch.val().length >= 3) {
            const results = searchFood(inputSearch.val(), allFoods);
            displayResult(results);
        }
    });

    
    inputSearch.focus(() => {
        formQuantity.fadeOut(500, () => {
            formQuantity.empty();
        });
    });


    inputSearch.blur(() => {
        inputSearch.val("");
    });


    btnAddFood.on('click', () => {
        quantityAndUnitFields = displayQuantityForm(selectArea.val());
        btnAddFood.attr('disabled', 'true');
        btnValideFormQuantity.removeAttr('disabled');
    });


    btnClearFoodSelected.on('click', () => {
        clearForms(formQuantity, selectArea, listingFood);
    });


    btnValideFormQuantity.on('click', (event) => {
        displayFoodsAndQuantity(listingFood, quantityAndUnitFields);
        btnAddFood.attr('disabled', 'true');
        $(event.target).attr('disabled', 'true');
    });


    btnValideSearch.on('click', () => {
        const foodsTable = $("#allUsedFoods");
        const foods = saveSearchFoods();
        displayResultSearchFood(foodsTable, foods);
        clearForms(formQuantity, selectArea, listingFood);
    });

});