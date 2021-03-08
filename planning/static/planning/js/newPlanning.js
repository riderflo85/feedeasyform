function getHeightBody() {
    windowHeight = window.innerHeight;
    section = document.getElementsByTagName('section')[0];

    if (windowHeight < section.offsetHeight) {
        $('body').css('height', '100%');
    }
}


function displaySearchRecipeBloc() {
    bloc = $('#searchRecipeBloc');

    if (!bloc.data('is-display')) {
        console.log('test');
        bloc.slideDown(400, function() {
            this.scrollIntoView();
        });
        bloc.data('is-display', true);
    }

}


$(document).ready(() => {
    getHeightBody();

    allAddRecipeBtn = $('.add-recipe-btn');

    for (const btn of allAddRecipeBtn) {
        // console.log($(btn).data('day'), $(btn).data('mlp'));
        $(btn).on('click', () => {
            displaySearchRecipeBloc();
        });

    }
});