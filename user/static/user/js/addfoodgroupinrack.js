function getNewFoodGroup() {
    const newFoodGroups = $('#forAddListingFoodgroup > li > input:checked');

    let newFoodGroupsId = [];

    for (const data of newFoodGroups) {
        newFoodGroupsId.push($(data).data('fg-id'));
    }

    return newFoodGroupsId;
}


$(document).ready(() => {
    const idRack = $('#nameRack').data('id-rack');
    const btnAdd = $('#btnAddGroupInRack');
    const btnDelete = $('#btnDeleteGroupInRack');
    const btnValidAdd = $('#btnSaveNewFoodGroupRack');
    const btnValidDel = $('#btnSaveDelFoodGroupRack');
    const btnCancelAdd = $('#btnCancleNewFoodGroupRack');
    const btnCancelDel = $('#btnCancleDelFoodGroupRack');
    const forAddFoodGroupBloc = $('#forAddFoodGroupRack');
    let csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    btnAdd.on('click', function() {
        $(this).prop('disabled', true);
        forAddFoodGroupBloc.slideToggle();
    });


    btnCancelAdd.on('click', function() {
        forAddFoodGroupBloc.slideToggle();
        btnAdd.prop('disabled', false);
    });


    btnValidAdd.on('click', function() {
        forAddFoodGroupBloc.slideToggle();
        btnAdd.prop('disabled', false);

        const ids = getNewFoodGroup();
        $.ajax({
            url: "/food/rack/",
            type: 'POST',
            dataType: 'json',
            data: {postType: 'put', idRack: idRack, idFoodGroup: JSON.stringify(ids)},
            success: (response) => {
                if (response.state === 'done') {
                    setTimeout(() => window.location.reload(), 500);
                }
            },
        });
    });

});