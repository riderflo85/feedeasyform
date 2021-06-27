$(document).ready(() => {
    const checkBox = $('#recipeIsCheck');

    let csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    checkBox.on('click', function() {
        const state = $(this).prop('checked');
        let data = {
            'postType': 'toggle_check',
            'is_checked': state
        };

        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            dataType: 'json',
            data: data,
            success: (response) => {
                if (response.status === 'done') {
                    setTimeout(() => document.location.reload(), 400);
                } else {
                    alert("Une erreur est survenue, merci d'en informer l'administrateur en présisant le nom de la recette.");
                }
            },
            error: (error) => {
                console.warn(error);
            }
        })
    });
});