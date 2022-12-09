import React, { useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Landing from './components/layout/Landing';
import Navbar from './components/layout/Navbar';

import NotFound from './components/layout/NotFound';
import Dashboard from './components/dashboard/Dashboard';
import PostForm from './components/posts/PostForm';
import Posts from './components/posts/Posts';
import Reservation from './components/reservation/Reservation';
import Users from './components/users/Users';
import Login from './components/auth/Login';
import Signup from './components/auth/Signup';


function App() {
// useEffect(()=>{
//   // check for token in LS when app first runs
//   if (localStorage.token) {
//     // if there is a token set axios headers for all requests
//     setAuthToken(localStorage.token);
//   }
//   // try to fetch a user, if no token or invalid token we
//   // will get a 401 response from our API
//   store.dispatch(loadUser());

//   // log user out from all tabs if they log out in one tab
//   window.addEventListener('storage', () => {
//     if (!localStorage.token) store.dispatch({ type: LOGOUT });
//   });
// })

  return (
    <Router>
        <Navbar/>
      <Routes>
        <Route path='/' element={<Landing/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/signup' element={<Signup/>}/>
        <Route path='/dashboard' element={<Dashboard/>}/>
        <Route path='/post' element={<PostForm/>}/>
        <Route path='/posts' element={<Posts/>}/>
        <Route path='/users' element={<Users/>}/>
        <Route path='/reservation' element={<Reservation/>}/>
        <Route path="/*" element={<NotFound />} />
      </Routes>
    </Router>
  )
}

export default App;
