$(document).ready(() => {
    const btnEditImage = $('#btnChangeImage');
    const btnCancelImage = $('#btnCancleNewImage');
    const btnValidNewImage = $('#btnSaveNewImage');

    const imageRecipe = $('#imgRecipe');
    const inputImage = "<input type='file' name='image' accept='image/*' required id='id_image'>";


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

        imageRecipe.replaceWith(inputImage);
    });


    btnCancelImage.on('click', function() {
        const baliseInputImg = $('#id_image');
        $(this).addClass('d-none');
        btnValidNewImage.addClass('d-none');
        btnEditImage.removeClass('d-none');

        baliseInputImg.replaceWith(imageRecipe);
    });


    btnValidNewImage.on('click', function() {
        const baliseInputImg = $('#id_image');
        let formData = new FormData();

        formData.append('postType', 'update image');
        formData.append('image', baliseInputImg[0].files[0]);

        addLoadingToBtn($(this), btnCancelImage);

        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            dataType: 'json',
            data: formData,
            processData: false,
			contentType: false,
            success: (response) => {
                if (response.status === 'done') {
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