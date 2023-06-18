import { useForm } from "react-hook-form";
import { useState } from "react";
import Display from "./Display";
const styles = {
  form: {
    display: "flex",
    flexDirection: "column",
    gap: 5,
    maxWidth: "500px",
    margin: "0 auto",
  },
};
export default function Form() {
  let [state, setState] = useState(true);
  let [isOpen, setIsOpen] = useState(true);
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();
  const onSubmit = (data) => {
    URL = "http://127.0.0.1:5000/steam/";
    console.log(data);
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

  return (
    <form onSubmit={handleSubmit(onSubmit)} style={styles.form}>
      <label htmlFor="firstName">First name</label>
      <input
        defaultValue="test"
        {...register("firstName", { required: true })}
      />
      {errors.firstName && <span>This field is required</span>}
      <select {...register("gender")}>
        <option value="male">Male</option>
        <option value="female">Female</option>
        <option value="other">Other</option>
      </select>
      <input type="submit" />
      {state !== true && (
        <Display data={state} state={isOpen} setState={setIsOpen} />
      )}
    </form>
  );
}
