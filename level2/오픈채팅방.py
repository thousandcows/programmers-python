class OpenChat:
    @staticmethod
    def solution(record: list[str]) -> list[str]:
        answer = []
        id_name_dict, command_dict = {}, {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
        for r in record:
            command, user_id, *arg = r.split(" ")
            if command in ["Enter", "Change"]:
                id_name_dict[user_id] = arg[0]

        for r in record:
            command, user_id, *arg = r.split(" ")
            if command != "Change":
                answer.append(f"{id_name_dict[user_id]}{command_dict[command]}")

        return answer
