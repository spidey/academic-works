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

function validatePhone(obj, field, size)
{
	if (obj.value.length != size)
	{
		alert(field + " tem de ter " + size + " dígitos!");
	}
	else
	{
		var invalidChars = obj.value.match(/[^0-9]/);
		if (invalidChars)
		{
			alert(field + " só pode ter dígitos, caracter " + invalidChars[0][0] + " inválido!");
		}
	}
}

function fillProductDropdown()
{
	var productTypes = [
		"Guidom",
		"Selim",
		"Pedal",
		"Bike16",
		"Bike26"
	];
	var products = [
		{ type: 0, name: "Alumínio CB", price: 35.00 },
		{ type: 0, name: "Alumínio Speed", price: 130.00 },
		{ type: 1, name: "RAD 7 Comfort", price: 49.00 },
		{ type: 1, name: "SERFAS DDMD-200", price: 199.00 },
		{ type: 2, name: "Inglês Alumínio", price: 27.00 },
		{ type: 3, name: "MTB VOLT 1.6 PT/AM", price: 490.00 },
		{ type: 3, name: "CALOI CECI BRANCA", price: 469.00 },
		{ type: 4, name: "POTY Br/Vm", price: 489.00 },
		{ type: 4, name: "CALOI Sport T19 V21", price: 880.00 }
	];
	var dropdown = document.getElementById("produtos");
	var i;
	for (i = 0; i < productTypes.length; ++i)
	{
		var optGroup = document.createElement("optgroup");
		optGroup.label = productTypes[i];
		var j;
		for (j = 0; j < products.length; ++j)
		{
			var product = products[j];
			if (product.type == i)
			{
				var option = document.createElement("option");
				option.value = product.price;
				option.innerHTML = product.name;
				optGroup.appendChild(option);
			}
		}
		dropdown.appendChild(optGroup);
	}
}

function buyProduct()
{
	var dropdown = document.getElementById("produtos");
	var selected = dropdown.selectedOptions[0];
	if (selected.value != "")
	{
		var type = selected.parentNode.label;
		var name = selected.innerHTML;
		var price = Number.parseFloat(selected.value);
		var notas = document.getElementById("notas");
		notas.value += type + " " + name + "\n";
		var valor = document.getElementById("valor");
		if (valor.value == "")
		{
			valor.value = "0";
		}
		var orderTotal = Number.parseFloat(valor.value);
		orderTotal += price;
		valor.value = orderTotal.toString();
	}
}

function clearForm()
{
	var valor = document.getElementById("valor");
	valor.value = "";
	var notas = document.getElementById("notas");
	notas.innerHTML = "";
}
