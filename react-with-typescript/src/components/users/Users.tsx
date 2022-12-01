import React,{useEffect} from 'react'
import {useSelector,useDispatch} from 'react-redux'
import { fetchUsers } from '../../features/auth/authSlice'
import {RootState} from '../../store'
import UserItem from './UserItem'


const Users = () => {
    const dispatch = useDispatch()
    const { users } = useSelector( (state: RootState) => state.auth);

    console.log(users)
    useEffect(()=>{
        dispatch(fetchUsers())
    },[])

  return (
    <div className='container'>
      <div className="row">

      {users && users.map((user)=><UserItem key={user.id} user={user}/>) }
      </div>
      
      
      </div>
  )
}

export default Users