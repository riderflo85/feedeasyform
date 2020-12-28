function getFoods() {
    const dataTable = $("#allUsedFoods");
    let foods = []; // ex: {id: 1, name: foodName, quantity: 1, unity: g}

    for (const tr of dataTable.children()) {
        let foodInformations = {
            id: $(tr).data('id'),
        };

        for (const td of $(tr).children().slice(0,3)) {
            const dataAttr = Object.entries($(td).data())[0];
            foodInformations[dataAttr[0]] = dataAttr[1];
        }

        foodInformations = {
            id: foodInformations.id,
            name: foodInformations.name,
            quantity: foodInformations.quantity+" "+foodInformations.unity
        };
        foods.push(foodInformations);
    }

    return foods;
}


function getSelectedUtensils(table) {
    let utensils = [];

    for (const field of table.children()) {
        const data = `${$($(field).children()[0]).data('id')}:${$($(field).children()[0]).data('name')}`;
        utensils.push(data);
    }

    return utensils;
}


function formatedDataForRequest(data) {
    let newData = data;
    let utensils = "?";
    let foods = "?";
    let diets = "?";
    let seasons = "?";

    for (const utensil of newData.utensils) {
        utensils = utensils.concat("&u=", utensil);
    }

    for (const food of newData.foods) {
        const foodInformations = `${food.id}:${food.name}:${food.quantity}`;
        foods = foods.concat("&f=", foodInformations);
    }

    for (const diet of newData.dietary_plan) {
        diets = diets.concat("&d=", diet);
    }

    for (const season of newData.season) {
        seasons = seasons.concat("&s=", season);
    }

    newData.foods = foods;
    newData.utensils = utensils;
    newData.dietary_plan = diets;
    newData.season = seasons;

    return newData;
}


function submitForm(foods, utensils, successCb, errorCb) {
    const parentNodeFoodsTable = $("#contentFoodsCol");
    const form = $("#formNewRecipe")[0];
    const fields = Array.from(form).filter((val) => $(val).attr('id') != undefined).filter((val) => val.nodeName != "BUTTON");
    let dataForRequest = {};
    let undefinedCounterField = 0;

    parentNodeFoodsTable.removeClass(['border', 'border-danger', 'is-invalid']);

    for (const field of fields) {
        const f = $(field);

        f.on('focus', () => {
            $(f).removeClass(['border', 'border-danger', 'is-invalid']);
        });


        if (f[0].validity.valid) {
            dataForRequest[f.attr('name')] = f.val();
        } else {
            undefinedCounterField++;
            f.addClass('is-invalid');
        }
    }

    if (foods.length === 0) {
        parentNodeFoodsTable.addClass(['border', 'border-danger']);
        undefinedCounterField++;
    }

    if (utensils.length === 0) {
        $("#allUsedUtensils").parent().parent().addClass(['border', 'border-danger']);
        undefinedCounterField++;
    }

    if (undefinedCounterField === 0) {
        dataForRequest['foods'] = foods;
        dataForRequest['utensils'] = utensils;

        const dataFormated = formatedDataForRequest(dataForRequest);
        $.ajax({
            url: "/planning/new_recipe/",
            type: "POST",
            dataType: "json",
            data: dataFormated,
            success: (data) => {
                if (data.success) {
                    successCb();
                    setTimeout(() => document.location.reload(), 3000);
                } else {
                    errorCb();
                    console.warn(data);
                }
            },
            error: (error) => {
                console.log(error);
                errorCb();
            }
        });

    } else {
        errorCb();
    }
}


$(document).ready(() => {
    let csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    const btnSendRequest = $("#sendRecipeForm");
    const errorMsg = $("#errorAlert");
    const successMsg = $("#successAlert");
    const tableUtensilsFormRecipe = $("#allUsedUtensils");


    btnSendRequest.on('click', () => {
        successMsg.fadeOut(200);
        errorMsg.fadeOut(200);

        const foods = getFoods();
        const utensils = getSelectedUtensils(tableUtensilsFormRecipe);

        submitForm(foods, utensils,
            () => {
                successMsg.fadeIn(500);
                btnSendRequest.attr('disabled', 'true');
            },
            () => {errorMsg.fadeIn(500);}
        );
    });

});