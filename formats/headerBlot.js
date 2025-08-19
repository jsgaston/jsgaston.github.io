const Block = Quill.import('blots/block');

class HeaderBlot extends Block {
  static blotName = 'header';
  static tagName = ['h1', 'h2'];
}

Quill.register(HeaderBlot);
