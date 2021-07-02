function addLoadingToBtn(btnSave, btnCancel) {
    btnSave.attr('disabled', 'true');
    btnSave.html('... ');
    $('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>').appendTo(btnSave);
    btnCancel.attr('disabled', 'true');
}

$(document).ready(() => {
    const btnEditImage = $('#btnChangeImageCategRecipe');
    const btnCancelImage = $('#btnCancleNewImageCategRecipe');
    const btnValidNewImage = $('#btnSaveNewImageCategRecipe');

    const imagesPicto = $('#imgPictoCategRecipeBloc');
    const inputs = `<div id="inputsFields">
        <p class='mb-2'>picto active: <input type='file' name='imageActive' accept='image/*' required id='id_image_active'></p>
        <p class='mb-2'>picto inactive: <input type='file' name='imageNotActive' accept='image/*' required id='id_image_not_active'></p>
    </div>
    `;


    let csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    btnEditImage.on('click', function() {
        $(this).addClass('d-none');
        btnCancelImage.removeClass('d-none');
        btnValidNewImage.removeClass('d-none');

        imagesPicto.replaceWith(inputs);
    });


    btnCancelImage.on('click', function() {
        const baliseInputImgActive = $('#inputsFields');
        $(this).addClass('d-none');
        btnValidNewImage.addClass('d-none');
        btnEditImage.removeClass('d-none');

        baliseInputImgActive.replaceWith(imagesPicto);
    });


    btnValidNewImage.on('click', function() {
        const baliseInputImgActive = $('#id_image_active');
        const baliseInputImgNotActive = $('#id_image_not_active');
        let formData = new FormData();
        
        formData.append('postType', 'update image');
        formData.append('image_active', baliseInputImgActive[0].files[0]);
        formData.append('image_not_active', baliseInputImgNotActive[0].files[0]);

        /* Is used for change the StoreRack picto */
        let url = $(this).data('url');
        if (url === undefined) {
            url = window.location.pathname;
        } else {
            formData.append('idRack', $('#nameRack').data('id-rack'));
        }
        /* ******************************************** */

        addLoadingToBtn($(this), btnCancelImage);

        $.ajax({
            url: url,
            type: 'POST',
            dataType: 'json',
            data: formData,
            processData: false,
			contentType: false,
            success: (response) => {
                if (response.status === 'done' || response.state === 'done') {
                    $(this).addClass('d-none');
                    btnValidNewImage.addClass('d-none');
                    btnEditImage.removeClass('d-none');
                    setTimeout(() => document.location.reload(), 1000);
                } else {
                    btnValidNewImage.attr('disabled', 'false');
                    btnValidNewImage.html('<i class="fas fa-check"></i> Valider');
                    console.warn(response);
                }
            },
            error: (error) => {
                console.warn(error);
                removeLoadingToBtn($(this), btnCancelImage);
            }
        });
    });
});