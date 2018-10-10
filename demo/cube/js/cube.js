var cube = {
	all: [],
	create: function(w, x, y, z, colors) {
		var cube = document.createElement("div");
		// 旋转角度
		cube.rx = 0;
		cube.ry = 0;
		cube.rz = 0;
		// 长宽高
		cube.w = w;
		// 位置
		cube.x = x;
		cube.y = y;
		cube.z = z;
		this.addStyle(cube, {
			webkitTransformStyle: "preserve-3d",
			width: cube.w + "px",
			height: cube.w + "px",
			position: "fixed",
			webkitTransformOriginX: cube.w / 2 + cube.x + "px",
			webkitTransformOriginY: cube.w / 2 + cube.y + "px",
			webkitTransformOriginZ: cube.w / 2 + cube.z + "px",
			webkitTransform: "rotateX(" + cube.rx + "deg) rotateY(" + cube.ry + "deg) rotateZ(" + cube.rz + "deg) translateX(" + cube.x + "px) translateY(" + cube.y + "px) translateZ(" + cube.z + "px)"
		});
		var arr = [0, 90, 180, 270, 90, 270];
		for(var i = 0; i < 6; i++) {
			var item = document.createElement("div");
			this.addStyle(item, {
				width: cube.w + "px",
				height: cube.w + "px",
				position: "absolute",
				top: "0px",
				left: "0px",
				backgroundColor: colors[i]
			});

			if(i < 4) {
				this.addStyle(item, {
					webkitTransform: "rotateY(" + arr[i] + "deg) translateZ(" + cube.w / 2 + "px)"
				});
			} else {
				this.addStyle(item, {
					webkitTransform: "rotateX(" + arr[i] + "deg) translateZ(" + cube.w / 2 + "px)"
				});
			}
			cube.appendChild(item);
		}
		this.all.push(cube);
		return cube;
	},
	addStyle: function(obj, styles) {
		for(var s in styles) {
			obj.style[s] = styles[s];
		}
	},
	rotateX: function(obj, r) {
		obj.rx = r;
		this.addStyle(obj, {
			webkitTransformOriginX: obj.w / 2 + obj.x + "px",
			webkitTransformOriginY: obj.w / 2 + obj.y + "px",
			webkitTransformOriginZ: 0 + obj.z + "px",
			webkitTransform: "rotateX(" + obj.rx + "deg) rotateY(" + obj.ry + "deg) rotateZ(" + obj.rz + "deg) translateX(" + obj.x + "px) translateY(" + obj.y + "px) translateZ(" + obj.z + "px)"
		});
	},
	rotateY: function(obj, r) {
		obj.ry = r;
		this.addStyle(obj, {
			webkitTransformOriginX: obj.w / 2 + obj.x + "px",
			webkitTransformOriginY: obj.w / 2 + obj.y + "px",
			webkitTransformOriginZ: 0 + obj.z + "px",
			webkitTransform: "rotateX(" + obj.rx + "deg) rotateY(" + obj.ry + "deg) rotateZ(" + obj.rz + "deg) translateX(" + obj.x + "px) translateY(" + obj.y + "px) translateZ(" + obj.z + "px)"
		});
	},
	rotateZ: function(obj, r) {
		obj.rz = r;
		this.addStyle(obj, {
			webkitTransformOriginX: obj.w / 2 + obj.x + "px",
			webkitTransformOriginY: obj.w / 2 + obj.y + "px",
			webkitTransformOriginZ: 0 + obj.z + "px",
			webkitTransform: "rotateX(" + obj.rx + "deg) rotateY(" + obj.ry + "deg) rotateZ(" + obj.rz + "deg) translateX(" + obj.x + "px) translateY(" + obj.y + "px) translateZ(" + obj.z + "px)"
		});
	}
	
	,move: function(obj, x,y,z) {
		obj.x = x;
		obj.y = y;
		obj.z = z;
		this.addStyle(obj, {
			webkitTransformOriginX: obj.w / 2 + obj.x + "px",
			webkitTransformOriginY: obj.w / 2 + obj.y + "px",
			webkitTransformOriginZ: 0 + obj.z + "px",
			webkitTransform: "rotateX(" + obj.rx + "deg) rotateY(" + obj.ry + "deg) rotateZ(" + obj.rz + "deg) translateX(" + obj.x + "px) translateY(" + obj.y + "px) translateZ(" + obj.z + "px)"
		});
	}

}