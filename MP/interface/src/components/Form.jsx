import { useState } from "react";
import urls from "../urls";
import Display from "./Display";
const styles = {
  form: {
    color: "white",
    fontWeight: "boldest",
    display: "flex",
    flexDirection: "column",
    gap: 10,
    maxWidth: "500px",
    margin: "0 auto",
    backgroundColor: "black",
    padding: "20px 30px",
  },
};
function Text(props) {
  return (
    <div className="field">
      <label htmlFor={props.identifier}>{props.label}</label>
      <input
        type="text"
        name={props.identifier}
        placeholder={props.placeholder}
        required
      />
    </div>
  );
}
function Select(props) {
  return (
    <div className="field">
      <label htmlFor={props.identifier}>{props.label}</label>
      <select name={props.identifier}>
        {props.options.map((value) => (
          <option key={value} value={value}>
            {value}
          </option>
        ))}
      </select>
    </div>
  );
}
export default function Form() {
  let [state, setState] = useState(true);
  let [isOpen, setIsOpen] = useState(false);
  let [form, setForm] = useState(false);
  const submitForm = (e) => {
    const formData = new FormData(e.target);
    var data = {};
    formData.forEach((value, key) => (data[key] = value));
    URL = urls.SUBMIT;
    console.log(JSON.stringify(data));
    fetch(URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((json) => {
        console.log("HERE:", json);
        setState(json);
        setIsOpen(true);
      });
  };
  URL = urls.FORM();
  fetch(URL, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((json) => {
      console.log("HERE:", json);
      if (form === false) setForm(json);
    });
  if (form) {
    return (
      <form
        method="POST"
        encType="multipart/form-data"
        style={styles.form}
        onSubmit={(e) => {
          e.preventDefault();
          submitForm(e);
        }}
      >
        {form.map((e) => {
          if (e.type === "text") {
            return (
              <Text identifier={e.identifier} label={e.label} key={e.label} />
            );
          } else if (e.type === "select") {
            return (
              <Select
                identifier={e.identifier}
                label={e.label}
                key={e.label}
                options={e.options}
              />
            );
          }
        })}
        <input type="submit" value="Submit" />
        <Display data={state} state={isOpen} setState={setIsOpen} />
      </form>
    );
  }
}