import { useState } from "react";
import RiskForm from "./components/RiskForm";
import { predictRisk } from "./api/riskApi";
import type { RiskRequest} from "../src/types/risk"
import PredictionCard from "./components/PredictionCard";

export default function App() {

    const [loading, setLoading] = useState(false);

    const [response, setResponse] = useState<any>(null);

    const handlePredict = async (data: RiskRequest) => {

        setLoading(true);

        try {

            const result = await predictRisk(data);

            setResponse(result);

        } finally {

            setLoading(false);

        }

    };

    return (

        <>
            <RiskForm
                loading={loading}
                onSubmit={handlePredict}
            />

            {response &&

                <PredictionCard
                    response={response}
                />

            }

        </>

    );

}