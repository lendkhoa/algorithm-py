from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        print(f"\nUnion {x1} {x2}")
        if p1 == p2:
            return False
        if self.parent[p1] > self.parent[p2]:
            print(f"  p1 > p2")
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            print(f"  p1 <= p2")
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        print(f"\n {self.parent}")
        print(f" {self.rank}\n")
        return True


def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    uf = UnionFind(len(accounts))
    email_to_acc = {}  # email _. index of acc

    for i, a in enumerate(accounts):
        for e in a[1:]:
            if e in email_to_acc:
                # this email not only belong to index
                uf.union(i, email_to_acc[e])
            else:
                email_to_acc[e] = i

    email_group = defaultdict(list)
    for e, i in email_to_acc.items():
        leader = uf.find(i)
        email_group[leader].append(e)

    res = []
    for i, emails in email_group.items():
        name = accounts[i][0]
        res.append([name] + sorted(emails[i]))

    return res


uf = UnionFind(5)

print(uf.parent)
print(uf.rank)

for i in range(5):
    uf.union(i, 1)

for i in range(5):
    print(f" {i}", end=" ")
print("\n")
print(uf.parent)
print(uf.rank)
