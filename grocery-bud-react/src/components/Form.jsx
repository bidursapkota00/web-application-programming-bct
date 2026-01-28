import { useState, useEffect } from "react";
import { toast } from "react-toastify";
import "./Form.css";

const Form = ({
  addItem,
  editItemId,
  updateItemName,
  itemToEdit,
  inputRef,
}) => {
  const [newItemName, setNewItemName] = useState("");

  useEffect(() => {
    if (itemToEdit) {
      setNewItemName(itemToEdit.name);
    } else {
      setNewItemName("");
    }
  }, [itemToEdit]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItemName) {
      toast.error("please provide value");
      return;
    }
    if (editItemId) {
      updateItemName(newItemName);
    } else {
      addItem(newItemName);
    }
    setNewItemName("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>grocery bud</h2>
      <div className="form-control">
        <input
          type="text"
          className="form-input"
          value={newItemName}
          ref={inputRef}
          placeholder="e.g. eggs"
          onChange={(event) => setNewItemName(event.target.value)}
        />
        <button type="submit" className="btn">
          {editItemId ? "edit item" : "add item"}
        </button>
      </div>
    </form>
  );
};

export default Form;
