import React from "react";
import UserInterface from "../../interface/posts/UserInterface";

const UserItem = ({ user }: any) => {
  return (
    <div className="col m-4">
      <div className="card text-center">
        <div className="card-header">{user.name}</div>
        <div className="card-body">
          <h5 className="card-title">{user.email}</h5>
          <p className="card-text">
            {user.username}
          </p>
          <p className="card-text">{user.phone}</p>
          <p className="card-text">{user.website}</p>
          <p className="card-text"></p>
            
            
          <a href="#!" className="btn btn-primary">
            Go somewhere
          </a>
        </div>
        <div className="card-footer text-muted">2 days ago</div>
      </div>
    </div>
  );
};

export default UserItem;
