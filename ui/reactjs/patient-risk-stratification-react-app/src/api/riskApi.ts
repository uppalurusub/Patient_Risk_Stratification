import axios from 'axios';
export const api=axios.create({baseURL:'http://127.0.0.1:8000'});
export async function predictRisk(payload:any){
 const {data}=await api.post('/predict-risk',payload);
 return data;
}
