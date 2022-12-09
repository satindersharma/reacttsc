import React, { Fragment, useEffect, useState } from "react";
import PostItem from "./PostItem";
import PostInterface from "../../interface/posts/PostInterface";
import api from "../../utils/api";
import { toast } from "react-toastify";

const Posts = () => {

  const [posts, setPosts] = useState<PostInterface[]>([]);
  // const fetchData = () => {
  //   // fetch("https://jsonplaceholder.typicode.com/posts")
  //   //   .then((response) => response.json())
  //   //   .then((data) => setPosts(data));
  //   api.get('/post/').then(
  //     (res)=>{
  //       // console.log(res)
  //       setPosts(res.data.result)
  //     }
  //   )
  // };
  useEffect(() => {
    // fetchData();
    // console.log(posts);
        api.get('/post/').then(
      (res)=>{
        // console.log(res)
        setPosts(res.data.result)
      }).catch((error:any)=>{
        // console.log(error)
        toast.error(error.response.data.detail)
      })
  }, []);

  return (
    <>
    <div className="container">
      <div className="row">
          <h1>posts list</h1>

          {posts && posts.map((post) => <PostItem key={post.id}  post={post} />)}

      </div>
    </div>
      
      {/* <ul>{posts && posts.map((p) => <li key={p.id}>{p.title}</li>)}</ul> */}
    </>
  );
};

export default Posts;
