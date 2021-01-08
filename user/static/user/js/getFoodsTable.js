function getFoods(table) {
    let foods = []; // ex: {id: 1, name: foodName, quantity: 1, unity: g}

    for (const tr of table.children()) {
        let foodInformations = {
            id: $(tr).data('id'),
        };

        for (const td of $(tr).children().slice(0,3)) {
            const dataAttr = Object.entries($(td).data())[0];
            foodInformations[dataAttr[0]] = dataAttr[1];
        }

        foodInformations = {
            id: foodInformations.id,
            name: foodInformations.name,
            quantity: foodInformations.quantity+" "+foodInformations.unity
        };
        foods.push(foodInformations);
    }

    return foods;
}