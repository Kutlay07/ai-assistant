import { useState } from "react";

import Header from "./components/Header"
import Sidebar from "./components/Sidebar"
import ChatWindow from "./components/ChatWindow"
import ChatInput from "./components/ChatInput"


export default function App() {
    type ChatMessage = {
        role: "user" | "assistant";
        content: string;
    };

    const [messages, setMessages] = useState<ChatMessage[]>([]);

    function handleSend(message: string) {
        const newMessage: ChatMessage = {
            role: "user",
            content: message,
        };
        
        setMessages((previousMessages) => [
            ...previousMessages,
            newMessage,
        ]);
    }

    return (
        <div className="flex h-screen flex-col">
            
            <Header />

            <div className="flex flex-1">

                <Sidebar/>

                <div className="flex flex-1 flex-col">

                    <ChatWindow 
                        messages={messages}/>


                    <ChatInput 
                        onSend={handleSend}
                    />

                </div>
            </div>
        </div>

    );
}

