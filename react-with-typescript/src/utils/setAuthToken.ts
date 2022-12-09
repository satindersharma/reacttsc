import api from './api';

// store our JWT in LS and set axios headers if we do have a token

const setAuthToken = (token:string|null) => {
  if (token) {
    // api.defaults.headers.common['x-auth-token'] = token;
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    localStorage.setItem('token', token);
  } else {
    // delete api.defaults.headers.common['x-auth-token'];
    delete api.defaults.headers.common["Authorization"]
    localStorage.removeItem('token');
  }
};

export default setAuthToken;
