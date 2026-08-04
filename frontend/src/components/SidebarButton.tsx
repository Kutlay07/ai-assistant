type SidebarButtonProps = {
    children: React.ReactNode;
};

export default function SidebarButton({
    children,
}: SidebarButtonProps) {
    return (
        <button
            className="
                w-full
                rounded-lg
                bg-neutral-800
                p-3
                text-left
                transition
                hover:bg-neutral-700
                "
            >
                {children}
            </button>
    );
}