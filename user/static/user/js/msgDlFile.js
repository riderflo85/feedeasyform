$(document).ready(() => {
    const msgBloc = $('.wait-dl-msg');
    const aLinkDl = $('.a-link-dl');

    aLinkDl.on('click', function() {
        msgBloc.fadeIn();
        setTimeout(() => msgBloc.fadeOut(), 15000);
    });
});