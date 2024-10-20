"""
Parallel Course. Topology sorting
"""
from typing import List
# Time: O(n+m)
# Space: O(n+m)
def minSemesters(n: int, relations: List[List[int]]):
    # because the course is 1-indexed
    graph = {i: [] for i in range(1, n+1)}
    in_degree = {i: 0 for i in range(1, n+1)}

    for relation in relations:
        prev, nxt = relation
        # build adj list
        graph[prev].append(nxt)
        in_degree[nxt] += 1

    # find course with no in degree to starter
    queue = []
    for node in graph:
        if in_degree[node] == 0:
            queue.append(node)

    semesters = 0
    studied_course = 0
    while queue:
        semesters += 1
        next_queue = []
        for node in queue: # go through all available course to finish this semester
            studied_course += 1
            other_courses_previously_blocked = graph[node]
            for course in other_courses_previously_blocked:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    next_queue.append(course)
        queue = next_queue

    return semesters if studied_course == n else -1



def minSemester(n: int, relations: List[List[int]]):
    # adj graph, in_degree. u --> v
    # Traverse U(s) with  0 in degree
    # BFS to search in parallel

    graph = {i:[] for i in range(1, n+1)} # course 1 indexed
    in_degree = {i: 0 for i in range(1, n+1)}
    for relation in relations:
        prereq, course  = relation
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = []
    for course in graph:
        if in_degree[course] == 0:
            queue.append(course)

    semesters = 0
    studied_courses = 0

    while queue:
        semesters += 1
        next_semester_courses = []
        for course in queue:
            studied_courses += 1
            courses_previously_blocked_by_course = graph[course]
            for c in courses_previously_blocked_by_course:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    next_semester_courses.append(c)
        queue = next_semester_courses

    return semesters if studied_courses == n else - 1






