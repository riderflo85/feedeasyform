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


$(document).ready(() => {
    getHeightBody();
    eventCheckboxClick();

    const searchBloc = $('#searchRecipeBloc');
    const btnHideSearch = $('#chevronTop');
    const allAddRecipeBtn = $('.add-recipe-btn');
    const allRecipes = $('#displayRecipeBloc');
    const listingRecipesChoiced = $('#recipesChoiced');
    const btnValideRecipe = $('#valideChoice');

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
});