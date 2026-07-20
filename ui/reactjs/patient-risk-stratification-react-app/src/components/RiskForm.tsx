import { useEffect } from "react";
import {
  Box,
  Card,
  CardContent,
  Typography,
  TextField,
  MenuItem,
  Button,
  Stack,
  Divider,
  CircularProgress,
} from "@mui/material";

import Grid from "@mui/material/Grid";

import { useForm, Controller } from "react-hook-form";

export interface RiskRequest {
  age: number;
  gender: string;
  glucose: number;
  cholesterol: number;
  bmi: number;
  systolic_bp: number;
  diastolic_bp: number;
  heart_rate: number;
  smoking: string;
  alcohol: string;
  clinical_notes: string;
}

interface Props {
  loading: boolean;
  onSubmit: (data: RiskRequest) => void;
}

const sampleData: RiskRequest = {
  age: 62,
  gender: "Male",
  glucose: 240,
  cholesterol: 280,
  bmi: 34,
  systolic_bp: 180,
  diastolic_bp: 110,
  heart_rate: 98,
  smoking: "Yes",
  alcohol: "No",
  clinical_notes:
    "Patient has severe hypertension and uncontrolled diabetes",
};

export default function RiskForm({
  loading,
  onSubmit,
}: Props) {
  const {
    control,
    handleSubmit,
    reset,
  } = useForm<RiskRequest>({
    defaultValues: sampleData,
  });

  useEffect(() => {
    reset(sampleData);
  }, [reset]);

  return (
    <Card
      elevation={4}
      sx={{
        borderRadius: 3,
      }}
    >
      <CardContent>

        <Typography
          variant="h5"
          fontWeight="bold"
          gutterBottom
        >
          Patient Risk Prediction
        </Typography>

        <Typography
          color="text.secondary"
          mb={3}
        >
          Enter patient clinical information to predict risk.
        </Typography>

        <Divider sx={{ mb: 3 }} />

        <Box
          component="form"
          onSubmit={handleSubmit(onSubmit)}
        >

          <Grid container spacing={2}>

            <Grid size={{ xs: 12, md: 4 }}>
              <Controller
                name="age"
                control={control}
                render={({ field }) => (
                  <TextField
                    {...field}
                    fullWidth
                    type="number"
                    label="Age"
                  />
                )}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Controller
                name="gender"
                control={control}
                render={({ field }) => (
                  <TextField
                    {...field}
                    select
                    fullWidth
                    label="Gender"
                  >
                    <MenuItem value="Male">Male</MenuItem>
                    <MenuItem value="Female">Female</MenuItem>
                  </TextField>
                )}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Controller
                name="bmi"
                control={control}
                render={({ field }) => (
                  <TextField
                    {...field}
                    fullWidth
                    type="number"
                    label="BMI"
                  />
                )}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Controller
                name="glucose"
                control={control}
                render={({ field }) => (
                  <TextField
                    {...field}
                    fullWidth
                    type="number"
                    label="Glucose"
                  />
                )}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Controller
                name="cholesterol"
                control={control}
                render={({ field }) => (
                  <TextField
                    {...field}
                    fullWidth
                    type="number"
                    label="Cholesterol"
                  />
                )}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Controller
                name="heart_rate"
                control={control}
                render={({ field }) => (
                  <TextField
                    {...field}
                    fullWidth
                    type="number"
                    label="Heart Rate"
                  />
                )}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Controller
                name="systolic_bp"
                control={control}
                render={({ field }) => (
                  <TextField
                    {...field}
                    fullWidth
                    type="number"
                    label="Systolic BP"
                  />
                )}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Controller
                name="diastolic_bp"
                control={control}
                render={({ field }) => (
                  <TextField
                    {...field}
                    fullWidth
                    type="number"
                    label="Diastolic BP"
                  />
                )}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Controller
                name="smoking"
                control={control}
                render={({ field }) => (
                  <TextField
                    {...field}
                    select
                    fullWidth
                    label="Smoking"
                  >
                    <MenuItem value="Yes">Yes</MenuItem>
                    <MenuItem value="No">No</MenuItem>
                  </TextField>
                )}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Controller
                name="alcohol"
                control={control}
                render={({ field }) => (
                  <TextField
                    {...field}
                    select
                    fullWidth
                    label="Alcohol"
                  >
                    <MenuItem value="Yes">Yes</MenuItem>
                    <MenuItem value="No">No</MenuItem>
                  </TextField>
                )}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Controller
                name="clinical_notes"
                control={control}
                render={({ field }) => (
                  <TextField
                    {...field}
                    fullWidth
                    multiline
                    rows={5}
                    label="Clinical Notes"
                    placeholder="Enter patient clinical observations..."
                  />
                )}
              />
            </Grid>

          </Grid>

          <Divider sx={{ my: 4 }} />

          <Stack
            direction="row"
            spacing={2}
            justifycontent="center"
          >

            <Button
              variant="outlined"
              color="secondary"
              onClick={() => reset()}
            >
              Reset
            </Button>

            <Button
              variant="outlined"
              onClick={() => reset(sampleData)}
            >
              Load Sample
            </Button>

            <Button
              type="submit"
              variant="contained"
              size="large"
              disabled={loading}
              sx={{
                minWidth: 180,
              }}
            >
              {loading ? (
                <CircularProgress
                  size={24}
                  color="inherit"
                />
              ) : (
                "Predict Risk"
              )}
            </Button>

          </Stack>

        </Box>

      </CardContent>
    </Card>
  );
}