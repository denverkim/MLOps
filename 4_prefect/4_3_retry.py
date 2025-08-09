from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta
import random


# ✅ 재시도 설정 (최대 3번, 각 5초 간격)
@task(retries=3, retry_delay_seconds=5, description="랜덤 에러 발생 Task - 재시도 예제")
def unstable_task():
    number = random.randint(1, 10)
    print(f"[실행 로그] 생성된 숫자: {number}")

    if number < 7:
        raise ValueError(f"[에러] 숫자 {number}가 너무 작습니다. 실패합니다.")

    return f"[성공] 숫자 {number}는 충분히 큽니다."


@flow(name="에러 재시도 및 로깅 실습")
def retry_logging_flow():
    result = unstable_task()
    print(f"[최종 결과] {result}")


if __name__ == "__main__":
    retry_logging_flow()
