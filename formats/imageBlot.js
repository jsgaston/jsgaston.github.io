const BlockEmbed = Quill.import('blots/block/embed');

class ImageBlot extends BlockEmbed {
  static blotName = 'image';
  static tagName = 'img';

  static create(value) {
    let node = super.create();
    node.setAttribute('alt', value.alt);
    node.setAttribute('src', value.url);
    return node;
  }
  
  static value(node) {
    return {
      alt: node.getAttribute('alt'),
      url: node.getAttribute('src')
    };
  }
}

Quill.register(ImageBlot);
