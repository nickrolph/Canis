import React from "react";
import TextField from "@material-ui/core/TextField";

function DateRange() {
  return (
    <div>
      <form className="" noValidate>
        <TextField
          id="date"
          label="Start Date"
          type="date"
          defaultValue="2017-05-24"
          className="p-3"
          InputLabelProps={{
            shrink: true,
          }}
        />
      </form>

      <form className="" noValidate>
        <TextField
          id="date"
          label="End Date"
          type="date"
          defaultValue="2017-05-24"
          className="p-3"
          InputLabelProps={{
            shrink: true,
          }}
        />
      </form>
    </div>
  );
}

export default DateRange;
