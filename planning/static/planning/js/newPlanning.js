function getHeightBody() {
    windowHeight = window.innerHeight;
    section = document.getElementsByTagName('section')[0];

    if (windowHeight < section.offsetHeight) {
        $('body').css('height', '100%');
    }
}


function displaySearchRecipeBloc(day, meal) {
    bloc = $('#searchRecipeBloc');
    dayTitle = $('#daySearchTitle');
    mealTitle = $('#mealSearchTitle');

    if (!bloc.data('is-display')) {
        bloc.slideDown(400, function() {
            this.scrollIntoView();
            getHeightBody();
        });
        bloc.data('is-display', true);
    }
    dayTitle.text(day);
    mealTitle.text(meal);

}


$(document).ready(() => {
    getHeightBody();

    allAddRecipeBtn = $('.add-recipe-btn');

    for (const btn of allAddRecipeBtn) {
        // console.log($(btn).data('day'), $(btn).data('mlp'));
        $(btn).on('click', () => {
            displaySearchRecipeBloc(
                $(btn).data('day'),
                $(btn).data('mlp')
            );
        });

    }
});