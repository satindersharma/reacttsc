import { applyMiddleware, configureStore } from '@reduxjs/toolkit'
import thunkMiddleware from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'
import { combineReducers } from 'redux'
import reservationReducer  from './features/reservation/reservationSlice'
import authReducer from './features/auth/authSlice'



const initialState = {};

const middlewares = [ thunkMiddleware]
const middlewareEnhancer = applyMiddleware(...middlewares)



// https://redux-toolkit.js.org/usage/usage-guide#manual-store-setup
export const store = configureStore({ reducer: {
    reservation:reservationReducer,
    auth:authReducer
}  ,middleware: middlewares,devTools: process.env.NODE_ENV !== 'production'})

console.log(store.getState())

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch
