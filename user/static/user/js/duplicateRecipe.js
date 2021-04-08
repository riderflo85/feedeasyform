function sendRequest(idRecipe) {
    const errorCb = () => {
        alert("Un problème est survenu, merci d'en informer l'administrateur du site web.");
    };

    $.ajax({
        url: '/recipe/duplicate_recipe/',
        type: 'POST',
        dataType: 'json',
        data: {id: idRecipe},
        success: (response) => {
            if (response.status === 'ok') {
                window.location.reload();
            } else {
                console.log(response);
                errorCb();
            }
        },
        error: (error) => {
            console.warn(error);
            errorCb();
        }
    });
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

    for (const duplicateRecipeBtn of $('.btn-duplicate-recipe')) {
        const btn = $(duplicateRecipeBtn);
        let isDisabled = false;
        const baliseSpinner = "<div class='spinner-border spinner-border-sm text-success mr-1' role='status'><span class='sr-only'>Loading...</span></div>"

        btn.tooltip();
        btn.on('click', function() {
            if (!isDisabled) {
                btn.tooltip('disable');
                btn.removeClass(['text-success', 'btn-duplicate-recipe']);
                btn.addClass('text-secondary');
                $(baliseSpinner).prependTo(btn.parent());
                isDisabled = true;

                sendRequest(btn.data('id-recipe'));
            }
        });
    }
});