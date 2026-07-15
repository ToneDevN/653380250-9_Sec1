#include <stdio.h>
#include <stdlib.h>

char getLastWeek() {

  char latest_week = '0';

  FILE *fp = popen("find . -maxdepth 1 -type d -name 'week*' | sort | tail "
                   "-n 1 | grep -o '.$'",
                   "r");
  if (fp != NULL) {
    latest_week = fgetc(fp);
  }
  pclose(fp);

  return latest_week;
}

void createNewWeek(char *week) {
  char command[256];
  snprintf(command, sizeof(command),
           "mkdir week%s && cd week%s && mkdir lab activity && touch "
           "lecture.md",
           week, week);
  printf("กำลัง Run command %s\n", command);
  int ret = system(command);
  if (ret == 0) {
    printf("สร้าง Directory สำหรับสัปดาห์ที่: %s เสร็จแล้ว\n", week);
  } else {
    printf("สร้าง Directory สำหรับสัปดาห์ที่: %s ไม่สำเร็จ\n", week);
  }
}

int main(int argc, char *argv[]) {

  char tree_command[64];
  if (argc > 1) {
    char *week = argv[1];
    createNewWeek(week);

    snprintf(tree_command, sizeof(tree_command), "tree -L 2 week%s", week);
    system(tree_command);

  } else {
    char latest_week = getLastWeek();
    if (latest_week != '0') {
      printf("สัปดาห์ล่าสุดคือ %c\n", latest_week);
      char next_week = (atoi(&latest_week)) + 1;
      printf("l");
      createNewWeek(&next_week);
    } else {
      printf("ไม่พบข้อมูล\n");
    }
  }

  return 0;
}