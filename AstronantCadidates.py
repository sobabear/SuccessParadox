import random

class LuckyPerson:
    maxTalent = 95
    maxLuck = 5

    def __init__(self):
        self.talent = random.uniform(0, self.maxTalent)
        self.luck = random.uniform(0, self.maxLuck)

    @property
    def total(self):
        return self.talent + self.luck

    @property
    def luckPercent(self):
        return (self.luck / self.maxLuck) * 100


# Simulate the selection process 1000 times
totalLuck = 0
totalCount = 0

for turn in range(1000):
    candidates = [LuckyPerson() for _ in range(18300)]
    candidates.sort(key=lambda x: x.total, reverse=True)

    averageLuck = sum(candidate.luckPercent for candidate in candidates[:11]) / 11

    print(f"🥶 this case: {turn} averageLuck: {averageLuck:.2f}")
    totalLuck += averageLuck
    totalCount += 1

print(f"🍠 in total : averageLuck : {totalLuck / totalCount:.2f}")
