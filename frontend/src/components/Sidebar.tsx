import SidebarButton from "./SidebarButton";

export default function Sidebar() {
    return (
        <aside
            className="
                flex
                w-64
                flex-col
                border-r
                border-neutral-800
                bg-neutral-900
                p-4
                text-white
            "
        >
        
        <h2 className="mb-6 text-xl font-semibold">
            Chats
        </h2>

        <SidebarButton>
            + New Chat
        </SidebarButton>

        <div className="mt-auto space-y-2">

            <SidebarButton>
                Settings
            </SidebarButton>

            <SidebarButton>
                Profile
            </SidebarButton>

            </div>
        </aside>
    );
}