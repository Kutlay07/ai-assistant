import { post, get } from "../api/client";

import type { 
    ChatRequest, 
    ChatResponse, 
    Message,
} from "../types/chat";


export async function sendMessage(
    message: string,
): Promise<ChatResponse> {

    const request: ChatRequest = {
        message,
    };

    return post<ChatResponse>(
        "/chat",
        request,
    );
}

export async function streamMessage(
    message: string,
    onChunk: (chunk: string) => void,
): Promise<void> {
    
    const response = await fetch(
        "http://127.0.0.1:8000/api/v1/chat/stream",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                message,
            }),
        }
    );


    if (!response.body) {
        throw new Error("Response body is empty");
    }


    const reader = response.body.getReader();
    const decoder = new TextDecoder();


    while (true) {
        const { done, value } = await reader.read();

        if (done) {
            break;
        }


        const chunk = decoder.decode(value);

        onChunk(chunk);
    }
}

export async function getHistory(): Promise<Message[]> {
    return get<Message[]>("/chat/history");
}