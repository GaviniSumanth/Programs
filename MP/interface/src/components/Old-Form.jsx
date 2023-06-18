import { Component } from "react";
import Display from "./Display";
const input_data = {
  steam: { A: { required: "yes", type: "text" } },
  "human-resources": { B: { required: "yes", type: "text" } },
  "student-adaptability": {
    C: { required: "yes", type: "text" },
    K: { required: "yes", type: "text" },
  },
};
function GenerateForm(props) {
  let components = [];
  let keys = Object.keys(input_data[props.form]);
  for (let i = 0; i < keys.length; i++) {
    components.push(
      <label key={"label-" + (i + 1)} className="label" htmlFor={keys[i]}>
        {keys[i]}
      </label>
    );
    components.push(
      <input
        key={"input-" + (i + 1)}
        className={keys[i].type}
        name={keys[i]}
        type={keys[i].type}
      />
    );
  }
  components.push(
    <input key="submit" id="Submit" className="button" type="submit" />
  );
  return components;
}
class Form extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <form className="form">
        <GenerateForm form={this.props.form} />
      </form>
    );
  }
}
export default Form;
