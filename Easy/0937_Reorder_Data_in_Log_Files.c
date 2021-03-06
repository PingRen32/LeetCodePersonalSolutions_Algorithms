/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int cmpFunc(const char** a, const char** b) {
  int ptrA = 0, ptrB = 0;
  int sizeA = strlen(a[0]);
  int sizeB = strlen(b[0]);
  int cmpResult;
  while(a[0][ptrA] != ' ') ptrA++;
  ptrA++;
  while(b[0][ptrB] != ' ') ptrB++;
  ptrB++;

  if(isalpha(a[0][ptrA]) && isalpha(b[0][ptrB])) {
    cmpResult = strcmp(&a[0][ptrA], &b[0][ptrB]);
    if(!cmpResult) {
      return(strcmp(a[0], b[0]));
    }
    else {
      return cmpResult;
    }
  }
  else if(isalpha(a[0][ptrA])) {
    return -1;
  }
  else if(isalpha(b[0][ptrB])) {
    return 1;
  }
  else {
    return 0;
  }
}

char ** reorderLogFiles(char ** logs, int logsSize, int* returnSize){
  *returnSize = logsSize;
  qsort(logs, logsSize, sizeof(char*), cmpFunc);
  return logs;
}