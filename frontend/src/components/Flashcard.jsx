import { useState } from "react";
import "./Flashcard.css";

function Flashcard({ term, definition }) {
  const [shouldDisplayTerm, setShouldDisplayTerm] = useState();
  const textToDisplay = shouldDisplayTerm ? term : definition;
  return (
    <div
      className="flashcard"
      onClick={() => setShouldDisplayTerm((flag) => !flag)}
    >
      <h2>{shouldDisplayTerm ? "Term" : "Definition"}</h2>
      <h1>{textToDisplay}</h1>
    </div>
  );
}

export default Flashcard;
