function submitForm(foods, utensils, successCb, errorCb) {
    const parentNodeFoodsTable = $("#contentFoodsCol");
    const form = $("#formNewRecipe")[0];
    const fields = Array.from(form).filter((val) => $(val).attr('id') != undefined).filter((val) => val.nodeName != "BUTTON");
    let dataForRequest = {};
    let undefinedCounterField = 0;

    parentNodeFoodsTable.removeClass(['border', 'border-danger', 'is-invalid']);

    for (const field of fields) {
        const f = $(field);

        f.on('focus', () => {
            $(f).removeClass(['border', 'border-danger', 'is-invalid']);
        });


        if (f[0].validity.valid) {
            dataForRequest[f.attr('name')] = f.val();
        } else {
            undefinedCounterField++;
            f.addClass('is-invalid');
        }
    }

    if (foods.length === 0) {
        parentNodeFoodsTable.addClass(['border', 'border-danger']);
        undefinedCounterField++;
    }

    if (utensils.length === 0) {
        $("#allUsedUtensils").parent().parent().addClass(['border', 'border-danger']);
        undefinedCounterField++;
    }

    if (undefinedCounterField === 0) {
        dataForRequest['foods'] = foods;
        dataForRequest['utensils'] = utensils;

        // formatedDataForRequest is defined in the parsedRequestData.js file.
        const dataFormated = formatedDataForRequest(dataForRequest);
        $.ajax({
            url: "/planning/new_recipe/",
            type: "POST",
            dataType: "json",
            data: dataFormated,
            success: (data) => {
                if (data.success) {
                    successCb();
                    setTimeout(() => document.location.reload(), 3000);
                } else {
                    errorCb();
                    console.warn(data);
                }
            },
            error: (error) => {
                console.log(error);
                errorCb();
            }
        });

    } else {
        errorCb();
    }
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

    const btnSendRequest = $("#sendRecipeForm");
    const errorMsg = $("#errorAlert");
    const successMsg = $("#successAlert");
    const tableUtensilsFormRecipe = $("#allUsedUtensils");
    const tableFoodsFormRecipe = $("#allUsedFoods");


    btnSendRequest.on('click', () => {
        successMsg.fadeOut(200);
        errorMsg.fadeOut(200);

        const foods = getFoods(tableFoodsFormRecipe);
        const utensils = getSelectedUtensils(tableUtensilsFormRecipe);

        submitForm(foods, utensils,
            () => {
                successMsg.fadeIn(500);
                btnSendRequest.attr('disabled', 'true');
            },
            () => {errorMsg.fadeIn(500);}
        );
    });

});