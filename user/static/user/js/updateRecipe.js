function getFoodsAndQuantity(foodsBloc) {
    let data = [];

    for (const ulBalise of foodsBloc.children()) {
        const food = $(ulBalise)[0].innerText.replace($(ulBalise).children()[0].innerText, "");
        const quantAndUnit = $(ulBalise).children()[0].innerText;
        data.push({
            id: $(ulBalise).data('food_id'),
            foodName: food,
            quantAndUnit: quantAndUnit
        });
    }

    return data;
}


function getUtensils(utensilsBloc) {
    let data = [];

    for (const ulBalise of utensilsBloc.children()) {
        const utensil = $(ulBalise)[0].innerText;
        data.push({
            id: $(ulBalise).data('utensil_id'),
            name: utensil
        });
    }

    return data;
}


function newFieldFoodsAndQuantity(foodsBloc) {
    let updatedFoods = "";
    let manyIdBtnAndContentTable = [];

    for (const foodQuant of getFoodsAndQuantity(foodsBloc)) {
        const quantAndUnit = foodQuant.quantAndUnit.split(' ');
        const trTable = `
            <tr id="foodTableRecapResult-${foodQuant.id}" data-id="${foodQuant.id}">
                <td data-name="${foodQuant.foodName}">${foodQuant.foodName}</td>
                <td data-quantity="${quantAndUnit[0]}">${quantAndUnit[0]}</td>
                <td data-unity="${quantAndUnit[1]}">${quantAndUnit[1]}</td>
                <td>
                    <button type="button" class="btn btn-danger btn-sm" id="clearFoodTableRecap-${foodQuant.id}">
                        <i class="fas fa-minus"></i>
                    </button>
                </td>
            </tr>
        `;
        updatedFoods = updatedFoods.concat(trTable);
        manyIdBtnAndContentTable.push({idBtn: `#clearFoodTableRecap-${foodQuant.id}`, idTr: `#foodTableRecapResult-${foodQuant.id}`});
    }

    return [updatedFoods, manyIdBtnAndContentTable];
}


function newFieldUtensils(utensilsBloc) {
    let updatedUtensils = "";
    let manyIdBtnAndTr = [];

    for (const utensil of getUtensils(utensilsBloc)) {
        const trTable = `
            <tr id="utensilsResult-${utensil.id}">
                <td data-name="${utensil.name}" data-id="${utensil.id}">${utensil.name}</td>
                <td>
                    <button type="button" class="btn btn-danger btn-sm" id="clearUtensilTable-${utensil.id}">
                        <i class="fas fa-minus"></i>
                    </button>
                </td>
            </tr>
        `;
        updatedUtensils = updatedUtensils.concat(trTable);

        manyIdBtnAndTr.push({idBtn: `#clearUtensilTable-${utensil.id}`, idTr: `#utensilsResult-${utensil.id}`});
    }

    return [updatedUtensils, manyIdBtnAndTr];
}


function replaceListingByTextarea(listingBalise) {
    let value = "";

    for (const childContent of listingBalise.children()) {
        value = value.concat('\n', $(childContent).contents()[0].data);
    }

    return value.replace('\n', '');
}


function newFieldCateg(selectedCateg) {
    const dataCategs = $("#dataCategs");
    let field = "<select type='text' name='RecipeCateg' id='id_recipe_categ' required class='form-control'>$forReplaceByAllCategs$</select>";
    let options = "";

    for (const categ of dataCategs.children()) {
        if ($(selectedCateg).contents()[0].data != $(categ).data('name')) {
            options = options.concat(`<option value="${$(categ).data('id')}">${$(categ).data('name')}</option>`);
        } else {
            options = options.concat(`<option value="${selectedCateg.data('id_categ')}" selected>${$(categ).data('name')}</option>`);
        }
    }

    return field.replace('$forReplaceByAllCategs$', options);
}


function newFieldPrice(selectedPrice) {
    const dataPrice = $("#dataPriceScale");
    let field = "<select type='text' name='PriceScaleRecipe' id='id_price_scale' required class='form-control'>'>$forReplaceByAllPrices$</select>";
    let options = "";

    for (const price of dataPrice.children()) {
        if ($(selectedPrice).contents()[0].data != $(price).data('name')) {
            options = options.concat(`<option value="${$(price).data('id')}">${$(price).data('name')}</option>`);
        } else {
            options = options.concat(`<option value="${$(price).data('id')}" selected>${$(price).data('name')}</option>`);
        }
    }

    return field.replace('$forReplaceByAllPrices$', options);
}


function newFieldLevel(selectLevel) {
    const dataLevel = $("#dataLevels");
    let field = "<select type='text' name='LevelRecipe' id='id_level' required class='form-control'>'>$forReplaceByAllLevel$</select>";
    let options = "";

    for (const level of dataLevel.children()) {
        if ($(selectLevel).contents()[0].data != $(level).data('name')) {
            options = options.concat(`<option value="${$(level).data('id')}">${$(level).data('name')}</option>`);
        } else {
            options = options.concat(`<option value="${$(level).data('id')}" selected>${$(level).data('name')}</option>`);
        }
    }

    return field.replace('$forReplaceByAllLevel$', options);
}


function newFieldOrigin(selectOrigin) {
    const dataOrigin = $("#dataOrigins");
    let field = "<select type='text' name='OriginRecipe' id='id_origin' required class='form-control'>'>$forReplaceByAllOrigin$</select>";
    let options = "";

    for (const origin of dataOrigin.children()) {
        if ($(selectOrigin).contents()[0].data != $(origin).data('name')) {
            options = options.concat(`<option value="${$(origin).data('id')}">${$(origin).data('name')}</option>`);
        } else {
            options = options.concat(`<option value="${$(origin).data('id')}" selected>${$(origin).data('name')}</option>`);
        }
    }

    return field.replace('$forReplaceByAllOrigin$', options);
}


function newFieldSeason(seasonBloc) {
    const dataSeason = $("#dataSeasons");
    let field = "<select type='text' name='SeasonRecipe' id='id_season' required class='form-control' multiple>$forReplaceByAllSeason$</select>";
    let options = "";

    for (const season of dataSeason.children()) {
        let isSelected = "";
        for (const liBalise of seasonBloc.contents().filter(function() {return this.nodeName === 'LI'})) {
            if ($(liBalise).text() === $(season).data('name')) {
                isSelected = "selected";
            }
        }
        options = options.concat(`<option value="${$(season).data('id')}" ${isSelected}>${$(season).data('name')}</option>`);
    }

    return field.replace('$forReplaceByAllSeason$', options)
}


function newFieldDiet(dietBloc) {
    const dataDiet = $("#dataDiets");
    let field = "<select type='text' name='DietRecipe' id='id_dietary' required class='form-control' multiple>$forReplaceByAllDiet$</select>";
    let options = "";

    for (const diet of dataDiet.children()) {
        let isSelected = "";
        for (const liBalise of dietBloc.contents().filter(function() {return this.nodeName === 'LI'})) {
            if ($(liBalise).text() === $(diet).data('name')) {
                isSelected = "selected";
            }
        }
        options = options.concat(`<option value="${$(diet).data('id')}" ${isSelected}>${$(diet).data('name')}</option>`);
    }

    return field.replace('$forReplaceByAllDiet$', options);
}


function getAllFields() {
    const name = $('#nameRecipe');
    const nameField = `<input type='text' name='name' id='id_name_recipe' required class='form-control' value="${name.contents()[0].data}">`;
    const prepTime = $('#RecipePrepareDuration');
    const prepTimeField = `<input type='text' name='prep_time' id='id_preparation_time' required class='form-control' value="${prepTime.contents()[0].data}">`;
    const cookTime = $('#RecipeCookingTime');
    const cookTimeField = `<input type='text' name='cook_time' id='id_cooking_time' required class='form-control' value="${cookTime.contents()[0].data}">`;
    const foodsAndQuant = $('#listingFoods');
    const [foodsAndQuantField, idBtnAndBodyTable] = newFieldFoodsAndQuantity(foodsAndQuant);
    const steps = $('#listingSteps');
    const stepsField = `<textarea name='step' cols='40' rows='10' required id='id_step' class='form-control'>${replaceListingByTextarea(steps)}</textarea>`;
    const tips = $('#listingTips');
    const tipsField = `<textarea name='tip' cols='40' rows='10' required id='id_tip' class='form-control'>${replaceListingByTextarea(tips)}</textarea>`;
    const categ = $('#RecipeCateg');
    const categField = newFieldCateg(categ);
    const portion = $('#RecipePortion');
    const portionField = `<input type='number' name='portion' id='id_portion' required class='form-control' value="${portion.contents()[0].data}">`;
    const point = $('#RecipePoint');
    const pointField = `<input type='number' name='point' id='id_point' required class='form-control' value="${point.contents()[0].data}">`;
    const price = $('#RecipePriceScale');
    const priceField = newFieldPrice(price);
    const level = $('#RecipeLevel');
    const levelField = newFieldLevel(level);
    const source = $('#RecipeSource');
    const sourceField = `<input type='text' name='source' id='id_source' required class='form-control' value="${source.contents()[0].data}">`;
    const origin = $('#RecipeOrigin');
    const originField = newFieldOrigin(origin);
    const typical = $('#RecipeTypical');
    const typicalField = typical.contents().length === 0 ?
        "<input type='text' name='typical' id='id_typical' class='form-control'>"
        : `<input type='text' name='typical' id='id_typical' class='form-control' value="${typical.contents()[0].data}">`;
    const season = $('#RecipeSeason');
    const seasonField = newFieldSeason(season);
    const diet = $('#RecipeDiet');
    const dietField = newFieldDiet(diet);
    const utensil = $('#RecipeUtensils');
    const [utensilField, idBtnAndTr] = newFieldUtensils(utensil);

    const data = {
        name: {
            data: name,
            originHTML: name[0].outerHTML,
            field: nameField
        },
        prepTime: {
            data: prepTime,
            originHTML: prepTime[0].outerHTML,
            field: prepTimeField
        },
        cookTime: {
            data: cookTime,
            originHTML: cookTime[0].outerHTML,
            field: cookTimeField
        },
        foodsAndQuant: {
            data: foodsAndQuant,
            originHTML: foodsAndQuant[0].outerHTML,
            field: foodsAndQuantField,
            idBtnAndTr: idBtnAndBodyTable
        },
        steps: {
            data: steps,
            originHTML: steps[0].outerHTML,
            field: stepsField
        },
        tips: {
            data: tips,
            originHTML: tips[0].outerHTML,
            field: tipsField
        },
        categ: {
            data: categ,
            originHTML: categ[0].outerHTML,
            field: categField
        },
        portion: {
            data: portion,
            originHTML: portion[0].outerHTML,
            field: portionField
        },
        point: {
            data: point,
            originHTML: point[0].outerHTML,
            field: pointField
        },
        price: {
            data: price,
            originHTML: price[0].outerHTML,
            field: priceField
        },
        level: {
            data: level,
            originHTML: level[0].outerHTML,
            field: levelField
        },
        source: {
            data: source,
            originHTML: source[0].outerHTML,
            field: sourceField
        },
        origin: {
            data: origin,
            originHTML: origin[0].outerHTML,
            field: originField
        },
        typical: {
            data: typical,
            originHTML: typical[0].outerHTML,
            field: typicalField
        },
        season: {
            data: season,
            originHTML: season[0].outerHTML,
            field: seasonField
        },
        dietary_plan: {
            data: diet,
            originHTML: diet[0].outerHTML,
            field: dietField
        },
        utensil: {
            data: utensil,
            originHTML: utensil[0].outerHTML,
            field: utensilField,
            idBtnAndTr: idBtnAndTr
        }
    };

    return data;
}


function displayAllFields(fields) {
    for (const field in fields) {
        const thisField = $(fields[field].field);

        if (field === 'utensil') {
            fields[field].data.remove();
            const table = $('#tableUpdatedUtensils');
            const tbodyTable = $('#allUsedUtensils');
            table.removeClass('d-none');
            thisField.appendTo(tbodyTable);

            for (const ids of fields[field].idBtnAndTr) {
                const btnRemoveUtensil = $(ids.idBtn);
                btnRemoveUtensil.on('click', () => {
                    const thisFieldTable = $(ids.idTr);
                    thisFieldTable.fadeOut(500, function() {
                        $(this).remove();
                    });
                });
            }
        } else if (field === 'foodsAndQuant') {
            fields[field].data.remove();
            const tableFoods = $('#allUsedFoods');
            const tbodyTableFoods = $('#updatedFoods');
            tableFoods.removeClass('d-none');
            thisField.appendTo(tbodyTableFoods);

            for (const ids of fields[field].idBtnAndTr) {
                const btnRemoveFood = $(ids.idBtn);
                btnRemoveFood.on('click', () => {
                    const thisFieldBodyTable = $(ids.idTr);
                    thisFieldBodyTable.fadeOut(500, function() {
                        $(this).remove();
                    });
                });
            }
        } else {
            fields[field].data.replaceWith(fields[field].field);
            $(`#${thisField.attr('id')}`).on('focus', function() {
                $(this).removeClass('is-invalid');
            });
        }
    }
}


function validateUpdatedData(fields) {
    let data = {};
    let invalidFields = [];

    for (const field in fields) {
        if (field === 'utensil') {
            const utensilsTable = $('#allUsedUtensils');
            // getSelectedUtensils is defined in the getSelectedUtensils.js file
            const utensils = getSelectedUtensils(utensilsTable);
            data['utensils'] = utensils;

        } else if (field === 'foodsAndQuant') {
            const foodsTable = $('#updatedFoods');
            // getFoods is defined in the getFoods.js file
            const foods = getFoods(foodsTable);
            data['foods'] = foods;

        } else {
            const el = $(`#${$(fields[field].field).attr('id')}`);
            if (el.val().length > 0) {
                data[field] = el.val();
            } else {
                if (field === 'typical') {
                    data[field] = "";
                } else {
                    const invalid = $(`#${el.attr('id')}`).addClass('is-invalid');
                    invalidFields.push(invalid);
                }
            }
        }
    }

    return [data, invalidFields];
}


function cancelUpdate(fields) {
    for (const field in fields) {
        const id = $(fields[field].field).attr('id');

        if (field === 'utensil') {
            const table = $('#tableUpdatedUtensils');
            const utensilsBloc = $('#divUtensils');
            table.addClass('d-none');
            $(fields[field].originHTML).appendTo(utensilsBloc);
        } else if (field === 'foodsAndQuant') {
            const table = $('#allUsedFoods');
            const utensilsBloc = $('#divFoods');
            table.addClass('d-none');
            $(fields[field].originHTML).appendTo(utensilsBloc);
        } else {
            $(`#${id}`).replaceWith(fields[field].originHTML);
        }
    }
}


function sendUpdatedData(recipeInformations, loadindCb, successCb, errorCb) {
    loadindCb();

    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        dataType: 'json',
        data: recipeInformations,
        success: (response) => {
            if (response.test === 'ok') {
                successCb();
            } else {
                console.log(response);
                errorCb;
            }
        },
        error: (error) => {
            console.warn(error);
            errorCb;
        }
    });
}


function addLoadingToBtn(btnSave, btnCancel) {
    btnSave.attr('disabled', 'true');
    btnSave.html('Enregistrement...');
    $('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>').appendTo(btnSave);
    btnCancel.attr('disabled', 'true');
}


function removeLoadingToBtn(btnSave, btnCancel) {
    btnSave.attr('disabled', 'false');
    btnSave.html('<i class="fas fa-check"></i> Valider');
    btnCancel.attr('disabled', 'false');
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

    const btnEditRecipe = $('#btnEditRecipe');
    const btnCancelEdit = $('#btnCancelEdit');
    const btnSaveEdit = $('#btnSaveEdit');
    const formActions = $('#formActions');
    const btnAddUtensils = $('#btnModalUtensils');
    const btnAddFoods = $('#btnAddFoods');
    const allFields = getAllFields();

    btnAddUtensils.fadeOut(1);
    btnAddFoods.fadeOut(1);
    btnSaveEdit.fadeOut(1);
    btnCancelEdit.fadeOut(1);
    formActions.fadeOut(1);


    btnEditRecipe.on('click', () => {
        btnEditRecipe.fadeOut(500, () => {
            btnAddUtensils.fadeIn(500);
            btnAddFoods.fadeIn(500);
            btnCancelEdit.fadeIn(500);
            formActions.fadeIn(500);
            btnSaveEdit.fadeIn(500);
        });
        displayAllFields(allFields);
    });


    btnCancelEdit.on('click', () => {
        btnAddUtensils.fadeOut(500);
        btnAddFoods.fadeOut(500);
        btnCancelEdit.fadeOut(500);
        formActions.fadeOut(500);
        btnSaveEdit.fadeOut(500, () => {
            btnEditRecipe.fadeIn(500);
        });
        cancelUpdate(allFields);
        setTimeout(() => document.location.reload(), 500);
    });


    btnSaveEdit.on('click', function() {
        const [dataUpdated, invalidFields] = validateUpdatedData(allFields);
        if (invalidFields.length === 0) {
            // formatedDataForRequest is defined in the parsedRequestData.js file.
            const formatedData = formatedDataForRequest(dataUpdated);

            sendUpdatedData(formatedData,
                () => {
                    // loadinb call back
                    addLoadingToBtn($(this), btnCancelEdit);
                },
                () => {
                    // success call back
                    setTimeout(() => document.location.reload(), 1000);
                },
                () => {
                    // error call back
                    removeLoadingToBtn($(this), btnCancelEdit);
                }
            );

        } else {
            // does not send data
        }
    });
});