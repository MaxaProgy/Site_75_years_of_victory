anime({
    targets: '.anime',
    d: [
        { value: (el) => el.getAttribute('data-morph-to'), duration: (el, i) => 2000},
        { value: (el) => el.getAttribute('d'), duration: (el, i,l) => 2000 }
    ],
    loop: true,
    easing: 'linear',
    update: () => {
        const el = document.getElementById('defs');
        el.style.display = 'none';
        el.offsetWidth;
        el.style.display = 'block';
    }
});

class Defilee {
    constructor (element) {
        if (!element) {
            return
        }
        this.element = element;
        this._name = "defilee";
        this._itemSelector = "." + this._itemClass
    }
    init () {
        this.addLoop();
    }
    addLoop () {
        const parent = this.element;
        Array.prototype.slice.call(this.element.children).reverse().forEach ( (el) => {
            const clone = el.cloneNode(true);
            clone.classList.add('clone');
            parent.insertBefore(clone, parent.firstChild );
        })
    }
}

const defilee = new Defilee(document.getElementById('defilee'));
defilee.init();