function openWindow(url, width, height)
{
	var properties = "width=" + width + ",height=" + height;
	window.open(url, url, properties);
}

function closeWindow()
{
	window.close();
}

function showBike(index)
{
	var bikes = [
		["MTB VOLT 1.6 PT/AM", "imagens/Bike_MTB_ARO16.jpg", "R$ 490,00"],
		["CALOI CECI BRANCA", "imagens/Bike_Caloi_ARO16.jpg", "R$ 469,00"],
		["POTY Branca/Vermelho", "imagens/Bike_Poty_ARO26.jpg", "R$ 489,00"],
		["CALOI Sport T19 V21", "imagens/Bike_Caloi_ARO26.jpg", "R$ 880,00"]
	];

	document.getElementById("bikeName").innerHTML = bikes[index][0];
	document.getElementById("bikeImage").src = bikes[index][1];
	document.getElementById("bikePrice").innerHTML = bikes[index][2];
}
