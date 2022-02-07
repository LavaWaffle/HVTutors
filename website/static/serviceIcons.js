// func that takes in img ele and img src path and changes the src of the img
		function changeSrc(element, path) {
			element.src = path;
		}
		// grabs all div elements with ad class
		const aAdvertisements = document.querySelectorAll('a.ad');
		
		aAdvertisements.forEach(ad => {
			console.log(ad)
			// gets corresponding img from img array
			let img = document.createElement('img');
			// sets images first img
			img.src = `../static/images/serviceIcons/Grey${ad.id}Icon.png`
			// sets image alt
			img.alt = `${ad.id} icon advertisement`;
			// adds classes to img class
			img.className += 'h-40 w-h md:h-36 rounded-lg border border-2 border-teal-50 hover:border-teal-100 transition ease-in-out';

			// adds img to div
			ad.appendChild(img)
			console.log(img)
			// allows img to become colorful when hovered
			ad.addEventListener('mouseenter', () => {img.src = `../static/images/serviceIcons/${ad.id}Icon.png`; });
			ad.addEventListener('mouseleave', () => {img.src = `../static/images/serviceIcons/Grey${ad.id}Icon.png`; });
		});