const Inline = Quill.import('blots/inline');

class LinkBlot extends Inline {
  static blotName = 'link';
  static tagName = 'a';

  static create(url) {
    let node = super.create();
    // Sanitize url if desired
    node.setAttribute('href', url);
    // Okay to set other non-format related attributes
    node.setAttribute('target', '_blank');
    return node;
  }
  
  static formats(node) {
    // We will only be called with a node already
    // determined to be a Link blot, so we do
    // not need to check ourselves
    return node.getAttribute('href');
  }
}

Quill.register(LinkBlot);
