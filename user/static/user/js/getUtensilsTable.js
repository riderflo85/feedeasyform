function getSelectedUtensils(table) {
    let utensils = [];

    for (const field of table.children()) {
        const data = `${$($(field).children()[0]).data('id')}:${$($(field).children()[0]).data('name')}`;
        utensils.push(data);
    }

    return utensils;
}