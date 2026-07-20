export interface RiskRequest{
 age:number;gender:string;glucose:number;cholesterol:number;bmi:number;
 systolic_bp:number;diastolic_bp:number;heart_rate:number;
 smoking:string;alcohol:string;clinical_notes:string;
}
export interface RiskResponse{
 risk_category:string;
 confidence:number;
}
