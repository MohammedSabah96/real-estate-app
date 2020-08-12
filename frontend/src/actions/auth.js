import axios from "axios";
import setAlert from "./alert";
import {
  SIGNUP_SUCCESS,
  SIGNUP_FAILURE,
  LOGIN_SUCCESS,
  LOGIN_FAILURE,
  LOGOUT,
} from "./types";

export const login = (email, password) => async (dispatch) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  const body = JSON.stringify({ email, password });
  try {
    const res = await axios.post("localhost:8000/api/token", body, config);
    dispatch({ type: LOGIN_SUCCESS, payload: res.data });
    dispatch(setAlert("Authenticated Successfully", "success"));
  } catch (err) {
    dispatch({ type: LOGIN_FAILURE });
    dispatch(setAlert("Error Authenticating", "error"));
  }
};

export const signup = ({ email, name, password1, password2 }) => async (
  dispatch
) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  const body = JSON.stringify({ email, name, password1, password2 });
  try {
    const res = await axios.post(
      "localhost:8000/api/accounts/signup",
      body,
      config
    );
    dispatch({ type: SIGNUP_SUCCESS, payload: res.data });
    dispatch(login(email, password));
  } catch (err) {
    dispatch({ type: SIGNUP_FAILURE });
    dispatch(setAlert("Error Signup", "error"));
  }
};

export const logout = () => (dispatch) => {
  dispatch(setAlert("logout Successfully", "success"));
  dispatch({ type: LOGOUT });
};
