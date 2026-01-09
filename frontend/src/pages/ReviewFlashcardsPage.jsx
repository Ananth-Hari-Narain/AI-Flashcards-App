import Flashcard from "../components/Flashcard.jsx";
import FlashcardArrow from "../components/FlashcardArrow.jsx";
import TopBar from "../components/TopBar.jsx";
import OptionsModal from "../components/OptionsModal.jsx";
import "./ReviewFlashcardsPage.css";
import React from "react";

function useFlashcard(numCards) {
  const [index, setIndex] = React.useState(0);

  const handlers = React.useMemo(() => ({
    next: () => {
      setIndex((index) => (index < numCards - 1 ? index + 1 : index));
    },
    prev: () => {
      setIndex((index) => (index == 0 ? 0 : index - 1));
    },
  }));

  return [index, handlers];
}

function useOnOff() {
  const [isOn, setIsOn] = React.useState(false);
  const handlers = React.useMemo(() => ({
    turnOn: () => {
      setIsOn((index) => (index = true));
    },
    turnOff: () => {
      setIsOn((index) => (index = false));
    },
  }));

  return [isOn, handlers];
}

function ReviewFlashcardsPage() {
  const termDefs = [
    ["What is the role of a ribosome?", "How the heck would I know??"],
    ["What is a virus?", "A virus is like a zombie - controls host cell"],
  ];

  const [cardIndex, { next, prev }] = useFlashcard(termDefs.length);
  const [term, definition] = termDefs[cardIndex];

  const [isSettingsTabOn, { turnOn, turnOff }] = useOnOff();

  return (
    <>
      {isSettingsTabOn && (
        <OptionsModal className="settings-tab" onClose={turnOff} />
      )}
      <div className="review-flashcards-page">
        <TopBar setName="My Set" settingsOnClick={turnOn} />
        <Flashcard term={term} definition={definition} />
        {/*
      <InputBox
      */}
        <div className="arrow-container">
          <FlashcardArrow isFacingLeft={true} onClick={prev} />
          <FlashcardArrow isFacingLeft={false} onClick={next} />
        </div>
      </div>
    </>
  );
}

export default ReviewFlashcardsPage;
