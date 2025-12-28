import Flashcard from "../components/Flashcard.jsx";
import FlashcardArrow from "../components/FlashcardArrow.jsx";
import "./ReviewFlashcardsPage.css";
import React from "react";

function useFlashcard(numCards) {
  const [index, setIndex] = React.useState(0);

  const handlers = React.useMemo(() => ({
    next: () => {
      setIndex(index => index < numCards - 1 ? index + 1 : index);
    },
    prev: () => {
      setIndex(index => index == 0 ? 0 : index - 1);
    },
  }));

  return [index, handlers];
}

function ReviewFlashcardsPage() {
  const termDefs = [
    ["What is the role of a ribosome?", "How the heck would I know??"],
    ["What is a virus?", "A virus is like a zombie - controls host cell"],
  ];

  const [cardIndex, { next, prev }] = useFlashcard(termDefs.length);
  const [term, definition] = termDefs[cardIndex]
  return (
    <>
      <Flashcard
        term={term}
        definition={definition}
      />
      {/*
      <InputBox
      */}
      <div className="arrow-container">
        <FlashcardArrow isFacingLeft={true} onClick={prev} />
        <FlashcardArrow isFacingLeft={false} onClick={next} />
      </div>
    </>
  );
}

export default ReviewFlashcardsPage;
