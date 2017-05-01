var CANVAS_WIDTH = 800;
var CANVAS_HEIGHT = 600;

window.addEventListener('load', init);

var canvas;
var renderingContext;

var Asset = {
	assets: [
		{type: 'image', name: 'background', src: '/game/assets/background.png'}
		{type: 'image', name: 'coal', src: '/game/assets/coal.png'}
		{type: 'image', name: 'dirt', src: '/game/assets/dirt.png'}
		{type: 'image', name: 'ironOre', src: '/game/assets/ironOre.png'}
		{type: 'image', name: 'wood', src: '/game/assets/wood.png'}
		{type: 'image', name: 'bedrock', src: '/game/assets/bedrock.png'}
		{type: 'image', name: 'diamond', src: '/game/assets/diamond.png'}
		{type: 'image', name: 'goldOre', src: '/game/assets/goldOre.png'}
		{type: 'image', name: 'stone', src: '/game/assets/stone.png'}
		{type: 'image', name: 'mainChar', src: '/game/assets/mainChar.png'}
	],
	images: {},

	loadAssets: function(onComplete) {
		var total = Asset.assets.length;
		var loadCount = 0;
		var onLoad = function() {
			loadCount++;
			if (loadCount >= total) {
				onComplete();
			}
		};
		this.assets.forEach(function(asset) {
			if (asset.type === 'image') {
				Asset._loadImage(asset, onLoad);
			}
		});
	},

	_loadImage: function(asset, onLoad) {
		var image = new Image();
		image.src = asset.src;
		image.onload = onLoad;
		this.images[asset.name] = image;
	}

};

function init() {
	canvas = document.getElementById('mainCanvas');
	renderingContext = canvas.getContext('2d');
	canvas.width = CANVAS_WIDTH;
	canvas.height = CANVAS_HEIGHT;
	Asset.loadAssets(function() {
		requestAnimationFrame(update);
	});
}

function update() {
	requestAnimationFrame(update);
	render();
}

function render() {
	renderingContext.clearRect(0, 0, canvas.width, canvas.height);
	renderingContext.drawImage(Asset.images['background'], 0, 0, 800, 600);
}
