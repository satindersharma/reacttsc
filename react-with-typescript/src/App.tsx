import React from 'react';
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


function App() {
  return (
    <Router>
        <Navbar/>
      <Routes>
        <Route path='/' element={<Landing/>}/>
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
