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

function useOnOff(startVal=false) {
  const [isOn, setIsOn] = React.useState(startVal);
  const handlers = React.useMemo(() => ({
    turnOn: () => {
      setIsOn(true);
    },
    turnOff: () => {
      setIsOn(false);
    },
    toggle: () => setIsOn((index) => (index = !index)),
  }));

  return [isOn, handlers];
}

function ReviewFlashcardsPage() {
  const termDefs = [
    ["What is the role of a ribosome?", "How the heck would I know??"],
    ["What is a virus?", "A virus is like a zombie - controls host cell"],
  ];

  const [cardIndex, { next: setNextCardIndex, prev: setPrevCardIndex }] =
    useFlashcard(termDefs.length);

  const [term, definition] = termDefs[cardIndex];

  const [isSettingsTabOn, { turnOn: openSettings, turnOff: closeSettings }] =
    useOnOff();

  // Might change depending on user preference, tho this makes the most sense
  // as generally the term is what the user will test themselves on and the 
  // definition will contain the answer
  const defaultShouldDisplayTerm = true;  

  const [
    shouldDisplayTerm,
    { turnOn: displayTerm, turnOff: displayDef, toggle: toggleDefTerm },
  ] = useOnOff(defaultShouldDisplayTerm);

  const [startOnTerm, { toggle: toggleDefaultView }] = useOnOff(defaultShouldDisplayTerm);

  function changeCard(indexChanger) {
    if (startOnTerm){
      displayTerm();
    }
    else{
      displayDef();
    }
    indexChanger();
  }

  return (
    <>
      {isSettingsTabOn && (
        <OptionsModal className="settings-tab" onClose={closeSettings} />
      )}
      <div className="review-flashcards-page">
        <TopBar setName="My Set" settingsOnClick={openSettings} />
        <Flashcard
          term={term}
          definition={definition}
          shouldDisplayTerm={shouldDisplayTerm}
          onClick={toggleDefTerm}
        />
        {/*
      <InputBox
      */}
        <div className="arrow-container">
          <FlashcardArrow isFacingLeft={true} onClick={() => changeCard(setPrevCardIndex)} />
          <FlashcardArrow isFacingLeft={false} onClick={() => changeCard(setNextCardIndex)} />
        </div>
      </div>
    </>
  );
}

export default ReviewFlashcardsPage;
