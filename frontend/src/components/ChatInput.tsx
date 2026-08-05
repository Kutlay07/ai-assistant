import { useState } from "react";
import { SendHorizontal } from "lucide-react";


type ChatInputProps = {
    onSend: (message: string) => void;
    isLoading: boolean,
};

export default function ChatInput({
    onSend,
    isLoading,
}: ChatInputProps) {
    const [message, setMessage] = useState("")

    function handleSubmit() {

        if (isLoading) {
            return;
        }

        if (message.trim() === "") {
            return;
        }

        onSend(message);

        setMessage("");
    }

    return (
        <footer className="border-t border-neutral-800 p-4 bg-neutral-800">

            <div className="mx-auto flex max-w-4xl gap-3">
                <textarea 
                    placeholder="Message AI Assistant..."

                    value={message}

                    onChange={(event) =>
                        setMessage(event.target.value)
                    }

                    disabled={isLoading}

                    onKeyDown={(event) => {

                    if (event.key === "Enter" && !event.shiftKey) {
                        event.preventDefault();
                        handleSubmit();
                    }

                }}
                    className="
                        flex-1
                        rounded-xl
                        border
                        border-neutral-700
                        bg-neutral-900
                        px-4
                        py-3
                        text-white
                        outline-none
                        placeholder:text-neutral-400
                    "
                />

                <button
                    onClick={handleSubmit}
                    disabled={isLoading}
                    className={`
                        rounded-xl
                        px-5
                        bg-neutral-800
                        text-white
                        transition
                        ${
                            isLoading
                                ? "bg-neutral-700 cursor-not-allowed"
                                : "bg-neutral-800 hover:bg-neutral-700"
                            }
                        `}
                    
                >
                    <SendHorizontal size={18} />
                </button>
            </div>
        </footer>
    );
}