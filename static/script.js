
const searchForm = document.querySelector('form');

const searchInput = document.querySelector('#search');
const healthSelect = document.querySelector('#health');
const mealTypeSelect = document.querySelector('#mealType');
const resultList = document.querySelector('#resultsSection');
const loginStatus = document.getElementById('loginStatus').value;

searchForm.addEventListener('submit', (e) => {
    e.preventDefault();
    searchRecipes();
});


async function searchRecipes() {
    const searchValue = searchInput.value.trim();
    const healthPreference = healthSelect.value;
    const mealType = mealTypeSelect.value;

    // Edamam API ID and Key
    const appId = 'afba8356';
    const appKey = '30faab0cd8893e372ae57afb15e3f958';

    const apiEndpoint = `https://api.edamam.com/search?q=${searchValue}&app_id=${appId}&app_key=${appKey}&from=0&to=10&health=${healthPreference}&mealType=${mealType}`;

    try {
        const response = await fetch(apiEndpoint);
        const data = await response.json();
        displayRecipes(data.hits);
    } catch (error) {
        console.error('Error fetching recipes:', error);
    }
}

function displayRecipes(recipes) {
    let html = '';

    if (recipes.length === 0) {
        html = '<p>No recipes found. Please try a different search.</p>';
    } else {
        if (loginStatus === "true"){
            recipes.forEach((recipe) => {
                html += `
                <div>
                    <img src="${recipe.recipe.image}" alt="${recipe.recipe.label}">
                    <h3>${recipe.recipe.label}</h3>
                    <ul>
                        ${recipe.recipe.ingredientLines.map(ingredient => `<li>${ingredient}</li>`).join('')}
                    </ul>
                    <a href="${recipe.recipe.url}" target="_blank">View Recipe</a>
                    <button class="add-to-favorites" onclick="addToFavorites('${recipe.recipe.label}', '${recipe.recipe.url}')">
    &#9829; Add to Favorites
</button>
                </div>

                `;
            });
        }
        else{
        recipes.forEach((recipe) => {
            html += `
            <div>
                <img src="${recipe.recipe.image}" alt="${recipe.recipe.label}">
                <h3>${recipe.recipe.label}</h3>
                <ul>
                    ${recipe.recipe.ingredientLines.map(ingredient => `<li>${ingredient}</li>`).join('')}
                </ul>
                <a href="${recipe.recipe.url}" target="_blank">View Recipe</a>
            </div>
            `;
        });

    }
    }

    resultList.innerHTML = html;
}

async function addToFavorites(label, url) {

    if (loginStatus === "true") {
        const response = await fetch('/add_to_favorites', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `label=${encodeURIComponent(label)}&url=${encodeURIComponent(url)}`,
        });

        const result = await response.json();
        if (result.success) {
            alert('Recipe added to favorites!');
        } else {
            alert('Failed to add recipe to favorites. Please try again.');
        }
    } else {
        alert('Please log in to add recipes to favorites.');
    }
}
