async function createCupcake(){
    const flavor = $('#flavor').val();
    const size = $('#size').val();
    const rating = $('#rating').val();
    const image = $('#image').val();

    const response = await axios.post('/api/cupcakes', {
        flavor: flavor,
        size: size,
        rating: rating,
        image: image
    });
    console.log(response.data.cupcake);

    const li = $('<li>').text(response.data.cupcake.flavor);
    $('#cupcakes').append(li);
}

$("#add-cupcake-form").on('submit', function(e){
    e.preventDefault();
    createCupcake();
})
