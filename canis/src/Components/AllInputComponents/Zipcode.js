import React from "react";
import TextField from "@material-ui/core/TextField";

function Zipcode() {
  return (
    <form noValidate autoComplete="off">
      <TextField id="outlined-basic" label="Zipcode" variant="outlined" />
    </form>
  );
}

export default Zipcode;
