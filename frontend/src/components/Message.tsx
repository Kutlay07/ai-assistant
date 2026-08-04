type MessageProps = {
    role: "user" | "assistant";
    content: string;
};

export default function Message({
    role,
    content,
}: MessageProps) {
    const isUser = role === "user";

    const alignment = isUser
        ? "justify-end"
        : "justify-start";

    const userStyle =
        "bg-neutral-800 text-white";

    const assistantStyle =
        "text-neutral-100";

    const style =
        isUser
            ? userStyle
            : assistantStyle;

    return (
        <div className={`mb-6 flex ${alignment}`}>
            <div
                className={`
                    rounded-2xl
                    px-5
                    py-4
                    whitespace-pre-wrap
                    break-words
                    max-w-2xl
                    ${style}
                `}
            >
                <p>{content}</p>
            </div>
        </div>
    );
}