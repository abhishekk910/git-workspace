package main

import (  
    "fmt"
    "math/rand"
    "sync"
    "time"
)

type Job struct {  
    id       int
    randomNumber int
}

type Result struct {  
    job         Job
    sumofdigits int
}

var jobs = make(chan Job, 10)  
var results = make(chan Result, 10)

func digits(number int) int {  
    sum := 0
    num := number
    for num != 0 {
        digit := num % 10
        sum += digit
        num = num/10
    }
    time.Sleep(2 * time.Second)
    return sum
}

func worker(wg *sync.WaitGroup) {  
    for job := range jobs {
        output := Result{job, digits(job.randomNumber)}
        results <- output
    }
    wg.Done()
}

func createWorkerPool(noOfWorkers int) {  
    var wg sync.WaitGroup
    for i := 0; i < noOfWorkers; i++ {
        wg.Add(1)
        go worker(&wg)
    }
    wg.Wait()
    close(results)
}

func allocate(noOfJobs int) {  
    for i := 0; i < noOfJobs; i++ {
        randomNumber := rand.Intn(999)
        job := Job{i, randomNumber}
        jobs <- job
    }
    close(jobs)
}

func result(ch chan bool) {  
    for result := range results {
        fmt.Printf("Job id %d, input random no %d , sum of digits %d\n", result.job.id, result.job.randomNumber, result.sumofdigits)
    }
    ch <- true
}

func main() {  
    startTime := time.Now()
    noOfJobs := 20 
    go allocate(noOfJobs)
    ch := make(chan bool)
    go result(ch)
    noOfWorkers := 2 
    createWorkerPool(noOfWorkers)
    <-ch 
    endTime := time.Now()
    diff := endTime.Sub(startTime)
    fmt.Println("total time taken ", diff.Seconds(), "seconds")
}