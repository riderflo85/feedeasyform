function showModalDetailRecipe(el) {
    const modalRecipe = $(`#modalRecipe${$(el).data('recipe-id')}`);
    modalRecipe.modal();
    eventCheckboxClick();
}


function displayModalEdit(day, mlp, recipes) {
    const modal = $('#modalEditPlanning');
    const modalTitle = $('#modalEditPlanningTitle');
    modal.modal();
    modalTitle.text(`${day} - ${mlp}`);

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
            $(`#checkRecipe-${$(recipe).data('id-recipe')}`).removeAttr('checked');
        });
    }
    eventCheckboxClick();
}


function addEditBtnOnRecipe(disabledBtnCallBack) {
    const tableTR = $('tbody tr');
    const tableTHEAD = $('thead tr th');
    let idForBtnChangeRecipe = 0;
    let indexMlp = 1;
    let mlps = [];

    for (const th of tableTHEAD) {
        mlps.push(String($(th).text()));
    }

    for (const tr of tableTR) {
        const day = tr.id;
        for (const td of $(tr).children()) {
            if (td.tagName != 'TH') {
                const mlp = mlps[indexMlp];
                const balise = `
                    <div class="d-flex justify-content-end mb-2">
                        <i class="fas fa-sync-alt text-success add-recipe-btn i-btn-add" data-day="${day}" data-mlp="${mlp}" id="btnAddRecipe-${idForBtnChangeRecipe}"></i>
                    </div>
                `;
                let recipes = [];
                $(balise).prependTo(td);

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
    disabledBtnCallBack();
}


function displaySearchResult(data) {
    const allRecipes = $('#displayRecipeBloc');
    allRecipes.empty();

    if (data.length > 0) {
        for (const recipe of data) {
            const recipeResultBalise = `
                <div class="col-12 col-lg-3 mb-3" id="recipeNumber-${recipe.id}">
                    <div class="content-card-recipe">
                        <div class="d-flex justify-content-between align-items-center">
                            <p class="lead">${recipe.name}</p>
                            <div class="checkbox-small">
                                <input type="checkbox" name="seleceted" id="checkRecipe-${recipe.id}">
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


function eventCheckboxClick() {
    const allRecipes = $('#displayRecipeBloc');
    const listingRecipesChoiced = $('#listingRecipe');
    let recipesChoiced = [];

    for (const recipeUsed of listingRecipesChoiced.children()) {
        recipesChoiced.push($(recipeUsed).data('recipe-name'));
    }

    for (const recipe of allRecipes.children()) {
        const checkbox = $(`#${recipe.id} div div div input`);
        const titleRecipe = $(`#${recipe.id} div div p.lead`).text();

        if (recipesChoiced.includes(titleRecipe)) {
            checkbox.attr('checked', true);
        } else {
            checkbox.removeAttr('checked');
        }
    
        checkbox.on('click', () => {
            if (!recipesChoiced.includes(titleRecipe)) {
                recipesChoiced.push(titleRecipe);
                const baliseRecipe = `
                    <li id="li-recipe-${recipe.id.split('-')[1]}" data-recipe-name="${titleRecipe}">
                        ${titleRecipe}
                        <i class="fas fa-trash-alt ml-4 text-danger i-btn-trash"></i>
                    </li>`
                ;
                $(baliseRecipe).appendTo('#listingRecipe');
                $(`#li-recipe-${recipe.id.split('-')[1]} i`).on('click', function() {
                    $(this).parent().remove();
                    $(`#checkRecipe-${recipe.id.split('-')[1]}`).removeAttr('checked');
                });
            } else {
                recipesChoiced = recipesChoiced.filter(el => el != titleRecipe);
                $(`#li-recipe-${recipe.id.split('-')[1]}`).remove();
            }
        });
    }
}


$(document).ready(() => {
    const btnEdit = $('#editPlanning');
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
        addEditBtnOnRecipe(() => {
            $(this).attr('disabled', 'true');
        });   
    });
});