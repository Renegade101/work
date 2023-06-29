SELECT A.Id
FROM Weather AS A, Weather AS B
WHERE DATEADD(day, -1, A.recordDate) = B.recordDate AND A.Temperature> B.Temperature

---SELECT A.id
---FROM Weather A INNER JOIN Weather B ON A.id = B.id+1
---WHERE A.temperature > B.temperature