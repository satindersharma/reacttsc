import {RootState} from '../../store'
import {useSelector} from 'react-redux'
import ReservationItem from './ReservationItem'
import ReservationForm from './ReservationForm'


const Reservation = () => {
   
    const reservations = useSelector(  (state: RootState) => state.reservation.value)

  return (
    <div className="container p-5">
        <div className="row">
        <div className='mb-2'>Reservation</div>
        </div>
        <div className="row mb-4">

            {reservations && reservations.map((name,index)=>(<ReservationItem key={index} name={name} index={index}/>))}
        </div>
        <div className="row">
        <ReservationForm/>
        </div>
    </div>
  )
}

export default Reservation