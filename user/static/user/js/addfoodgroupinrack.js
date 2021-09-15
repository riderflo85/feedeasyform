function getNewFoodGroup() {
    const newFoodGroups = $('#forAddListingFoodgroup > li > input:checked');

    let newFoodGroupsId = [];

    for (const data of newFoodGroups) {
        newFoodGroupsId.push($(data).data('fg-id'));
    }

    return newFoodGroupsId;
}


function getForDeleteFoodGroup() {
    const delFoodGroups = $('#forDelListingFoodgroup > li > input:not(:checked)');

    let delFoodGroupsId = [];

    for (const data of delFoodGroups) {
        delFoodGroupsId.push($(data).data('fg-id'));
    }

    return delFoodGroupsId;
}


function sendData(data) {
    $.ajax({
        url: "/food/rack/",
        type: 'POST',
        dataType: 'json',
        data: data,
        success: (response) => {
            if (response.state === 'done') {
                setTimeout(() => window.location.reload(), 500);
            }
        },
        error: (err) => {
            console.warn(err);
        }
    });
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
    const forDeleteFoodGroupBloc = $('#forDelFoodGroupRack');
    let csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    /* For add new food group */
    btnAdd.on('click', function() {
        $(this).prop('disabled', true);
        btnDelete.prop('disabled', false);
        forDeleteFoodGroupBloc.slideUp();
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
        const dataRequest = {
            postType: 'add',
            idRack: idRack,
            idFoodGroup: JSON.stringify(ids)
        };
        sendData(dataRequest);
    });
    /* ********************************************* */


    /* For delete food group */
    btnDelete.on('click', function() {
        $(this).prop('disabled', true);
        btnAdd.prop('disabled', false);
        forAddFoodGroupBloc.slideUp();
        forDeleteFoodGroupBloc.slideToggle();
    });


    btnCancelDel.on('click', function() {
        forDeleteFoodGroupBloc.slideToggle();
        btnDelete.prop('disabled', false);
    });


    btnValidDel.on('click', function() {
        forDeleteFoodGroupBloc.slideToggle();
        btnDelete.prop('disabled', false);

        const ids = getForDeleteFoodGroup();
        const dataRequest = {
            postType: 'delete',
            idRack: idRack,
            idFoodGroup: JSON.stringify(ids)
        };
        sendData(dataRequest);
    });
    /* ********************************************* */
});