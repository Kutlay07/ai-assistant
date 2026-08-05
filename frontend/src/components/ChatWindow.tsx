import { useEffect, useRef } from "react";
import type { Message as ChatMessage } from "../types/chat";

import Message from "./Message";

type ChatWindowProps = {
    messages: ChatMessage[];
};

export default function ChatWindow({
    messages,
}: ChatWindowProps) {

    const bottomRef = useRef<HTMLDivElement | null>(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages]);

    return (
        <main className="
                    flex-1
                    overflow-y-auto
                    p-6
                    bg-neutral-700
                "
            >
            
            <div className="mx-auto max-w-4xl">
                {messages.map((message, index) => (
                    <Message
                        key={index}
                        role={message.role}
                        content={message.content}
                        isTyping={message.isTyping}
                /> 
                
            ))}
            <div ref={bottomRef}/>
            
            </div>
        </main>
    );
}