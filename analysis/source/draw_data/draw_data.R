library(yaml)
library(MASS)

CONFIG <- yaml.load_file("config_global.yaml")

main <- function() {
  simga <- matrix(c(1,.5,.5,1),2,2)
  mean <- rep(0, 2)
  draw <-mvrnorm(10000, mean, simga)
  write.table(draw, sprintf("%s/data.csv", CONFIG$build$draw_data), sep=",",
              row.names = FALSE, col.names = FALSE, quote = FALSE)
}
main()