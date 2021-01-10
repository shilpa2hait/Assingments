Cutlets<-read.csv(file.choose())
attach(Cutlets)
View(Cutlets)
colnames(Cutlets) <- c("Unit_A","Unit_B")

View(Cutlets)
attach(Cutlets)

shapiro.test(Unit_A)
shapiro.test(Unit_B)

var.test(Unit_A,Unit_B)

t.test(Unit_A,Unit_B,alternative = "two.sided",conf.level = 0.95,correct=TRUE)
?t.test
t.test(Unit_A,Unit_B,alternative = "greater")