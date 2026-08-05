import { useState, useEffect} from "react";

import type { Message } from "./types/chat";
import { streamMessage, getHistory } from "./services/chatService";
import Header from "./components/Header"
import Sidebar from "./components/Sidebar"
import ChatWindow from "./components/ChatWindow"
import ChatInput from "./components/ChatInput"


export default function App() {


    const [messages, setMessages] = useState<Message[]>([]);

    const [isLoading, setIsLoading] = useState(false);

    async function handleSend(message: string) {

    setIsLoading(true);

    try {

        const userMessage: Message = {
            role: "user",
            content: message,
        };

        setMessages((previousMessages) => [
            ...previousMessages,
            userMessage,
        ]);

        const assistantMessage: Message = {
            role: "assistant",
            content: "",
            isTyping: true,
        };

        setMessages((previousMessages) => [
            ...previousMessages,
            assistantMessage,
        ]);

        await streamMessage(
            message,
            (chunk) => {
                setMessages((previousMessages) => {
                    const updatedMessages = [...previousMessages];

                    const lastMessage =
                        updatedMessages[updatedMessages.length - 1];

                    updatedMessages[
                        updatedMessages.length - 1
                    ] = {
                        ...lastMessage,
                        isTyping: false,
                        content: lastMessage.content + chunk,
                    };

                    return updatedMessages;
                });
            }
        );

        }
        catch (error) {
            console.error(error);

            setMessages((previousMessages) => {

                const updatedMessages = [...previousMessages];

                updatedMessages[
                    updatedMessages.length - 1
                ] = {
                    ...updatedMessages[updatedMessages.length - 1],
                    isTyping: false,
                    content: "⚠ Unable to connect to the server.",
                };

                return updatedMessages;
            });
        }
    finally {

        setIsLoading(false);

    }
}

    useEffect(() => {
        async function loadHistory() {
            const history = await getHistory();

            setMessages(history);
        }

        loadHistory();
    }, []);

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
                        isLoading={isLoading}
                    />

                </div>
            </div>
        </div>

    );
}