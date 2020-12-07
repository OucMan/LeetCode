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


## nlargest(n, iter)


## nsmallest(n, iter)
