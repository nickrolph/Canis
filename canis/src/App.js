import React from "react";
import Header from "./Components/Header";
import Footer from "./Components/Footer";
import InputComponents from "./Components/InputComponents";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

function App() {
  return (
    <div>
      <Router>
        <Header />
        <Switch>
          <Route exact path="/">
            <h1 className="font-bold text-2xl">
              Instructions: This web-app is designed to help sort through the
              social media postings of lost and found pets. To narrow down your
              search for social media postings: 1. select a time period for
              posts you would like to look at 2. select a region via zipCode 3.
              select a radius from that ZipCode. It is important to note that
              some social media posts do not contain location information. These
              posts are included by default, and surrounded by a different color
              () and are excludable by checking the box below.{" "}
            </h1>
            <InputComponents />
          </Route>
          <Route path="/about">
            <h1 className="font-bold text-2xl">
              Golden Retriever was founded as a simple tool that makes it easier
              to connect with your local comunity to help find your lost pet.
              Idealy every pet would have a collar, micro chip, or tracking
              device. But in the event where those methods fail. Golden
              Retriever is here as a last defence to provide any help we can.{" "}
            </h1>
          </Route>
        </Switch>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
