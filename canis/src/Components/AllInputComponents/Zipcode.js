import React, { Component } from "react";
import ReactDOM from "react-dom";
import TextField from "@material-ui/core/TextField";

class Zipcode extends Component {
  render() {
    return (
      <form noValidate autoComplete="off">
        <TextField id="outlined-basic" label="Zipcode" variant="outlined" />
      </form>
    );
  }
}

export default Zipcode;
