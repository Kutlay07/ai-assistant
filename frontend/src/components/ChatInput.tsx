import { useState } from "react";
import { SendHorizontal } from "lucide-react";


type ChatInputProps = {
    onSend: (message: string) => void;
};

export default function ChatInput({
    onSend,
}: ChatInputProps) {
    const [message, setMessage] = useState("")

    function handleSubmit() {
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
                    className="
                        rounded-xl
                        bg-neutral-800
                        px-5
                        text-white
                        transition
                        hover:bg-neutral-700
                    "
                >
                    <SendHorizontal size={18} />
                </button>
            </div>
        </footer>
    );
}