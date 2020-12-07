# 使用需要导入包

```Python
import heapq
```

# API

## heappush(heap, x)

将x压入堆中

```Python
import heapq
heap = []
for i in range(10, -1, -1):
    heapq.heappush(heap, i)
print(heap)
```

## heappop(heap)

从堆中弹出最小的元素
```Python
import heapq
heap = list(range(9, -1, -1))
heapq.heapify(heap)   # 将列表转变为符合堆特征的结构
for i in range(10):
    print(heapq.heappop(heap))
```


## heapify(heap)

让列表具备堆特征

```Python
import heapq
heap = list(range(9, -1, -1))
print(heap) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
heapq.heapify(heap)
print(heap) # [0, 1, 3, 2, 5, 4, 7, 9, 6, 8]

```

## heapreplace(heap, x)

弹出最小的元素，并将x压入堆中，相当于执行了一次heappop(heap)，接着执行了一次和heappush(heap, x)

```Python
import heapq
heap = list(range(9, -1, -1))
print(heap) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
heapq.heapify(heap) 
heapq.heapreplace(heap, 10)
print(heap) # [1, 2, 3, 6, 5, 4, 7, 9, 10, 8]
```

## nlargest(n, iter)

返回iter中n个最大的元素
```Python
import heapq
heap = list(range(9, -1, -1))
heapq.heapify(heap)
print(heapq.nlargest(3, heap))
```

## nsmallest(n, iter)

返回iter中n个最小的元素
```Python
import heapq
heap = list(range(9, -1, -1))
heapq.heapify(heap)
print(heapq.nsmallest(3, heap))
```

# 注意

heapq实现的是小顶堆，要是实现大顶堆，可以将元素取相反数，原数的大顶堆就是相反数的小顶堆


