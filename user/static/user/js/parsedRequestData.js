function formatedDataForRequest(data) {
    let newData = data;
    let utensils = "?";
    let foods = "?";
    let diets = "?";
    let seasons = "?";
    let categs = "?";

    for (const utensil of newData.utensils) {
        utensils = utensils.concat("&u=", utensil);
    }

    for (const food of newData.foods) {
        const foodInformations = `${food.id}:${food.name}:${food.quantity}`;
        foods = foods.concat("&f=", foodInformations);
    }

    for (const diet of newData.dietary_plan) {
        diets = diets.concat("&d=", diet);
    }

    for (const season of newData.season) {
        seasons = seasons.concat("&s=", season);
    }

    for (const categ of newData.categories) {
        categs = categs.concat("&c=", categ);
    }

    newData.foods = foods;
    newData.utensils = utensils;
    newData.dietary_plan = diets;
    newData.season = seasons;
    newData.categories = categs;

    return newData;
}