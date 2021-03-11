function getHeightBody() {
    const windowHeight = window.innerHeight;
    const section = document.getElementsByTagName('section')[0];

    if (windowHeight < section.offsetHeight) {
        $('body').css('height', '100%');
    } else {
        $('body').css('height', '100vh');
    }
}


function displaySearchRecipeBloc(bloc, day, meal) {
    const dayTitle = $('#daySearchTitle');
    const mealTitle = $('#mealSearchTitle');

    if (!bloc.data('is-display')) {
        bloc.slideDown(400, function() {
            this.scrollIntoView();
            getHeightBody();
        });
        bloc.data('is-display', true);
    }
    const dayData = day.split('&');
    const mealData = meal.split('&');
    dayTitle.text(dayData[0]);
    dayTitle.data('id', dayData[1]);
    mealTitle.text(mealData[0]);
    mealTitle.data('id', mealData[1]);

}


function eventCheckboxClick() {
    const allRecipes = $('#displayRecipeBloc');
    const listingRecipesChoiced = $('#recipesChoiced');
    let recipesChoiced = [];

    for (const recipe of allRecipes.children()) {
        const checkbox = $(`#${recipe.id} div div div input`);
        const titleRecipe = $(`#${recipe.id} div div p.lead`).text();
    
        checkbox.on('click', () => {
            if (!recipesChoiced.includes(titleRecipe)) {
                recipesChoiced.push(titleRecipe);
                const balise = `<span class="badge badge-pill badge-success" id="${recipe.id}">${titleRecipe}</span>`;
                $(balise).appendTo(listingRecipesChoiced);
            } else {
                recipesChoiced = recipesChoiced.filter(el => el != titleRecipe);
                $(`#${recipe.id}`).remove();
            }
        });
    }
}


function hideSearchRecipeBloc(bloc) {
    if (bloc.data('is-display')) {
        bloc.slideUp(400, function() {
            getHeightBody();
        });
        bloc.data('is-display', false);
    }
}


function clearSearchBloc(blocRecipeChoiced, allRecipes) {
    blocRecipeChoiced.empty();
    for (const recipe of allRecipes.children()) {
        $(`#${recipe.id} div div div input`).replaceWith(
            `<input type="checkbox" name="seleceted" id="${recipe.id}">`
        );
    }
    eventCheckboxClick();
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
    getHeightBody();

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


$(document).ready(() => {
    getHeightBody();
    eventCheckboxClick();

    const searchBloc = $('#searchRecipeBloc');
    const btnHideSearch = $('#chevronTop');
    const allAddRecipeBtn = $('.add-recipe-btn');
    const allRecipes = $('#displayRecipeBloc');
    const listingRecipesChoiced = $('#recipesChoiced');
    const btnValideRecipe = $('#valideChoice');
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

    for (const btn of allAddRecipeBtn) {
        $(btn).on('click', () => {
            displaySearchRecipeBloc(
                searchBloc,
                $(btn).data('day'),
                $(btn).data('mlp')
            );
        });
    }

    btnHideSearch.on('click', () => hideSearchRecipeBloc(searchBloc));

    btnValideRecipe.on('click', () => {
        let dataNewRecipe = [];
        const idDay = $('#daySearchTitle').data('id');
        const idMlp = $('#mealSearchTitle').data('id');
        const tdTable = $(`#${idDay}-${idMlp}`);

        for (const recipeData of listingRecipesChoiced.children()) {
            dataNewRecipe.push(
                {id: recipeData.id, name: recipeData.innerText}
            );
            const baliseRecipeTable = `<div class="d-flex justify-content-center align-items-center recipe-bloc">
            <p class="title-recipe">${recipeData.innerText}</p>
            <i class="fas fa-trash-alt text-danger ml-2 i-btn-trash" id="removeRecipe${recipeData.id}"></i>
            </div>`;
            $(baliseRecipeTable).appendTo(tdTable);
            const btnRemoveRecipe = $(`#removeRecipe${recipeData.id}`);

            btnRemoveRecipe.on('click', function() {$(this).parent().remove();});
        }
        hideSearchRecipeBloc(searchBloc);
        clearSearchBloc(listingRecipesChoiced, allRecipes);
    });

    searchInput.keyup(function() {
        let textUser = $(this).val();
        if (textUser.length >= 3) {
            console.log(textUser);
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
});