import React from "react";
import { Link } from "react-router-dom";
// import PostForm from '../posts/Postform'
const Landing = () => {
  return (
    <>
      <div className="container">
        <div className="row">
          <div className="col">
            <h3 className="pt-4 text-center">Landing page</h3>
          </div>
        </div>
        <div className="row">
          <div className="col">
            <Link to="/post">Add Post</Link>
          </div>
          <div className="col">
            <Link to="/posts">All Post</Link>
          </div>
          <div className="col">
            <Link to="/reservation">Add Reservation</Link>
          </div>
          <div className="col">
            <Link to="/users">Users</Link>
          </div>
        </div>
      </div>
    </>
  );
};

export default Landing;
