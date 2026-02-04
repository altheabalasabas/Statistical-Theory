U = c(3, -2, 5)
V = c(-4, -1, 6)

a = sum(U * V)
b = sum((U + 3) * (V - 4))
c = sum(V^2)
d = sum(U) * (sum(V))^2
e = sum(U * V^2)
f = sum(U^2 - 2 * V^2 + 2)
g = sum(U / V)

results = data.frame(
  Part = c("a", "b", "c", "d", "e", "f", "g"),
  Value = c(a, b, c, d, e, f, g)
)
print(results)
