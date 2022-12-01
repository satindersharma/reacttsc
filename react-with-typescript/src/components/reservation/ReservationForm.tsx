import { Formik, Form, Field } from "formik";
import * as Yup from "yup";
import {useDispatch} from 'react-redux'
import {addReservation} from '../../features/reservation/reservationSlice'

const ReservationSchema = Yup.object({

    
  name: Yup.string()
    .min(2, "Too Short!")
    .max(50, "Too Long!")
    .required("Required"),
});
// type ReservationState = Yup.InferType<typeof ReservationSchema>;



const ReservationForm = () => {

    const dispatch = useDispatch()

  return (
    <>
    <div className="container text-center">
        <div className="row"><h3>Reservation Form</h3></div>
        <div className="row ">

        <div className="col">

        
      <Formik
        initialValues={{
          name: "",
        }}
        validationSchema={ReservationSchema}
        onSubmit={(values,{ resetForm }) => {
          // same shape as initial values

          console.log(values);
          dispatch(addReservation(values.name));
          resetForm()
        }}
      >
        {({ errors, touched }) => (

          <Form>
            <Field name="name"  className="col-3 form-control mb-2" />

            {errors.name && touched.name ? <div>{errors.name}</div> : null}

            <button className="btn btn-outline-success" type="submit">Submit</button>
          </Form>
        )}
      </Formik>
      </div>
      </div>
    </div>
    </>
  );
};

export default ReservationForm;
