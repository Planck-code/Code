#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_FRAMES 10 // 最大物理块数
#define MAX_PAGES 50  // 最大逻辑页数

// 函数声明
void fifo(int pages[], int num_pages, int num_frames); // FIFO置换算法函数
void lru(int pages[], int num_pages, int num_frames);  // LRU置换算法函数
bool is_in_frame(int frames[], int num_frames, int page); // 检查页面是否在物理块中

int main() {
    int num_pages, num_frames;
    int pages[MAX_PAGES];

    // 输入逻辑页面数和物理块数
    printf("请输入逻辑页面数: ");
    scanf("%d", &num_pages);

    printf("请输入物理块数: ");
    scanf("%d", &num_frames);

    // 检查输入是否合法，防止超出限制
    if (num_frames > MAX_FRAMES || num_pages > MAX_PAGES) {
        printf("输入的页面数或物理块数超出限制！\n");
        return 1; // 退出程序
    }

    // 输入页面访问序列
    printf("请输入页面访问序列（以空格分隔，按Enter结束）: ");
    for (int i = 0; i < num_pages; i++) {
        scanf("%d", &pages[i]);
    }

    // 使用FIFO置换算法
    printf("\nFIFO置换算法:\n");
    fifo(pages, num_pages, num_frames);

    // 使用LRU置换算法
    printf("\nLRU置换算法:\n");
    lru(pages, num_pages, num_frames);

    return 0;
}

// 检查页面是否在物理块中
bool is_in_frame(int frames[], int num_frames, int page) {
    for (int i = 0; i < num_frames; i++) {
        if (frames[i] == page) { // 如果页面已经在物理块中
            return true;
        }
    }
    return false; // 页面不在物理块中，返回false
}

// FIFO置换算法
void fifo(int pages[], int num_pages, int num_frames) {
    int frames[MAX_FRAMES] = {-1}; // 初始化物理块，-1表示空闲
    int front = 0;                // 队列头指针，用于记录最早进入的页面
    int page_faults = 0;          // 缺页次数

    for (int i = 0; i < num_pages; i++) {
        int page = pages[i]; // 当前访问的页面
        if (!is_in_frame(frames, num_frames, page)) {
            // 如果页面不在物理块中，发生缺页
            frames[front] = page; // 替换最早进入的页面
            front = (front + 1) % num_frames; // 更新队列头指针，循环队列实现
            page_faults++; // 缺页次数加1
        }

        // 输出当前物理块内容
        printf("页面 %d -> [", page);
        for (int j = 0; j < num_frames; j++) {
            if (frames[j] != -1) {
                printf("%d ", frames[j]); // 输出已加载的页面
            } else {
                printf("  "); // 空闲块显示为空
            }
        }
        printf("]\n");
    }

    printf("FIFO 缺页次数: %d\n", page_faults);
}

// LRU置换算法
void lru(int pages[], int num_pages, int num_frames) {
    int frames[MAX_FRAMES];          // 初始化物理块
    int last_used[MAX_FRAMES];       // 最近使用时间
    int page_faults = 0;             // 缺页次数

    for (int i = 0; i < num_frames; i++) {
        frames[i] = -1;              // -1 表示物理块为空
        last_used[i] = -1;           // -1 表示没有使用过
    }

    for (int i = 0; i < num_pages; i++) {
        int page = pages[i];
        int found = -1;

        // 检查页面是否在物理块中
        for (int j = 0; j < num_frames; j++) {
            if (frames[j] == page) {
                found = j;           // 页面命中
                break;
            }
        }

        if (found == -1) {
            // 缺页，寻找最近最少使用的页面
            int lru_index = 0;
            for (int j = 1; j < num_frames; j++) {
                if (last_used[j] < last_used[lru_index]) {
                    lru_index = j;   // 找到最近最少使用页面的索引
                }
            }
            frames[lru_index] = page;  // 替换页面
            last_used[lru_index] = i; // 更新替换页面的最近使用时间
            page_faults++;
        } else {
            // 页面命中，更新最近使用时间
            last_used[found] = i;
        }

        // 输出当前物理块内容
        printf("页面 %d -> [", page);
        for (int j = 0; j < num_frames; j++) {
            if (frames[j] != -1) {
                printf("%d ", frames[j]);
            } else {
                printf("  ");
            }
        }
        printf("]\n");
    }

    printf("LRU 缺页次数: %d\n", page_faults);
}
