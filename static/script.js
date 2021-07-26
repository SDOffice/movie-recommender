var sidenav = document.getElementById("sideNav");
var main = document.getElementById("main");
var menu = document.getElementById('menuBtn');
var footer = document.getElementById('footer');
var bg = document.getElementById("bg");

function openNav() {
    sidenav.style.width = "250px"
    main.style.transform = "translateX(-250px)"
    bg.style.transform = "translateX(-250px)"
    main.style.transition = "transform 1s"
    bg.style.transition = "transform 1s"
    footer.style.transform = "translateX(-250px)"
    footer.style.transition = "transform 1s"
    menu.onclick = function () {
        closeNav();
    };

    menu.className = "far fa-times-circle"
}

function closeNav() {
    sidenav.style.width = "0"
    main.style.transform = "translateX(0)"
    main.style.transition = "transform 0.3s"
    bg.style.transform = "translateX(0)"
    bg.style.transition = "transform 0.3s"
    footer.style.transform = "translateX(0)"
    footer.style.transition = "transform 0.3s"
    menu.onclick = function () {
        openNav();
    }
    menu.className = "fas fa-bars"
}

var scroll = new SmoothScroll('a[href*="#"]', {
    speed: 500,
    speedAsDuration: true
});


// const endpoint = 'https://gist.githubusercontent.com/saviourcode/c1b98f02cb3a0290faada2ff2000f808/raw/cc3d5d28015ddb0b713d8ca580ec430b30776ce4/titles.json';

const titles = [];
fetch("/static/titles.json")
    .then(blob => blob.json())
    .then(data => titles.push(...data));

function findMatches(wordToMatch, titles) {
    return titles.filter(place => {
        
        const regex = new RegExp(wordToMatch, 'gi');
        return place.title.match(regex)
    });
}

function displayMatches() {
    const matchArray = findMatches(this.value, titles);
    const html = matchArray.map(place => {
        const regex = new RegExp(this.value, 'gi');
        const cityName = place.title.replace(regex, `<span class="hl">${this.value}</span>`);
        const word = place.title.replace(regex, this.value);
        return  `
        <li>
        <a href = '/recommend/?title=${word}'>${cityName}</a>
        </li>
        `;
    }).join('');
    suggestions.innerHTML = html;
}

const searchInput = document.querySelector('.search');
const suggestions = document.querySelector('.suggestions');

searchInput.addEventListener('change', displayMatches);
searchInput.addEventListener('keyup', displayMatches);

// Bind keyup event on the input
$('#search').keyup(function() {
  
    // If value is not empty
    if ($(this).val().length == 0) {
      // Hide the element
      $('.suggestions').hide();
    } else {
      // Otherwise show it
      $('.suggestions').show();
    }
  }).keyup(); // Trigger the keyup event, thus running the handler on page load