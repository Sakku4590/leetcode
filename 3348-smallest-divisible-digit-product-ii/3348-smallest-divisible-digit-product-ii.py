class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        n = len(num)
        a = b = c = d = 0
        tt = t
        while tt % 2 == 0: tt //= 2; a += 1
        while tt % 3 == 0: tt //= 3; b += 1
        while tt % 5 == 0: tt //= 5; c += 1
        while tt % 7 == 0: tt //= 7; d += 1
        if tt != 1:
            return "-1"

        digit_exp = {0:(0,0,0,0),1:(0,0,0,0),2:(1,0,0,0),3:(0,1,0,0),4:(2,0,0,0),
                     5:(0,0,1,0),6:(1,1,0,0),7:(0,0,0,1),8:(3,0,0,0),9:(0,2,0,0)}

        INF = float('inf')
        minD2D = [[INF]*(b+1) for _ in range(a+1)]
        minD2D[0][0] = 0
        ab_digits = [(1,0),(0,1),(2,0),(1,1),(3,0),(0,2)]
        for x in range(a+1):
            for y in range(b+1):
                if x == 0 and y == 0: continue
                best = INF
                for dx, dy in ab_digits:
                    px, py = max(0, x-dx), max(0, y-dy)
                    if px == x and py == y: continue
                    best = min(best, minD2D[px][py] + 1)
                minD2D[x][y] = best

        def need_digits(ra, rb, rc, rd):
            return minD2D[ra][rb] + rc + rd

        def construct(ra, rb, rc, rd, L):
            res = []
            cra, crb, crc, crd = ra, rb, rc, rd
            remaining = L
            i = 0
            while i < L:
                if cra == 0 and crb == 0 and crc == 0 and crd == 0:
                    res.append('1' * (L - i))
                    break
                remaining -= 1
                for dig in range(1, 10):
                    dx, dy, dz, dw = digit_exp[dig]
                    nra, nrb = max(0, cra-dx), max(0, crb-dy)
                    nrc, nrd = max(0, crc-dz), max(0, crd-dw)
                    if need_digits(nra, nrb, nrc, nrd) <= remaining:
                        res.append(str(dig))
                        cra, crb, crc, crd = nra, nrb, nrc, nrd
                        break
                i += 1
            return ''.join(res)

        if '0' not in num:
            A = B = C = D = 0
            for ch in num:
                dx, dy, dz, dw = digit_exp[int(ch)]
                A += dx; B += dy; C += dz; D += dw
            if A >= a and B >= b and C >= c and D >= d:
                return num

        PA = [0]*(n+1); PB = [0]*(n+1); PC = [0]*(n+1); PD = [0]*(n+1)
        for idx in range(n):
            dx, dy, dz, dw = digit_exp[int(num[idx])]
            PA[idx+1] = PA[idx]+dx; PB[idx+1] = PB[idx]+dy
            PC[idx+1] = PC[idx]+dz; PD[idx+1] = PD[idx]+dw

        firstZero = num.find('0')
        ans = None
        for i in range(n-1, -1, -1):
            if firstZero != -1 and firstZero < i:
                continue
            pa, pb, pc, pd = PA[i], PB[i], PC[i], PD[i]
            remaining_slots = n - 1 - i
            orig = int(num[i])
            for dig in range(orig+1, 10):
                dx, dy, dz, dw = digit_exp[dig]
                npa, npb, npc, npd = pa+dx, pb+dy, pc+dz, pd+dw
                ra, rb = max(0, a-npa), max(0, b-npb)
                rc, rd = max(0, c-npc), max(0, d-npd)
                if need_digits(ra, rb, rc, rd) <= remaining_slots:
                    suffix = construct(ra, rb, rc, rd, remaining_slots)
                    ans = num[:i] + str(dig) + suffix
                    break
            if ans is not None:
                break

        if ans is not None:
            return ans

        minAll = need_digits(a, b, c, d)
        L = max(n+1, minAll)
        return construct(a, b, c, d, L)
        