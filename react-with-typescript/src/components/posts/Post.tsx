import React from 'react'
import PostInterface from "../../interface/posts/PostInterface";

interface PostPropInterrface {
    post: PostInterface;
  }

const Post = ({post:{id, title,body}}:PostPropInterrface) => {
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
  )
}

export default Post