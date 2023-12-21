
interface Project {
    name: string;
    description: string;
    difficulty: string;
    time: string;
    tools: Tool[];
    image: string;
    code?: Codebase;
    saved?: boolean;
}

interface Tool {
    name: string;
    logo: string;
}

interface Codebase {
    folders: Folder[];
    files: File[];
}

interface Folder {
    name: string;
    files: File[];
}

interface File {
    title: string;
    contents: string;
}