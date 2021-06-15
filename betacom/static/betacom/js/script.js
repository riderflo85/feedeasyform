$(document).ready(() => {
    let csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    const msgBloc = $('.msg-box');
    const inputEmail = $('#email');
    const btnValid = $('#btnSubmit');
    const errorMsgInvalid = `
        <p><i class="fas fa-info-circle"></i> Votre adresse email n'est pas une adresse valide. Merci de corriger cela.</p>
    `;
    const errorMsgUserAlreadyExist = `
        <p><i class="fas fa-info-circle"></i> Votre adresse email est déjà enregistrée en liste d'attente. Vous receverrez sous peut un email contenant toute les informations nécessaire à l'installation de la version bêta.</p>
    `;
    const successMsg = `
        <p><i class="fas fa-check-circle"></i> Féliciation, vous venez d'être enregistré sur la liste d'attente. Un email de confirmation viens de vous être envoyé.</p>
    `;

    inputEmail.on('focus', function() {
        msgBloc.empty();
        msgBloc.removeClass('success-bg', 'error-bg');
    });

    btnValid.on('click', function() {
        if (inputEmail.val().length > 0) {
            $(this).prop('disabled', true);
            $.ajax({
                url: "/beta/register",
                type: "POST",
                dataType: "json",
                data: {email: inputEmail.val()},
                success: (data) => {
                    if (Object.keys(data).includes('done')) {
                        $(successMsg).appendTo(msgBloc);
                        msgBloc.addClass('success-bg');
                        msgBloc.fadeIn();
                        setTimeout(() => document.location.reload(), 8000);
                    } else if (data.error == "User already exist") {
                        $(errorMsgUserAlreadyExist).appendTo(msgBloc);
                        msgBloc.addClass('error-bg')
                        msgBloc.fadeIn();
                        $(this).prop('disabled', false);
                        setTimeout(() => msgBloc.fadeOut(), 10000);
                    } else {
                        $(errorMsgInvalid).appendTo(msgBloc);
                        msgBloc.addClass('error-bg')
                        msgBloc.fadeIn();
                        $(this).prop('disabled', false);
                        setTimeout(() => msgBloc.fadeOut(), 10000);
                    }
                },
                error: (err) => {
                    console.warn(err);
                }
            });
        }
    });
});