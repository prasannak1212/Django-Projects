let cards = document.querySelectorAll('.card');



// One of the techniques to do scroll animation
// window.addEventListener('scroll', animate);

// function animate() {
//     const trigger = window.innerHeight/5 * 4;
//     cards.forEach(card => {
//         const cardTop = card.getBoundingClientRect().top;
//         if (cardTop < trigger) {
//             card.classList.add('show');
//         } else {
//             card.classList.remove('show');
//         }
//     })
// }

const searchInput = document.querySelector('#search-input');

function searchFilter() {
    const search = searchInput.value.toLowerCase();
    cards.forEach((card) => {
        const animalName = card.getAttribute('data-name').toLowerCase();

        if (animalName.includes(search)){
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    })
}

searchInput.addEventListener('keyup', searchFilter);

const filters = document.querySelectorAll('.filter-btn');

filters.forEach( (filter_btn) => {
    filter_btn.addEventListener('click', () => {
        const filter = filter_btn.getAttribute('data-filter').toLowerCase();
        console.log(filter);
        cards.forEach((card) => {
            const animalType = card.getAttribute('data-food').toLowerCase();
            console.log(animalType);
            if((filter == animalType) || filter == 'all' ){
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        })
    });
});

