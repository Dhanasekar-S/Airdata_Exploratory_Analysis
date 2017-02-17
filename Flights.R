data1<- read.csv(file="DelayedFlights",sep=",",head=TRUE)
png("Flight1.png", width=600, height=600)
hist(data1$FlightNum,main="Frequency of Flight nos",xlab="Flight No")
dev.off()
png("Flight2.png", width=600, height=600)
hist(data1$Cancelled,main="Frequency of Cancelled Flights",xlab="Flight No")
hist(data1$Cancelled,main="Frequency of Cancelled Flights",xlab="Flight No")
dev.off()
png("Flight3.png", width=600, height=600)
boxplot(data1$ArrDelay,main='Arrival Delay BoxPlot',ylab='Arrival Delay')
dev.off()
png("Flight4.png", width=600, height=600)
boxplot(data1$DepDelay,main='Departure Delay BoxPlot',ylab='Departure Delay')
dev.off()
png("Flight5.png", width=600, height=600)
plot(data1$Distance,data1$WeatherDelay,
          main="Relationship Between Air Distance and WeatherDelay",
          xlab="Distance",
          ylab="Weather Delay")
dev.off()
png("Flight6.png", width=600, height=600)
plot(data1$Distance,data1$ArrDelay,
           main="Relationship Between Air Distance and Arrival Delay",
           xlab="Distance",
           ylab="Arrival Delay")
dev.off()

png("Flight7.png", width=600, height=600)
plot(data1$Distance,data1$AirTime,
                      main="Relationship Between Distance and Airtime",
                      xlab="Distance",
                      ylab="Airtime")
dev.off()
png("Flight8.png", width=600, height=600)
plot(data1$Distance,data1$SecurityDelay,
                      main="Relationship Between Distance and Security Delay",
                      xlab="Distance",
                      ylab="Security Delay")
dev.off()

png("Flight9.png", width=600, height=600)
plot(data1$Distance,data1$ActualElapsedTime,
                      main="Relationship Between Distance and ElapsedTime",
                      xlab="Distance",
                      ylab="Elapsed Time")
         
dev.off()
