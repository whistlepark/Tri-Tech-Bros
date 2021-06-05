function onLoad(){
	var devicesForm = document.getElementById('addDevice');
	var canBtn = document.getElementById('cancel');
	var addDeviceBtn = document.getElementById('addDeviceBtn');
	var subBtn = document.getElementById('submit');

	addDeviceBtn.addEventListener('click', function (e) {
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

document.addEventListener('DOMContentLoaded', function(){
	onLoad();
});
