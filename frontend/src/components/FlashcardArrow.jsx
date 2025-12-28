import './FlashcardArrow.css'

function FlashcardArrow({isFacingLeft, onClick}) {
  return <button onClick={onClick}>{isFacingLeft ? "<" : ">"}</button>
}

export default FlashcardArrow