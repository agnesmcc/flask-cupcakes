$(function() {
    async function getCupcakes() {
        try {
            const response = await axios.get('/api/cupcakes');
            const cupcakes = response.data.cupcakes;
            const ul = $('<ul>').attr('id', 'cupcakes');

            cupcakes.forEach(cupcake => {
            const li = $('<li>').text(cupcake.flavor);
            ul.append(li);
            });

            $('#cupcakes').replaceWith(ul);
        } catch (error) {
            console.log(error);
        }
    }

    getCupcakes();
});
