import React from "react";
import Navigation from "./Navigation";
import logo from "../SiriusLogo.svg";

function Header() {
  return (
    <header className="border-b p-3 flex justify-between items-center">
      <img src={logo} alt="Sirius Temp Logo" />
      <span className="font-bold text-xl"> Sirius </span>
      <Navigation />
    </header>
  );
}

export default Header;
