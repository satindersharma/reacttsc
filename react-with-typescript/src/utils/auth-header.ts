export default function authHeader() {
    const token = localStorage.getItem('token');
  
    if (token) {
      return { Authorization: `Bearer ${token}` };
      // for Node.js Express back-end
        // return { 'x-access-token': user.accessToken };
    } else {
      return {};
    }
  }


  