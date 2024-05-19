import re


class SkillTree:
    @staticmethod
    def solution(skill, skill_trees):
        answer = 0

        for sk in skill_trees:
            sk = re.sub(f"[^{skill}]", "", sk)
            flag = True
            for origin, compare in zip(sk, skill):
                if origin != compare:
                    flag = False
                    break
            answer += flag

        return answer
