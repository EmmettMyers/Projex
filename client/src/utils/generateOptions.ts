import { ref } from 'vue';

export const types = ref<string[]>([
    'Website', 'Mobile App', 'Game', 'Desktop App', 'Data Analysis', 'Machine Learning', 
    'Artificial Intelligence', 'API Development', 'Database Management', 'Blockchain', 
    'Automation', 'Virtual Reality', 'Cloud Computing', 'Computer Vision'
]);

export const difficulties = ref<string[]>([
    'Starter', 'Learning Curve', 'Intermediate', 'Challenging', 'Advanced'
]);

export const times = ref<string[]>([
    '1-3 Days', '1 Week', '2-3 Weeks', '1 Month', '2-3 Months', '4-6 Months', '7+ Months'
]);

export const tools = ref<string[]>();

export const resetTools = () => {
    tools.value = [
        'Java', 'Python', 'HTML', 'CSS', 'JavaScript', 'TypeScript', 'React', 'Angular', 'Vue', 'Django', 
        'Node', 'Swift', 'Go', 'Flask', 'Ruby on Rails', 'GraphQL', 'MongoDB', 'MySQL', 'PostgreSQL', 'Kotlin', 
        'React Native', 'AWS', 'Azure', 'Docker', 'Dart', 'Unity', 'Unreal Engine', 'R', 'MATLAB', 'Godot',
        'Power BI', 'Kubernetes'
    ];
}

export const topics = ref<string[]>();

export const resetTopics = () => {
    topics.value = [
        'Sports', 'Education', 'Finance', 'Career', 'Food', 'Scheduling', 'Music', 'History', 'Science',
        'Books', 'Movies', 'Fitness', 'Social', 'Writing', 'Crafts', 'Pets', 'Photography', 'Activism',
        'Fashion', 'News', 'Art', 'Parenting', 'Language', 'Gaming', 'Children', 'Math', 'Environment',
        'Weather', 'Hiking', 'Journaling', 'Cars', 'Space', 'Beauty'
    ];
}