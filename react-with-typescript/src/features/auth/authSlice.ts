import {createSlice,PayloadAction, createAsyncThunk} from '@reduxjs/toolkit'
import UserInterface from '../../interface/posts/UserInterface'
import api  from '../../utils//api'







interface AuthState {
    token:string | null,
    isAuthenticated:boolean | null,
    loading:boolean,
    user:UserInterface | null
    users:UserInterface[] | null
}


const initialState:AuthState = {
    token:localStorage.getItem('token'),
    isAuthenticated:null,
    loading:true,
    user:null,
    users:[]
}

// First, create the thunk
export const fetchUsers:any = createAsyncThunk(
    'users/fetchUsers',
    async () => {
      const response = await api.get('/users')
      // console.log(response)
      return await response.data
    }
  )



export const authSlice = createSlice({

    name:'auth',
    initialState,
    reducers:{

    },
    extraReducers: (builder) => {
        // Add reducers for additional action types here, and handle loading state as needed
        builder.addCase(fetchUsers.fulfilled, (state, action:PayloadAction<UserInterface[]>) => {
          // Add user to the state array
          state.users = action.payload
        })
        builder.addCase(fetchUsers.rejected, (state, action:PayloadAction<any>) => {
            // Add user to the state array
            state.loading = false
            state.isAuthenticated = false

          })

      },

}
)

// export const fetchUsers
// export const {fetchUsers} = authSlice.actions

export default authSlice.reducer