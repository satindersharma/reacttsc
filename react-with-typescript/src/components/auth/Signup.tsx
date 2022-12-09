import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import api from "../../utils/api";

const Signup = () => {
  const navigate = useNavigate()
  const [values, setValues] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    phone_number: "",
    country: "",
    city: "",
  });

  const handleInputChange = (e: any) => {
   const  {name,value} = e.target
    setValues({...values, [name]:value})
  };

  const handleSubmit = (e:any)=>{
    e.preventDefault()
    console.log(values)

    api.post('/account/signup/',values).then((res)=>{
      console.log(res.data)
      toast.success('signup successful. Login')
      navigate('/login')

    }).catch((err)=>{
      console.log(err)
    }
    )

    

  }
  return (
    <div className="container">
      <div className="row">
        <h4 className="text-center pb-2">Signup Form</h4>
      </div>
      <div className="row justify-content-center">
        <form onSubmit={handleSubmit} className="col-6">
          <div className="form-group">
            <label className="form-label">First Name</label>
            <input
              type="text"
              id="first_name"
              name="first_name"
              value={values.first_name}
              onChange={handleInputChange}
              className="form-control"
            />
          </div>
          <div className="form-group">
            <label htmlFor="last_name" className="form-label">
              Last Name
            </label>
            <input type="text" 
            id="last_name"
            name="last_name"
            value={values.last_name}
            onChange={handleInputChange}
            className="form-control" />
          </div>
          <div className="form-group">
            <label htmlFor="email" 
            
            className="form-label">
              Email
            </label>
            <input type="email"
            id="email"
            name="email"
            value={values.email}
            onChange={handleInputChange}
            
            className="form-control" />

          </div>
          <div className="form-group">
            <label htmlFor="password" className="form-label">
              Password
            </label>
            <input type="password"
            id="password"
            name="password"
            value={values.password}
            onChange={handleInputChange}
            
             className="form-control" />
          </div>
          <div className="form-group">
            <label htmlFor="phone_number" className="form-label">
              Phone Number
            </label>
            <input type="text" 
            id="phone_number"
            name="phone_number"
            value={values.phone_number}
            onChange={handleInputChange}
            
            className="form-control" />
          </div>
          <div className="form-group">
            <label htmlFor="country" className="form-label">
              Country
            </label>
            <input type="text"
            id="country"
            name="country"
            value={values.country}
            onChange={handleInputChange}
            
             className="form-control" />
          </div>
          <div className="form-group">
            <label htmlFor="city" className="form-label">
              City
            </label>
            <input type="text" 
            id="city"
            name="city"
            value={values.city}
            onChange={handleInputChange}
            
            className="form-control" />
          </div>
          <div className="form-group pt-2 text-center">
            <input type="submit" value="Signup" className="btn btn-outline-dark" />
          </div>


        </form>
      </div>
    </div>
  );
};

export default Signup;
