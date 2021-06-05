function onLoad(){
	var devicesForm = document.getElementById('editSettings');
	var canBtn = document.getElementById('cancel');
	var pipEditBtn = document.getElementById('popEdit');
	var subBtn = document.getElementById('submit');

	pipEditBtn.addEventListener('click', function (e) {
		console.log(devicesForm)
		devicesForm.showModal();
	})

	canBtn.addEventListener('click', function (e) {
		devicesForm.close();
	});

	subBtn.addEventListener('click', function (e) {
		devicesForm.close();
	});

}

document.addEventListener('DOMContentLoaded', function () {
	onLoad();
});






//function onLoad(){
//	var devicesForm = document.getElementById('addDevice');
//	var canBtn = document.getElementById('cancel');
//	var addDeviceBtn = document.getElementById('addDeviceBtn');
//	var subBtn = document.getElementById('submit');

//	addDeviceBtn.addEventListener('click', function (e) {
//		console.log(devicesForm)
//		devicesForm.showModal();
//	})

//	canBtn.addEventListener('click', function (e) {
//		devicesForm.close();
//	});

//	subBtn.addEventListener('click', function (e) {
//		devicesForm.close();
//	});

//}

//document.addEventListener('DOMContentLoaded', function(){
//	onLoad();
//});

//let modalBtns = [...document.querySelectorAll("button.edit_button")];
//modalBtns.forEach(function(btn) {
//	console.log
//  btn.onclick = function() {
//	let popup = btn.getAttribute('popup');
//	document.getElementById(popup)
//	  .style.display = "block";
//  }
//});
//let closeBtns = [...document.querySelectorAll(".close")];
//closeBtns.forEach(function(btn) {
//  btn.onclick = function() {
//	let popup_form = btn.closest('.popup_form');
//	popup_form.style.display = "none";
//  }
//});
//window.onclick = function(event) {
//  if(event.target.className === "popup_form") {
//	event.target.style.display = "none";
//  }
//}

//document.addEventListener('DOMContentLoaded', function () {
//var slider = document.getElementById("myRange");
//var output = document.getElementById("sliderval");
//	//slider.oninput = function() {
//	//	const response = fetch('/'+slider.name+slider.value, {
//	//	method: 'POST',
//	//	body: output,
//	//	});
//	//}
//});

//function post(id){
//	var url = id;
//	console.log(url);
//	fetch(url).then(function(response) {
//		response.text().then(function(text) {
//			console.log(text);
//		});
//	});
//}
