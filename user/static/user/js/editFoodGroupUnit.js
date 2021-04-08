function sendRequestEditUnit(unit, idGroup, successCb) {
    const errorCb = () => {
        alert("Un problème est survenu, merci d'en informer l'administrateur du site web.");
    };

    $.ajax({
        url: '/food/set_food_group_unit/',
        type: 'POST',
        dataType: 'json',
        data: {id: idGroup, unit: unit},
        success: (response) => {
            if (response.status === 'ok') {
                successCb();
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
    const btnEditUnit = $('#btnEditUnit');
    const formBloc = $('#blocEditUnit');
    const formField = $('#typeUnit');
    const btnValideUnit = $('#btnValideEditUnit');
    const btnCancelEdit = $('#btnCancelEditUnit');

    const successRequest = () => {
        btnEditUnit.removeAttr('disabled');
        btnValideUnit.removeAttr('disabled');
        formBloc.addClass('d-none');
        window.location.reload();
    };

    let csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    btnEditUnit.on('click', function() {
        $(this).attr('disabled', true);
        formBloc.removeClass('d-none');
    });

    btnCancelEdit.on('click', function() {
        btnEditUnit.removeAttr('disabled');
        formBloc.addClass('d-none');
    });

    btnValideUnit.on('click', function() {
        $(this).attr('disabled', true);
        if (formField.val() != "null") {
            sendRequestEditUnit(formField.val(), formBloc.data('id-group'), successRequest);
        }
    });
});