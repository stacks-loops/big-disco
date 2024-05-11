import React from 'react'
import { Formik, Form, Field, FieldArray } from 'formik'
import { v4 as uuidv4 } from 'uuid'
import * as Yup from 'yup'

const workoutStepSchema = Yup.object().shape({
    exerciseName: Yup.string().required('Exercise name is required'),
    intervalType: Yup.string().oneOf(['days'], 'Currently only "days" interval is supported'), 
    intervalValue: Yup.number()
      .required('Interval value is required')
      .positive('Interval must be a positive number')
      .integer('Interval must be whole days'),
  });
  
  const formSchema = Yup.object().shape({
    title: Yup.string().required('Workout title is required'),
    steps: Yup.array()
      .of(workoutStepSchema)
      .min(1, 'You must add at least one workout step'),
  });



const initialFormData = {
    title: '', 
    steps: [
        { id: uuidv4(), exerciseName: '', description: '', sets: '', reps: '', interval: '' }
    ]
}

const workoutStep = {
    exerciseName: '',
    description: '',
    sets: '',
    reps: '',
    intervalType: 'days',
    intervalValue: ''
}

function DinoForm() {
    return (
        <Formik 
        initialValues={initialFormData}
        onSubmit={(values) => console.log(values)}
        >
        {({ values }) => (
            <Form>
                <Field type="text" name="title" placeholder="Loop Name" />

                <FieldArray name="steps">
                    {({ push, remove }) => (
                        <div>
                            {values.steps.map((step, index) => (
                                <div key={step.id}>
                                    <Field type="text" name={`steps[${index}].exerciseName`} placeholder="Exercise Name" />
                                    <Field as="select" name={`steps[${index}].intervalType`}>
                                        <option value="days">Days</option>
                                    </Field>
                                    <Field type="number" name={`steps[${index}].intervalValue`} placeholder="Repeat Every.... days"/>




                                    <button type="button" onClick={() => remove(index)}>Remove Step</button>
                                    </div>
                            ))}
                            <button type="button" onClick={() => push({ id: uuidv4(), exerciseName: '', description: '', sets: '', reps: '', interval: '' })}>Add Step</button>
                        </div>
                    )}
                </FieldArray>

                <button type="submit">Submit</button>


            </Form>


            
        )}
        </Formik>
    )
}

export default DinoForm;