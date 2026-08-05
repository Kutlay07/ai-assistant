export interface Message {
    role: "user" | "assistant";
    content: string;
    isTyping?: boolean;
}


export interface ChatRequest {
    message: string;
}


export interface ChatResponse {
    response: string;
}