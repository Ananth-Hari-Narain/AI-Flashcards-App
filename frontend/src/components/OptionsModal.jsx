import "./OptionsModal.css";
import { useEffect } from "react";

function OptionsModal({ onClose }) {
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") {
        onClose();
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [onClose]);

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h1>Settings</h1>
        <p>Change this</p>  
        <p>Change that</p>
      </div>
    </div>
  );
}

export default OptionsModal;
