Cutlets<-read.csv(file.choose())
attach(Cutlets)
View(Cutlets)
colnames(Cutlets) <- c("Unit_A","Unit_B")

View(Cutlets)
attach(Cutlets)

shapiro.test(Unit_A)
shapiro.test(Unit_B)

var.test(Unit_A,Unit_B)

#####Sample T Test#######

t.test(Unit_A,Unit_B,alternative = "two.sided",conf.level = 0.95,correct=TRUE)
?t.test
t.test(Unit_A,Unit_B,alternative = "greater")

####On-way ANOVA####

Cutlets1 <- read.csv(file.choose())
attach(Cutlets1)
View(Cutlets1)
stack_Cutlets1 <- stack(Cutlets1)
attach(stack_Cutlets1)
annova_results <- aov(values~ind,data = stack_Cutlets1)
summary(annova_results)

###proportional T Test #####

COF<-read.csv(file.choose())
View(COF)
attach(COF)

table1 <- table(Phillippines,Indonesia,Malta,India)
table1

?prop.test
prop.test(x=c(58,152),n=c(480,740),conf.level = 0.95,correct = FALSE,alternative = "two.sided")

###Unequal proportion

prop.test(x=c(58,152),n=c(480,740),conf.level = 0.95,correct = FALSE,alternative = "less")

#### Chi-squre Test####

BRO <- read.csv(file.choose())
View(BRO)
attach(BRO)
table(Observed.Values,East, West, North, South)

t2<-prop.table(table(East))
t3<-prop.table(table(West))
t4<-prop.table(table(North))
t5<-prop.table(table(South))
t1<-table(Observed.Values)

chisq.test(table(Observed.Values,East))
chisq.test(table(Observed.Values,West))
chisq.test(table(Observed.Values,North))
chisq.test(table(Observed.Values,South))

Fantaloons <- read.csv(file.choose())
View(Fantaloons)
attach(Fantaloons)

table4 <- table(Weekdays,Weekend)
table4

?prop.test
prop.test(x=c(58,152),n=c(480,740),conf.level = 0.95,correct = FALSE,alternative = "two.sided")

###Unequal proportion

prop.test(x=c(58,152),n=c(480,740),conf.level = 0.95,correct = FALSE,alternative = "less")

LabTAT <- read.csv(file.choose())
View(LabTAT)
attach(LabTAT)

table5 <- table(Laboratory.1,Laboratory.2,Laboratory.3,Laboratory.4)
table5

?prop.test
prop.test(x=c(58,152),n=c(480,740),conf.level = 0.95,correct = FALSE,alternative = "two.sided")

###Unequal proportion

prop.test(x=c(58,152),n=c(480,740),conf.level = 0.95,correct = FALSE,alternative = "less")
