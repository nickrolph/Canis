import React from "react";
import FormControl from "@material-ui/core/FormControl";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import Select from "@material-ui/core/Select";

function SearchRadius() {
  const [radius, setRadius] = React.useState("");

  const handleChange = (event) => {
    setRadius(event.target.value);
  };

  return (
    <div>
      <FormControl className="">
        <InputLabel id="Simple Distance MenuItem">Radius</InputLabel>
        <Select
          labelId="Simple Distance MenuItem"
          id="radius-distance-select"
          value={radius}
          onChange={handleChange}
        >
          <MenuItem value={10}>Ten</MenuItem>
          <MenuItem value={20}>Twenty</MenuItem>
          <MenuItem value={30}>Thirty</MenuItem>
        </Select>
      </FormControl>
    </div>
  );
}

export default SearchRadius;
