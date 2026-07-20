import {
  Card,
  CardContent,
  Typography,
  Chip,
  Grid,
  LinearProgress,
  Box,
} from "@mui/material";

interface Props {
  response: {
    risk_category: string;
    confidence: number;
  };
}

export default function PredictionCard({ response }: Props) {
  const color =
    response.risk_category === "High Risk"
      ? "error"
      : response.risk_category === "Medium Risk"
      ? "warning"
      : "success";

  return (
    <Card elevation={4} sx={{ borderRadius: 3 }}>
      <CardContent>

        <Typography variant="h5" gutterBottom>
          Prediction Result
        </Typography>

        <Grid container spacing={3}>

          <Grid size={{ xs: 12, md: 6 }}>
            <Typography variant="subtitle2">
              Risk Category
            </Typography>

            <Chip
              label={response.risk_category}
              color={color}
              size="medium"
              sx={{
                mt: 1,
                fontSize: 16,
                fontWeight: 600,
              }}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <Typography variant="subtitle2">
              Confidence
            </Typography>

            <Typography
              variant="h4"
              color="primary"
              fontWeight="bold"
            >
              {response.confidence}%
            </Typography>

            <LinearProgress
              variant="determinate"
              value={response.confidence}
              sx={{
                mt: 2,
                height: 12,
                borderRadius: 10,
              }}
            />
          </Grid>

        </Grid>

      </CardContent>
    </Card>
  );
}