class SegmentTree:
    def __init__(self, xs):
        self.cnts = collections.defaultdict(int)
        self.total = collections.defaultdict(int)
        self.xs = xs

    def update(self, v, tl, tr, l, r, h):
        if l > r:
            return

        if l == tl and r == tr:
            self.cnts[v] += h
        else:
            tm = (tl + tr)//2
            self.update(v*2, tl, tm, l, min(r, tm), h)
            self.update(v*2+1, tm+1, tr, max(l, tm+1), r, h)

        if self.cnts[v] > 0:
            self.total[v] = self.xs[tr + 1] - self.xs[tl]
        else:
            self.total[v] = self.total[v*2] + self.total[v*2+1]

        return self.total[v]
