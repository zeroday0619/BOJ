#include <stdio.h>

// 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 
// 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다. 

int main(void) { 
    int current_hour;
    int current_minute;
    int require_minute;

    int hour, minute;
    
    scanf("%d %d", &current_hour, &current_minute);
    scanf("%d", &require_minute);

    if (require_minute >= 60)
    {
        hour = current_hour;
        minute = current_minute + require_minute;
        if (minute >= 60)
        {
            hour += minute / 60;
            if (hour == 24)
            {
                hour = 0;
            }
            minute = minute % 60;
        }
        if (hour > 24) {
            hour = hour % 24;
        }
    } else {
        hour = current_hour;
        minute = current_minute + require_minute;
        if (minute >= 60)
        {
            hour += minute / 60;
            if (hour == 24)
            {
                hour = 0;
            }
            minute = minute % 60;
        }
        if (hour > 24) {
            hour = hour % 24;
        }
    }
    printf("%d %d\n", hour, minute);
    return 0;

}