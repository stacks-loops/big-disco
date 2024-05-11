import { configureStore } from '@reduxjs/toolkit'
import exercisesReducer from './features/exercisesSlice'

export default configureStore({
    reducer: {
        exercises: exercisesReducer,
    },
})