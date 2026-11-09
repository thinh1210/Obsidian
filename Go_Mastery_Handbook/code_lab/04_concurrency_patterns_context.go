package main

import (
	"context"
	"fmt"
	"runtime"
	"sync"
	"time"
)

type Job struct {
	ID       int
	Duration time.Duration
}

type Result struct {
	JobID    int
	WorkerID int
	Output   int
	Err      error
}

func runBoundedWorkerPool(ctx context.Context, numWorkers int, jobs []Job) []Result {
	jobCh := make(chan Job, len(jobs))
	for _, j := range jobs {
		jobCh <- j
	}
	close(jobCh)

	resultCh := make(chan Result, len(jobs))
	var wg sync.WaitGroup

	for w := 1; w <= numWorkers; w++ {
		wg.Add(1)
		go func(workerID int) {
			defer wg.Done()
			for {
				select {
				case <-ctx.Done():
					return
				case job, ok := <-jobCh:
					if !ok {
						return
					}
					// Mô phỏng xử lý công việc có lắng nghe tín hiệu hủy từ Context
					timer := time.NewTimer(job.Duration)
					select {
					case <-ctx.Done():
						timer.Stop()
						resultCh <- Result{JobID: job.ID, WorkerID: workerID, Err: ctx.Err()}
						return
					case <-timer.C:
						resultCh <- Result{JobID: job.ID, WorkerID: workerID, Output: job.ID * 10}
					}
				}
			}
		}(w)
	}

	// Đóng kênh kết quả ngay khi toàn bộ Worker đã thoát an toàn
	wg.Wait()
	close(resultCh)

	var results []Result
	for res := range resultCh {
		results = append(results, res)
	}
	return results
}

func main() {
	fmt.Println("=== [LAB 04] BOUNDED WORKER POOL & CONTEXT CANCELLATION (0 GOROUTINE LEAK) ===")

	baseGoroutines := runtime.NumGoroutine()
	fmt.Printf("  • Số Goroutine ban đầu                  : %d\n", baseGoroutines)

	// Tạo 6 jobs (3 jobs đầu mất 10ms, 3 jobs sau mất 200ms) nhưng đặt Timeout tổng là 45ms
	jobs := []Job{
		{ID: 1, Duration: 10 * time.Millisecond},
		{ID: 2, Duration: 10 * time.Millisecond},
		{ID: 3, Duration: 10 * time.Millisecond},
		{ID: 4, Duration: 200 * time.Millisecond},
		{ID: 5, Duration: 200 * time.Millisecond},
		{ID: 6, Duration: 200 * time.Millisecond},
	}

	ctx, cancel := context.WithTimeout(context.Background(), 45*time.Millisecond)
	defer cancel()

	results := runBoundedWorkerPool(ctx, 3, jobs)
	for _, r := range results {
		if r.Err != nil {
			fmt.Printf("    [Job #%d | Worker %d] HỦY SỚM DO TIMEOUT: %v\n", r.JobID, r.WorkerID, r.Err)
		} else {
			fmt.Printf("    [Job #%d | Worker %d] HOÀN THÀNH: Output = %d\n", r.JobID, r.WorkerID, r.Output)
		}
	}

	afterGoroutines := runtime.NumGoroutine()
	fmt.Printf("  • Số Goroutine sau khi Pool kết thúc    : %d (Rò rỉ Goroutine = %v)\n",
		afterGoroutines, afterGoroutines > baseGoroutines)
}
