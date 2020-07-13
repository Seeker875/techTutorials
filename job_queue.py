# python3

from collections import namedtuple


AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
## creating a worker class
worker = namedtuple("worker", ["thread", "jobTime"])

#shift down modified to sort by process time
def shiftDown(data,idx):
    '''
    input i position as input
    Shifts down an element maintaining heap str
    '''
    size= len(data) -1
    while idx<=(size//2):
        minIdx = idx

        # -1 for zero based idx
        leftChild = 2*idx+1
        rightChild = 2*idx+2
        #print(f'leftChild  {leftChild}') # 
       
        #
        
        if  leftChild <= size:
            leftWorker = data[leftChild]
            minWorker = data[minIdx]
            if leftWorker.jobTime < minWorker.jobTime:
                 minIdx = leftChild
            elif leftWorker.jobTime == minWorker.jobTime:   
                if leftWorker.thread <  minWorker.thread:
                    minIdx = leftChild
         


        if  rightChild <= size:
            rightWorker = data[rightChild]
            minWorker = data[minIdx]
            if rightWorker.jobTime < minWorker.jobTime:
                minIdx= rightChild
            elif rightWorker.jobTime == minWorker.jobTime:   
                if rightWorker.thread <  minWorker.thread:
                    minIdx = rightChild

        if  minIdx !=idx:
            
            data[idx], data[minIdx] = data[minIdx], data[idx]
        
            idx=minIdx
        else:
            break;
            

    return data   

def assign_jobs(n_workers, jobs):
#    # TODO: replace this code with a faster algorithm.
#    result = []
#
#    next_free_time = [0] * n_workers
#    for job in jobs:
#        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
#        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
#        next_free_time[next_worker] += job
#
#    return result

    
    result = []
    workerList=[]
    # initiating with job time as zero
    next_free_time = [0] * n_workers
    for i in range(n_workers):
        #Giving workers a thread and job time
        workerList.append(worker(i,0))
    for job in jobs:
        next_worker = workerList.pop(0) 
       # next_worker = workerList[0] 

        result.append(AssignedJob(next_worker.thread,next_worker.jobTime))
        #keeping the thread same and inserting current job time
        # insering at the top of heapq
        next_free_time[next_worker.thread] += job
        workerList.insert(0,worker(next_worker.thread, next_free_time[next_worker.thread] ))
      # Immutable named tuple, cant set attribute erro
       # next_worker.jobTime+ = job
        #next_worker._replace(jobTime=next_worker.jobTime+job)

        #workerList[0] =  next_worker
        workerList=shiftDown(workerList,0)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
