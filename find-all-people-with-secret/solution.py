# LeetCode: Find All People With Secret
from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        meetings.sort(key=lambda x: x[2])

        secret = set([0, firstPerson])
        i = 0

        while i < len(meetings):
            time = meetings[i][2]

            graph = defaultdict(list)
            people = set()

            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1

            queue = deque()
            visited = set()

            for p in people:
                if p in secret:
                    queue.append(p)
                    visited.add(p)

            while queue:
                curr = queue.popleft()
                for nei in graph[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

            secret |= visited

        return list(secret)
