import { Moon, ChevronDown } from "lucide-react";


export default function Header() {
    return (
        <header
            className="
                flex
                h-16
                items-center
                justify-between
                border-b
                border-neutral-800
                px-6
                text-white
                bg-neutral-700
            "
        >
            <div>

                <h1
                    className="
                        text-xl
                        font-semibold
                    "
                >
                    AI Assistant
                </h1>
            </div>

            <div>

                <button
                    className="
                        flex
                        items-center
                        gap-2
                        rounded-lg
                        bg-neutral-800
                        px-4
                        py-2
                        hover:bg-neutral-700
                    "
                >
                    TukGPT
                    <ChevronDown size={18} />
                </button>
            </div>

            <div>

                <button
                    className="
                        rounded-lg
                        bg-neutral-800
                        p-2
                        hover:bg-neutral-700
                    "
                >
                    <Moon size={18} />
                </button>
            </div>
            <button>
                ⚙️
            </button>
        </header>
    );
}
