function getAllUtensils() {
    const utensilsBalise = $("#allUtensils").children();

    let utensils = [];

    for (const utensil of utensilsBalise) {
        const data = {
            id: $(utensil).data('id'),
            name: $(utensil).data('name')
        };
        utensils.push(data);
    }

    return utensils;
}


function searchUtensil(text, utensils) {
    return utensils.filter((val) => val.name.toLowerCase().includes(text.toLowerCase()));
}


function addUtenstilsToTable(parentNode, utensils, modal=false) {
    for (const utensil of utensils) {
        const [id, name] = utensil.split(':');
        if (modal) {
            const item = `
            <tr id="utensilsModalResult-${id}">
                <td data-name="${name}" data-id="${id}">${name}</td>
                <td>
                    <button type="button" class="btn btn-danger btn-sm" id="clearUtensilTableModal-${id}">
                        <i class="fas fa-minus"></i>
                    </button>
                </td>
            </tr>`;
            $(item).appendTo(parentNode);
    
            const btnClearUtensil = $(`#clearUtensilTableModal-${id}`);
            btnClearUtensil.on('click', () => {
                const thisField = $(`#utensilsModalResult-${id}`);
                thisField.fadeOut(500, () => {
                    thisField.remove();
                });
            });
        } else {
            const item = `
            <tr id="utensilsResult-${id}">
                <td data-name="${name}" data-id="${id}">${name}</td>
                <td>
                    <button type="button" class="btn btn-danger btn-sm" id="clearUtensilTable-${id}">
                        <i class="fas fa-minus"></i>
                    </button>
                </td>
            </tr>`;
            $(item).appendTo(parentNode);
    
            const btnClearUtensil = $(`#clearUtensilTable-${id}`);
            btnClearUtensil.on('click', () => {
                const thisField = $(`#utensilsResult-${id}`);
                thisField.fadeOut(500, () => {
                    thisField.remove();
                });
            });
        }
    }
    parentNode.fadeIn(500);
}


function displayUtensilsSearchResult(utensils, selectNode) {
    selectNode.empty();
    for (const utensil of utensils) {
        const item = `<option value="${utensil.id}:${utensil.name}">${utensil.name}</option>`;
        $(item).appendTo(selectNode);
    }
}


function clearUtensilForms(area, table) {
    table.fadeOut(500, () => {
        table.empty();
        area.empty();

    });
}


function getUtensilsTable(table) {
    let utensils = [];

    for (const field of table.children()) {
        const data = `${$($(field).children()[0]).data('id')}:${$($(field).children()[0]).data('name')}`;
        utensils.push(data);
    }

    return utensils;
}


$(document).ready(() => {
    const btnSelectUtensils = $("#btnAddUtensil");
    const selectInput = $("#utensilsResult");
    const tableUtensils = $("#selectedUtensils");
    const btnClearSearch = $("#btnUtensilClear");
    const inputSearch = $("#searchUtensilInput");
    const allUtensils = getAllUtensils();
    const btnSaveUtensilSearch = $("#btnValideSearchUtensil");
    const tableUtensilsFormRecipe = $("#allUsedUtensils");


    selectInput.focus(() => {
        btnSelectUtensils.removeAttr('disabled');
    });


    btnSelectUtensils.on('click', () => {
        addUtenstilsToTable(tableUtensils, selectInput.val(), modal=true);
        btnSelectUtensils.attr('disabled', 'true');
    });


    btnClearSearch.on('click', () => {
        clearUtensilForms(selectInput, tableUtensils);
    });


    inputSearch.keyup(() => {
        if (inputSearch.val().length === 0) {
            displayUtensilsSearchResult(allUtensils, selectInput);
        } else if (inputSearch.val().length >= 3) {
            const results = searchUtensil(inputSearch.val(), allUtensils);
            displayUtensilsSearchResult(results, selectInput);
        }
    });


    btnSaveUtensilSearch.on('click', () => {
        const utensilesSelected = getUtensilsTable(tableUtensils);
        if (utensilesSelected.length > 0) {
            addUtenstilsToTable(tableUtensilsFormRecipe, utensilesSelected);
        }
        tableUtensils.empty();
    });
});