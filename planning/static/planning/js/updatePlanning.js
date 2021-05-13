function showModalDetailRecipe(el) {
    const modalRecipe = $(`#modalRecipe${$(el).data('recipe-id')}`);
    modalRecipe.modal();
}


function displayModalEdit(day, mlp, recipes) {
    const modal = $('#modalEditPlanning');
    const modalTitle = $('#modalEditPlanningTitle');
    modal.modal();
    modalTitle.text(`${day} - ${mlp.name}`);
    modalTitle.attr("data-mlp-id", mlp.id);

    $('#listingRecipe').replaceWith("<ul id='listingRecipe'></ul>");

    for (const recipe of recipes) {
        const baliseRecipe = `
            <li id="li-recipe-${$(recipe).data('id-recipe')}" data-recipe-name="${$(recipe).text()}">
                ${$(recipe).text()}
                <i class="fas fa-trash-alt ml-4 text-danger i-btn-trash"></i>
            </li>`
        ;
        $(baliseRecipe).appendTo('#listingRecipe');
        $(`#li-recipe-${$(recipe).data('id-recipe')} i`).on('click', function() {
            $(this).parent().remove();
        });
    }
}


function addEditBtnOnRecipe(addBtn, disabledBtnCallBack) {
    const tableTR = $('tbody tr');
    const tableTHEAD = $('thead tr th');
    let idForBtnChangeRecipe = 0;
    let indexMlp = 1;
    let mlps = [];

    for (const th of tableTHEAD) {
        mlps.push(
            {id: $(th).data('mlp-id'), name: String($(th).text())}
        );
    }

    for (const tr of tableTR) {
        const day = tr.id;
        for (const td of $(tr).children()) {
            if (td.tagName != 'TH') {
                const mlp = mlps[indexMlp];
                let recipes = [];
                if (addBtn) {
                    const balise = `
                        <div class="d-flex justify-content-end mb-2">
                            <i class="fas fa-sync-alt text-success add-recipe-btn i-btn-add" data-day="${day}" data-mlp="${mlp.name}" id="btnAddRecipe-${idForBtnChangeRecipe}"></i>
                        </div>
                    `;
                    $(balise).prependTo(td);
                }

                for (const divRecipe of $(td).children()) {
                    if ($(divRecipe).hasClass('recipe-bloc')) {
                        recipes.push($(divRecipe).children()[0]);
                    }
                }

                $(`#btnAddRecipe-${idForBtnChangeRecipe}`).on('click', () => displayModalEdit(day, mlp, recipes));

                idForBtnChangeRecipe++;
                indexMlp++;
            }
        }
        indexMlp = 1;
    }
    if (disabledBtnCallBack) {
        disabledBtnCallBack();
    }
}


function displaySearchResult(data) {
    const allRecipes = $('#displayRecipeBloc');
    allRecipes.empty();

    const listingRecipesChoiced = $('#listingRecipe');
    let recipesChoiced = [];

    for (const recipeUsed of listingRecipesChoiced.children()) {
        recipesChoiced.push($(recipeUsed).data('recipe-name'));
    }

    if (data.length > 0) {
        for (const recipe of data) {
            const recipeResultBalise = `
                <div class="col-12 col-lg-3 mb-3" id="recipeNumber-${recipe.id}">
                    <div class="content-card-recipe">
                        <div class="d-flex justify-content-between align-items-center">
                            <p class="lead">${recipe.name}</p>
                            <div class="checkbox-small btn-group btn-group-sm" role="group">
                                <button class="btn btn-sm btn-primary" id="checkRecipe-${recipe.id}"><i class="fas fa-check"></i></button>
                            </div>
                        </div>
                        <div class="d-flex mt-2">
                            <div class="image-bloc">
                                <img src="${recipe.image}" alt="image of the recipe" class="img-fluid">
                            </div>
                            <div class="data-recipe">
                                <p>${recipe.categ}</p>
                                <hr class="hr-data-recipe">
                                <p>${recipe.seasons.toString()}</p>
                                <hr class="hr-data-recipe">
                                <p>${recipe.diets.toString()}</p>
                            </div>
                        </div>
                    </div>
                </div>
            `;
            $(recipeResultBalise).appendTo(allRecipes);
        }
    } else {
        const errorMessage = `
            <div class="col-12">
                <h4 class="text-danger">Aucune recette n'a été trouvée dans la base de données.</h4>
            </div>
        `;
        $(errorMessage).appendTo(allRecipes)
    }
    eventCheckboxClick();
}


function searchRecipe(text) {
    $.ajax({
        url: "/planning/search",
        type: "GET",
        dataType: "json",
        data: {'text': text},
        success: (data) => {
            displaySearchResult(data.recipes);
        },
        error: (error) => {
            console.warn(error);
        }
    });
}


function filteredRecipe(dataFilterAndText) {
    $.ajax({
        url: "/planning/filter",
        type: "GET",
        dataType: "json",
        data: dataFilterAndText,
        success: (data) => {
            displaySearchResult(data.recipes);
        },
        error: (error) => {
            console.warn(error);
        }
    });
}


function sendUpdatedData(data, successCb) {
    $.ajax({
        url: "/planning/updated/",
        type: "POST",
        dataType: "json",
        data: data,
        success: (data) => {
            if (data.status === true) {
                successCb();
                window.location.reload();
            }
        },
        error: (error) => {
            console.warn(error);
        }
    });
}


function eventCheckboxClick() {
    const allRecipes = $('#displayRecipeBloc');

    for (const recipe of allRecipes.children()) {
        const checkbox = $(`#${recipe.id} div div div button`);
        const titleRecipe = $(`#${recipe.id} div div p.lead`).text();

        checkbox.on('click', () => {
            const baliseRecipe = `
                <li id="li-recipe-${recipe.id.split('-')[1]}" data-recipe-name="${titleRecipe}">
                    ${titleRecipe}
                    <i class="fas fa-trash-alt ml-4 text-danger i-btn-trash"></i>
                </li>`
            ;
            $(baliseRecipe).appendTo('#listingRecipe');
            $(`#li-recipe-${recipe.id.split('-')[1]} i`).on('click', function() {
                $(this).parent().remove();
            });
        });
    }
}


function getRecipeChoiced() {
    let listingRecipe = $('#listingRecipe');
    let modalTitle = $('#modalEditPlanningTitle');
    let momentDay = modalTitle.text();
    let tdTable = $(`#${momentDay.split(' - ')[0]}-${modalTitle.attr('data-mlp-id')}`);
    let recipes = [];

    for (const li of listingRecipe.children()) {
        recipes.push({id:li.id.split('-')[2], name: $(li).data('recipe-name')});
    }

    for (const div of tdTable.children()) {
        if ($(div).hasClass('recipe-bloc')) {
            $(div).remove();
        }
    }

    for (const recipe of recipes) {
        let newBalise = `
            <div class="d-flex justify-content-center align-items-center recipe-bloc">
                <p class="title-recipe" data-id-recipe="${recipe.id}">${recipe.name}</p>
            </div>
        `;
        $(newBalise).appendTo(tdTable);
    }
    addEditBtnOnRecipe();
}


function getAllRecipeInPlanning(planningName, planningId) {
    const tableTR = $('tbody tr');

    const data = {};
    let planningIsCompleted = false;

    blocCheckData: {
        for (const tr of tableTR) {
            data[`${tr.id}-${tr.getAttribute('data-id-day')}`] = "?";
            for (const td of $(tr).children()) {
                if (td.tagName != 'TH') {
                    let encodeRecipe = "";
                    for (const div of $($(td).children())) {
                        if ($(div).hasClass('recipe-bloc')) {
                            const recipe = $(div).children()[0];
                            encodeRecipe = encodeRecipe + `_${$(recipe).data('id-recipe')}`;
                        }
                    }
                    if (encodeRecipe != "") {
                        data[`${tr.id}-${tr.getAttribute('data-id-day')}`] = data[`${tr.id}-${tr.getAttribute('data-id-day')}`] + `&${td.id}=${encodeRecipe}`;
                        planningIsCompleted = true;
                    } else {
                        planningIsCompleted = false;
                        break blocCheckData;
                    }
                }
            }
        }
    }
    if (planningName != "" && planningIsCompleted) {
        planningIsCompleted = true;
        data['name'] = planningName;
        data['id'] = planningId;
    } else {
        planningIsCompleted = false;
    }

    return [data, planningIsCompleted];
}


function newOriginField(selectOrigin) {
    const dataOrigin = $("#dataOrigins");
    let field = "<select type='text' name='OriginPlanning' id='id_origin_planning' required class='form-control mr-5'>'>$forReplaceByAllOrigin$</select>";
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


function newSeasonField(selectSeason) {
    const dataSeason = $("#dataSeasons");
    let field = "<select type='text' name='SeasonPlanning' id='id_season_planning' required class='form-control mr-5'>'>$forReplaceSeason$</select>";
    let options = "";

    for (const season of dataSeason.children()) {
        if ($(selectSeason).contents()[0].data != $(season).data('name')) {
            options = options.concat(`<option value="${$(season).data('id')}">${$(season).data('name')}</option>`);
        } else {
            options = options.concat(`<option value="${$(season).data('id')}" selected>${$(season).data('name')}</option>`);
        }
    }

    return field.replace('$forReplaceSeason$', options);
}


function newDietField(selectDiet) {
    const dataDiet = $("#dataDiets");
    let field = "<select type='text' name='DietPlanning' id='id_diet_planning' required class='form-control mr-5'>'>$forReplaceDiet$</select>";
    let options = "";

    for (const diet of dataDiet.children()) {
        if ($(selectDiet).contents()[0].data != $(diet).data('name')) {
            options = options.concat(`<option value="${$(diet).data('id')}">${$(diet).data('name')}</option>`);
        } else {
            options = options.concat(`<option value="${$(diet).data('id')}" selected>${$(diet).data('name')}</option>`);
        }
    }

    return field.replace('$forReplaceDiet$', options);
}


function newPremiumField(premiumStateJqObject) {
    let state = '';
    if (premiumStateJqObject.data('is-premium') === 'True') {
        state = 'checked';
    }
    
    return `<input type="checkbox" name="premium" id="is_premium_planning" class="form-control mr-5" ${state}>`
}


function displayAllFieldsInformations() {
    const name = $('#namePlanning');
    const season = $('#id_season_planning');
    const origin = $('#id_origin_planning');
    const diet = $('#id_diet_planning');
    const premium = $('#is_premium_planning');

    const nameField = `<input type='text' name='namePlanning' id='namePlanning' required class='form-control mr-5' value="${name.contents()[0].data}" data-id-planning="${name.data('id-planning')}">`;
    const seasonField = newSeasonField(season);
    const originField = newOriginField(origin);
    const dietField = newDietField(diet);
    const premiumField = newPremiumField(premium);

    name.replaceWith(nameField);
    season.replaceWith(seasonField);
    origin.replaceWith(originField);
    diet.replaceWith(dietField);
    premium.replaceWith(premiumField);
}


function getAllManyInformations() {
    const name = $('#namePlanning');
    const season = $('#id_season_planning');
    const origin = $('#id_origin_planning');
    const diet = $('#id_diet_planning');
    const premium = $('#is_premium_planning');
    let done = true;

    if (name.val() === "") {
        done = false;
        name.addClass('is-invalid');
        name.on('focus', function() {
            name.removeClass('is-invalid');
        });
    }

    const data = {
        name: name.val(),
        season: season.val(),
        origin: origin.val(),
        diet: diet.val(),
        premium: premium.prop('checked')
    };

    return [data, done];

}


$(document).ready(() => {
    const btnEdit = $('#editPlanning');
    const btnValid = $('#confirmPlanning');
    const btnModalSaveRecipe = $('#saveChangeBtn');
    const searchInput = $('#inputSearchRecipe');
    const btnValideFilter = $('#valideFilter');
    let csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    searchInput.keyup(function() {
        let textUser = $(this).val();
        if (textUser.length >= 3) {
            searchRecipe(textUser);
        }
    });

    btnValideFilter.on('click', () => {
        const categFilter = $('#categorieFilter').val();
        const originFilter = $('#originFilter').val();
        const dietFilter = $('#dietFilter').val();
        const seasonFilter = $('#seasonFilter').val();

        const data = {
            categ: categFilter,
            origin: originFilter,
            diet: dietFilter,
            season: seasonFilter,
            text: searchInput.val()
        }

        filteredRecipe(data);
    });

    btnEdit.on('click', function() {
        addEditBtnOnRecipe(true, () => {
            $(this).attr('disabled', 'true');
        });
        btnValid.removeAttr('disabled');
        displayAllFieldsInformations();
    });

    btnValid.on('click', function() {
        const loadingSpinner = $('#loading');
        loadingSpinner.removeClass('d-none');
        $(this).attr('disabled', true);
        const [recipes, state1] = getAllRecipeInPlanning($('#namePlanning').val(), $('#namePlanning').data('id-planning'));
        const [manyData, state2] = getAllManyInformations();

        if (state1 && state2) {
            const dataForRequest = Object.assign(recipes, manyData);
            sendUpdatedData(dataForRequest, function() {loadingSpinner.addClass('d-none');});
        }
    });

    btnModalSaveRecipe.on('click', () => {
        getRecipeChoiced();
    });

    eventCheckboxClick();
});