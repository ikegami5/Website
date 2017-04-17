var CANVAS_WIDTH = 800;
var CANVAS_HEIGHT = 600;

window.addEventListener('load', init);

var canvas;
var renderingContext;

function init() {
	canvas = document.getElementById('mainCanvas');
	renderingContext = canvas.getContext('2d');
	canvas.width = CANVAS_WIDTH;
	canvas.height = CANVAS_HEIGHT;
	requestAnimationFrame(update);
}

function update() {
	requestAnimationFrame(update);
	render();
}

function render() {
	renderingContext.clearRect(0, 0, canvas.width, canvas.height);
}
