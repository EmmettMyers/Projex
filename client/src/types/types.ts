import { Ref, ref } from "vue";

export interface Project {
    name: string;
    description: string;
    difficulty: string;
    time: string;
    tools: string[];
    image?: string;
    code?: Codebase;
    saved?: boolean;
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

export interface Preferences {
    [key: string]: Ref<string[]>;
    projectInterests: Ref<string[]>;
    toolsKnown: Ref<string[]>;
    toolsDesiredToLearn: Ref<string[]>;
    topicInterests: Ref<string[]>;
}

export interface Options {
    [key: string]: Ref<string[]>;
    type: Ref<string[]>;
    difficulty: Ref<string[]>;
    time: Ref<string[]>;
    tools: Ref<string[]>;
    topics: Ref<string[]>;
}