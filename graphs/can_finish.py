class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        
        # Initialize in-degree for ALL courses (0 to numCourses-1)
        in_degree = [0] * numCourses
        adj = defaultdict(list)
        
        # Build adjacency list and in-degree count
        for course, prereq in prerequisites:
            adj[prereq].append(course)  # Edge from prereq to course
            in_degree[course] += 1      # Course has one more prerequisite
        
        # Find all courses with no prerequisites
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        completed_courses = 0
        
        # Kahn's algorithm
        while queue:
            current_course = queue.popleft()
            completed_courses += 1
            
            # Remove this course and update dependent courses
            for dependent_course in adj[current_course]:
                in_degree[dependent_course] -= 1
                if in_degree[dependent_course] == 0:
                    queue.append(dependent_course)
        
        # If we completed all courses, no cycle exists
        return completed_courses == numCourses

