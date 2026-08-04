import type { ChatMessage } from "../types/chat";

import Message from "./Message";

type ChatWindowProps = {
    messages: ChatMessage[];
};

export default function ChatWindow({
    messages,
}: ChatWindowProps) {
    return (
        <main className="
                    flex-1
                    overflow-y-auto
                    p-6
                    bg-neutral-700
                "
            >
            
            <div className="mx-auto max-w-4xl">
                {messages.map((message) => (
                    <Message
                        key={message.content}
                        role={message.role}
                        content={message.content}
                />
            ))}
            </div>
        </main>
    );
}