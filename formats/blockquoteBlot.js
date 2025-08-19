const Block = Quill.import('blots/block');

class BlockquoteBlot extends Block {
  static blotName = 'blockquote';
  static tagName = 'blockquote';
}

Quill.register(BlockquoteBlot);
