import React from "react";

interface PostItemInterface {
  post: {
    id: number;
    title: string;
    body: string;
    userId?: number;
  };
}

const PostItem = ({ post: { id, title, body } }: PostItemInterface) => {
  return (
    <div className="col-6 mb-4">
      <div className="card text-center">
        <div className="card-header">{title}</div>
        <div className="card-body">
          <p className="card-text">{body}</p>
          <a href="#!" className="btn btn-primary">
            {id}
          </a>
        </div>
      </div>

      <h2>{title}</h2>
      <p>{body}</p>
    </div>
  );
};

export default PostItem;
