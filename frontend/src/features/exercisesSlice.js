import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'

// basic structure for fetch called async thunk
export const fetchExercises = createAsyncThunk('exercises/fetchExercises', async () => {
    const response = await fetch('/exercises')
    const data = await response.json()
    return data;
})
//creating new one
export const createExercise = createAsyncThunk(
    'exercises/createExercise', 
    async (newExercise) => {
        const response = await fetch('/exercises', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newExercise)
    })
    if (response.ok) {
        const data = await response.json()
        return data
    } else {
        throw new Error('Error creating a new exercise')
    }
})

// async thunk for updating
export const updateExercise = createAsyncThunk(
    'exercises/updateExercise',
     async ({ id, ...updateExerciseAction }) => {
    const response = await fetch(`/exercises/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(updateExerciseAction)
    });
    if (response.ok) {
      const data = await response.json();
      return data;
    } else {
      throw new Error('Error updating exercise');
    }
  });

export const deleteExercise = createAsyncThunk(
    'exercises/deleteExercise', 
    async (exerciseId) => {
    const response = await fetch(`/exercises/${exerciseId}`, {
    method: 'DELETE',
    });
    if (response.ok) {
      return exerciseId; // Return the ID of the deleted exercise
    } else {
      throw new Error('Error deleting exercise');
    }
  });
  

  const exercisesSlice = createSlice({
    name: 'exercises',
    initialState: {
      data: [],
      status: 'idle',
      error: null,
    },
    reducers: {}, // Currently no synchronous reducers
    extraReducers: (builder) => {
      builder
        // Handle pending, fulfilled, and rejected states for fetchExercises
        .addCase(fetchExercises.pending, (state) => {
          state.status = 'loading';
        })
        .addCase(fetchExercises.fulfilled, (state, action) => {
          state.status = 'succeeded';
          state.data = action.payload;
        })
        .addCase(fetchExercises.rejected, (state, action) => {
          state.status = 'failed';
          state.error = action.error.message;
        })
  
        // Handle pending, fulfilled, and rejected states for createExercise
        .addCase(createExercise.pending, (state) => {
          state.status = 'loading';
        })
        .addCase(createExercise.fulfilled, (state, action) => {
          state.status = 'succeeded';
          state.data.push(action.payload); // Add new exercise to the array
        })
        .addCase(createExercise.rejected, (state, action) => {
          state.status = 'failed';
          state.error = action.error.message;
        })
  
        // Handle pending, fulfilled, and rejected states for updateExercise
        .addCase(updateExercise.pending, (state) => {
          state.status = 'loading';
        })
        .addCase(updateExercise.fulfilled, (state, action) => {
          state.status = 'succeeded';
          const index = state.data.findIndex(
            (exercise) => exercise.id === action.payload.id
          );
          if (index !== -1) {
            state.data[index] = action.payload; // Update exercise at the found index
          }
        })
        .addCase(updateExercise.rejected, (state, action) => {
          state.status = 'failed';
          state.error = action.error.message;
        })
  
        // Handle pending, fulfilled, and rejected states for deleteExercise
        .addCase(deleteExercise.pending, (state) => {
          state.status = 'loading';
        })
        .addCase(deleteExercise.fulfilled, (state, action) => {
          state.status = 'succeeded';
          state.data = state.data.filter(exercise => exercise.id !== action.payload);
        })
        .addCase(deleteExercise.rejected, (state, action) => {
          state.status = 'failed';
          state.error = action.error.message;
        });
    },
  });


export default exercisesSlice.reducer