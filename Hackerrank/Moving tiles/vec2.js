class Vec2 {
    constructor(x, y=x) {
        this.x = x;
        this.y = y;
    }

    add(v) {
        return new Vec2(this.x + v.x, this.y + v.y);
    }

    subtract(v) {
        return new Vec2(this.x - v.x, this.y - v.y);
    }

    scale(a) {
        return new Vec2(a * this.x, a * this.y);
    }

    length() {
        return Math.sqrt(this.x**2 + this.y**2);
    }

    dist(v) {
        return this.subtract(v).length();
    }

    normalize() {
        let length = this.length();
        return new Vec2(this.x / length, this.y / length);
    }

    mid(v) {
        return new Vec2(this.x + v.x, this.y + v.y).scale(0.5);
    }

    static rand(maxX, maxY) {
        return new Vec2(
            Math.floor(Math.random() * (maxX + 1)),
            Math.floor(Math.random() * (maxY + 1))
        );
    }
}

class Planet {
    constructor(p, m = 1) {
        this.p = p; // position
        this.m = m; // mass

        this.acceleration = new Vec2(1, 0);
        this.velocity = new Vec2(0); //new Vec2(2*Math.cos(p.x), 2*Math.sin(p.y));

        this.fixed = false;
        this.deleted = false;
    }

    radius() {
        // mass is the surface area of the circle.
        return Math.sqrt(this.m / (4*Math.PI));
    }

    static rand(r) {
        return new Planet( 
            Vec2.rand(window.innerWidth, window.innerHeight),
            Math.random() * r
        )
    }
}