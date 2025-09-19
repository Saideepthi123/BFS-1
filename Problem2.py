class Solution(object):
    # tc : O(V+E) where v is the num of courses, and e is the number of dependecies fo the courses ( egdes of the graph)
    # sc : O(V+E) 
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # to take a course ai first bi should be selected and so on...
        # and since the depedent courses for each course can be more than 2 its not a binary tree but can b narrowed down to 
        # a n array tree and once the whole test case is drawn its moving to the graph ...
        # things needed : i need to know the depent coursed for each course to be taken before dng this course
        # will created a hashmap or adj_list where the key is the course and the values as the depeent courses of that course

        # build adjacency list
        adj_list = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        # if while processign a course x and we are returning to x again that means there is a cyclic dependent and return False
        # if not then we have successuly able to take course x and its dependents y,z and if there are any other courses left we again check for the other courses similar way 

        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting ( processign if we can take this course successfully), 2 = visited ( already taken)

        def dfs(course):
            if visited[course] == 1:  # cycle detected
                return False
            if visited[course] == 2:  # already processed
                return True

            visited[course] = 1  # mark as visiting
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            visited[course] = 2  # mark as visited
            return True

        # check each course graph may be disconnected and we have to check every course and see we can take them successfully 
        for c in range(numCourses):
            if visited[c] == 0: 
                if not dfs(c):
                    return False

        return True

        
