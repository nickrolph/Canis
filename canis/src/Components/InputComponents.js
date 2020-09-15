//This file is for storing the general code for the Input components. Individual
//input components can be found in the InputComponents folder
import React from "react";
import Zipcode from "./AllInputComponents/Zipcode";
import DateRange from "./AllInputComponents/DateRange.js";
import IncludeLocationless from "./AllInputComponents/IncludeLocationless.js";
import SearchRadius from "./AllInputComponents/SearchRadius.js";

function InputComponents() {
  return (
    <div>
      <DateRange />
      <Zipcode />
      <SearchRadius />
      <IncludeLocationless />
    </div>
  );
}

export default InputComponents;
