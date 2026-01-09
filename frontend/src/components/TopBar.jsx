import "./TopBar.css";
import settingsIcon from "../assets/images/settings.png"

const TopBar = ({ setName, settingsOnClick, exitOnClick }) => {
  return (
    <div className="top-bar">
      <button onClick={settingsOnClick}>
        <img src={settingsIcon}/>
      </button>
      <h1>{setName}</h1>
      <button onClick={exitOnClick}>X</button>
    </div>
  );
};

export default TopBar;
