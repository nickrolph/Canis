import React from "react";
import Navigation from "./Navigation";
import logo from "../tempGoldenLogo.svg";

function Header() {
  return (
    <header className="border-b p-3 flex justify-between items-center">
      <img src={logo} alt="Golden Retriever Temp Logo" />
      <span className="font-bold text-xl"> Golden Retriever </span>
      <Navigation />
    </header>
  );
}

export default Header;
