import React, { useState, useEffect } from "react";
import api from "../../utils/api";
import { toast } from "react-toastify";
import setAuthToken from "../../utils/setAuthToken";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();
  const [values, setValues] = useState({
    email: "",
    password: "",
  });

  const handleInputChange = (e: any) => {
    const { name, value } = e.target;
    setValues({ ...values, [name]: value });
  };
  useEffect(() => {
    setAuthToken(null);
  }, []);

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    try {
      const res = await api.post("/account/login/", values);
      console.log(res.data);
      // localStorage.setItem("token", res.data.result.token.access);
      setAuthToken(res.data.result.token.access);
      toast.info('login success')
      // return <Navigate to="/posts" />;
      navigate('/posts')

      // return redirect('/');
      // window.ref = '/'
    } catch (error: any) {
      // console.error(error.message);
      if (error.response.data.result) {
        const { non_field_errors } = error.response.data.result;
        console.log(non_field_errors);
        non_field_errors.forEach((m: string) => {
          toast.error(m);
        });
      } else {
        toast.error(error.message);
      }
    }
  };

  return (
    <div className="container">
      <div className="row">
        <h4 className="text-center pb-2">Login Form</h4>
      </div>
      <div className="row justify-content-center">
        <form onSubmit={handleSubmit} className="col-6">
          <div className="form-group">
            <label htmlFor="email" className="form-label">
              Email
            </label>
            <input
              type="email"
              id="email"
              name="email"
              value={values.email}
              onChange={handleInputChange}
              className="form-control"
            />
          </div>

          <div className="form-group">
            <label htmlFor="password" className="form-label">
              Password
            </label>
            <input
              id="password"
              name="password"
              type="password"
              value={values.password}
              onChange={handleInputChange}
              className="form-control"
            />
          </div>

          <div className="form-group text-center pt-3">
            <input
              className="btn btn-outline-dark"
              type="submit"
              value="Login"
            />
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
