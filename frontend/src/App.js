import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Layout from "./hocs/Layout";
import Home from "./containers/Home";
import About from "./containers/About";
import Contact from "./containers/Contact";
import Listings from "./containers/Listings";
import ListingDetail from "./containers/ListingDetail";
import SignUp from "./containers/SignUp";
import SignIn from "./containers/SignIn";
import NotFound from "./components/NotFound";
import PrivateRoute from "./components/privateRoute";

import { Provider } from "react-redux";
import store from "./store";

import "./sass/main.scss";

const App = () => (
  <Provider store={store}>
    <Router>
      <Layout>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/about" component={About} />
          <Route path="/contact" component={Contact} />
          <PrivateRoute path="/listings/:id" component={ListingDetail} />
          <Route path="/listings" component={Listings} />
          <Route path="/login" component={SignIn} />
          <Route path="/signup" component={SignUp} />
          <Route component={NotFound} />
        </Switch>
      </Layout>
    </Router>
  </Provider>
);

export default App;
