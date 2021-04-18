import React from "react";
import Header from "./Components/Header";
import List from "./Components/List";
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
            <h1 className="font-bold font-serif text-2xl">
              Sirius Pet Retriever finds tweets referencing lost and found pets.{" "}
            </h1>
            <h1 className="font-bold text-2xl">
              Specify your post criteria and search below:{" "}
            </h1>
            <InputComponents />
          </Route>
          <Route path="/about">
            <h1 className="font-bold text-2xl">
              Sirius Pet Retriever was founded as a simple tool that makes it
              easier to connect with your local comunity to help find your lost
              pet. Idealy every pet would have a collar, micro chip, or tracking
              device. But in the event where those methods fail, Sirius is here
              as a last defence to provide any help we can.{" "}
            </h1>
          </Route>
        </Switch>
        <List />
        <Footer />
      </Router>
    </div>
  );
}

export default App;
