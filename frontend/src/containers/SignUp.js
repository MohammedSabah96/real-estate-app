import React, { useState } from "react";
import { connect } from "react-redux";
import { Link, Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import { Helmet } from "react-helmet";
import { signup } from "../actions/auth";
import setAlert from "../actions/alert";

const SignUp = ({ setAlert, signup, isAuthenticated }) => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password1: "",
    password2: "",
  });
  const { name, email, password1, password2 } = formData;

  const onChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = (e) => {
    e.preventDefault();

    if (password1 !== password2) {
      setAlert("Passwords do not match", "error");
    } else {
      signup({ name, email, password1, password2 });
    }
  };
  if (isAuthenticated) {
    return <Redirect to="/" />;
  }

  return (
    <div className="auth">
      <Helmet>
        <title>Realest Estate - Sign Up</title>
        <meta name="description" content="sign up page" />
      </Helmet>
      <h1 className="auth__title">Sign Up</h1>
      <p className="auth__lead">Create your Account</p>
      <form
        className="auth__form"
        onSubmit={(e) => onSubmit(e)}
        autoComplete="off"
      >
        <div className="auth__form__group">
          <input
            className="auth__form__input"
            type="text"
            placeholder="Enter Your Name"
            name="name"
            value={name}
            onChange={(e) => onChange(e)}
            required
          />
        </div>
        <div className="auth__form__group">
          <input
            className="auth__form__input"
            type="email"
            placeholder="Email address"
            name="email"
            value={email}
            onChange={(e) => onChange(e)}
            required
          />
        </div>
        <div className="auth__form__group">
          <input
            className="auth__form__input"
            type="password"
            placeholder="Password"
            name="password1"
            value={password1}
            onChange={(e) => onChange(e)}
            minLength="6"
            required
          />
        </div>
        <div className="auth__form__group">
          <input
            className="auth__form__input"
            type="password"
            placeholder="Confirm Password"
            name="password2"
            value={password2}
            onChange={(e) => onChange(e)}
            minLength="6"
            required
          />
        </div>
        <button className="auth__form__button">Register</button>
      </form>
      <p className="auth__authtext">
        Already have an account?{" "}
        <Link className="auth__authtext__link" to="/login">
          Sign In
        </Link>
      </p>
    </div>
  );
};

SignUp.propTypes = {
  signup: PropTypes.func.isRequired,
  setAlert: PropTypes.func.isRequired,
  isAuthenticated: PropTypes.bool,
};

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { setAlert, signup })(SignUp);
