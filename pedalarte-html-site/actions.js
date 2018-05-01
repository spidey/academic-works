function openWindow(url, width, height)
{
	var properties = "width=" + width + ",height=" + height;
	window.open(url, url, properties);
}

function closeWindow()
{
	window.close();
}
