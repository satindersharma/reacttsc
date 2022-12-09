import { useState } from "react";
import { toast } from "react-toastify";
import api from "../../utils/api";

const PostForm = () => {
  const [values, setValues] = useState({
    title: "",
    body: "",
  });

  const handleInputChange = (e:any) => {
    const { name, value } = e.target;
    setValues({ ...values, [name]: value });
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    // console.log(values);

    api.post('/post/',values).then((res)=>{
      console.log(res.data)
      toast.success('post added')
    }).catch((err)=>{
      console.log(err.response)
    })
  };

  return (
    <div className="container">
      <div className="row pt-5">
        <h4 className="text-center pb-2">Post add</h4>
      </div>
      <div className="row justify-content-center">
        <form onSubmit={handleSubmit} className="col-6">
          <div className="form-group">
            <label className="form-label" htmlFor="title">
              Title
            </label>
            <input
              className="form-control"
              type="text"
              id="title"
              name="title"
              value={values.title}
              onChange={handleInputChange}
            />
          </div>
          <div className="form-group">
            <label className="form-label" htmlFor="body">
              Body
            </label>
            <input
              className="form-control"
              type="text"
              id="body"
              name="body"
              value={values.body}
              onChange={handleInputChange}
            />
          </div>
          <div className="form-group pt-3 text-center">
            <input
              type="submit"
              value="Add Post"
              className="btn btn-outline-dark"
            />
          </div>
        </form>
      </div>
    </div>
  );
};

export default PostForm;
