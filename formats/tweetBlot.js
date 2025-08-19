const BlockEmbed = Quill.import('blots/block/embed');

class TweetBlot extends BlockEmbed {
  static blotName = 'tweet';
  static tagName = 'div';
  static className = 'tweet';

  static create(id) {
    let node = super.create();
    node.dataset.id = id;
    twttr.widgets.createTweet(id, node);
    return node;
  }
  
  static value(domNode) {
    return domNode.dataset.id;
  }
}

Quill.register(TweetBlot);
