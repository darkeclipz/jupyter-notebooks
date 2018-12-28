class Draw {

    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext("2d");
        console.log('Canvas initialized:', canvasId);
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        this.strokeMode = false;
    }

    fill() {
        this.strokeMode = false;
    }

    stroke() {
        this.strokeMode = true;
    }

    clear() {
        let fc = this.ctx.fillStyle;
        this.color("black");
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        this.color(fc);
    }

    point(p) {
        this.rect(p, new Vec2(2));
    }

    rect(p, d) {
        if (this.strokeMode) this.ctx.strokeRect(p.x, innerHeight-p.y, d.x, d.y);
        else this.ctx.fillRect(p.x, innerHeight-p.y, d.x, d.y);
        console.log(p, d);
    }

    color(c) {
        this.ctx.fillStyle = c;
        this.ctx.strokeStyle = c;
    }

    text(p, t) {
        if(this.strokeMode) this.ctx.strokeText(t, p.x, innerHeight-p.y);
        else this.ctx.fillText(t, p.x, innerHeight-p.y);
    }

    font(family, size) {
        this.ctx.font = size + 'px ' + family;
    }

    line(p1, p2) {
        this.ctx.beginPath();
        this.ctx.moveTo(p1.x, innerHeight-p1.y);
        this.ctx.lineTo(p2.x, innerHeight-p2.y);
        this.ctx.stroke();
    }

    width(w) {
        this.ctx.lineWidth = w;
    }

}