import React from 'react'
import {useDispatch} from 'react-redux'
import { removeReservation} from '../../features/reservation/reservationSlice'
interface ReservationType {
    name:string,
    index:number
}

const ReservationItem = ({name,index}:ReservationType) => {
    const dispatch = useDispatch()

      return (
    <div className="list-group">

    <div className="list-group-item m-1 d-flex justify-content-between align-items-center">
        {name} <span className=" btn badge text-dark" onClick={()=>{dispatch(removeReservation(index))}}>X</span>
    </div>
    </div>
  )
}

export default ReservationItem