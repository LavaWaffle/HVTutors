// grabs the entire service div
const serviceDiv = document.querySelector('.service-d');
// grabs the dropdown service div
const serviceCon = document.querySelector('.service-c');


// when user hovers the mouse over the service div, show the service content
serviceDiv.addEventListener('mouseenter',() => {
	if (window.innerWidth > 640) {
		serviceCon.classList.remove('hidden');
	};
});
// when the user is not hovering the mouse over the service div, do not show the service content
serviceDiv.addEventListener('mouseleave',() => {
	if (window.innerWidth > 640) {
		serviceCon.classList.add('hidden');
	};
});

// grabs the mobile service button
const serviceBtn = document.querySelector('button.service-b');
// grabs the mobile svg
const mobileSer = document.querySelector('svg.mobile-ser');
// when the user clicks the service button
serviceBtn.addEventListener('click', () => {
	// is the service content is hidden, show it
	if (serviceCon.classList.contains('hidden')) {
		serviceCon.classList.remove('hidden');
		mobileSer.classList.add('-rotate-180');
	// if the service content is not hidden, hide it
	} else {
		serviceCon.classList.add('hidden');
		mobileSer.classList.remove('-rotate-180');
	};
	
});


// grabs button element that holds both svgs
const mobileBtn = document.querySelector('button.mobile-b');
// grabs content to be shown
const divPages = document.querySelector('.pages-d');

// grabs hamburger svg
const mobileHam = document.querySelector('svg.mobile-ham');
// grabs x svg
const mobileX = document.querySelector('svg.mobile-x');
// when the mobile button is clicked
mobileBtn.addEventListener('click', () => {
	// if the content is hidden, display it
	if (divPages.classList.contains('hidden')) {
		divPages.classList.remove('hidden');
		mobileHam.classList.add('hidden');
		mobileX.classList.remove('hidden');
	// if the content is not hidden, hide it
	} else {
		divPages.classList.add('hidden');
		mobileHam.classList.remove('hidden');
		mobileX.classList.add('hidden');
	};
	
});