function sendNewFoodName(foodId, newName, loadingCb, successCb, errorCb) {
    loadingCb();

    $.ajax({
        url: '/recipe/update_food_name/',
        type: 'POST',
        dataType: 'json',
        data: {id: foodId, new_name: newName},
        success: (response) => {
            if (response.status === 'ok') {
                successCb();
            } else {
                console.log(response);
                alert("Un aliment portant ce nom éxiste déjà, merci de corriger cela.");
                errorCb();
            }
        },
        error: (error) => {
            console.warn(error);
            errorCb();
        }
    });
}


function addLoadingToBtn(btnSave, btnCancel) {
    btnSave.attr('disabled', 'true');
    btnSave.html('... ');
    $('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>').appendTo(btnSave);
    btnCancel.attr('disabled', 'true');
}


function removeLoadingToBtn(btnSave, btnCancel) {
    btnSave.removeAttr('disabled');
    btnSave.html('<i class="fas fa-check"></i>');
    btnCancel.removeAttr('disabled');
}


$(document).ready(() => {
    const name = $('#nameFood');
    const foodId = name.data('id-food');
    const nameField = `<input type='text' name='name' id='id_name_food' required class='form-control' value="${name.contents()[0].data}">`;
    const btnEdit = $('#btnEditFoodName');
    const btnValideNewData = $('#btnValideData');
    const btnCancel = $('#btnCancelEdit');

    let csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    btnEdit.on('click', function() {
        $(this).fadeOut(400, () => {
            btnValideNewData.fadeIn();
            btnCancel.fadeIn();
        });
        name.replaceWith(nameField);
    });


    btnValideNewData.on('click', function() {
        sendNewFoodName(
            foodId,
            $('#id_name_food').val(),
            () => {
                // loadinb call back
                addLoadingToBtn($(this), btnCancel);
            },
            () => {
                // success call back
                setTimeout(() => document.location.reload(), 500);
            },
            () => {
                // error call back
                removeLoadingToBtn($(this), btnCancel);
            }
        );
    });


    btnCancel.on('click', function() {
        btnValideNewData.fadeOut();
        $(this).fadeOut(400, () => {
            btnEdit.fadeIn();
        });
        $('#id_name_food').replaceWith(name[0]);
    });
});
