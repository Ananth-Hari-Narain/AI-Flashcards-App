import "./Flashcard.css";

function Flashcard({ term, definition, shouldDisplayTerm, onClick }) {
  const textToDisplay = shouldDisplayTerm ? term : definition;
  return (
    <div
      className="flashcard"
      onClick={onClick}
    >
      <h2>{shouldDisplayTerm ? "Term" : "Definition"}</h2>
      <h1>{textToDisplay}</h1>
    </div>
  );
}

export default Flashcard;
