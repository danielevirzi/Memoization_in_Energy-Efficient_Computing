############################### R SCRIPT ###################################

# Set working directory
setwd("/Users/danielevirzi/Desktop/GreenLab/Data_analysis")   # Set the working directory to the folder where the dataset is stored

# Import libraries
library(ggplot2)
library(dplyr)
library(plotly)
library(corrplot)
library(car)


############################### DATA PREPROCESSING ###############################


# Load dataset 
data <- read.csv("master.csv")

# Drop the unnecessary columns 
columns_to_remove<- c('Index', 'average_cpu_usage_quartile', 'average_memory_usage_quartile', 'average_energy_usage_quartile')
data <- data[, !(names(data) %in% columns_to_remove)]


# Show the first 6 rows of the dataset
head(data)

# Change the the cells where the name contains '_basic' with the name of the function
data$cache_strategy[data$cache_strategy == 'dijkstra_basic'] <- 'dijkstra'
data$cache_strategy[data$cache_strategy == 'fibonacci_basic'] <- 'fibonacci'
data$cache_strategy[data$cache_strategy == 'hessian_basic'] <- 'hessian'
data$cache_strategy[data$cache_strategy == 'knapsack_basic'] <- 'knapsack'
data$cache_strategy[data$cache_strategy == 'lemmatization_basic'] <- 'lemmatization'
data$cache_strategy[data$cache_strategy == 'pca_basic'] <- 'pca'

# Make new column called 'function_name' that contains the name of the function
data$function_name <- gsub("_cache", "", data$cache_strategy)
data$function_name <- gsub("_lru", "", data$function_name)

# Make new column called 'implementation' that contains the implementation of the function
data$implementation <- ifelse(data$cache_strategy %in% c('dijkstra', 'fibonacci', 'hessian', 'knapsack', 'lemmatization', 'unique_paths', 'edit_distance', 'tower_of_hanoi', 'reverse_string', 'DFT', 'merge_sort', 'pca', 'generate_permutations', 'floyd_warshall', 'convolve2d'),
                              'base',
                              ifelse(data$cache_strategy %in% c('dijkstra_cache', 'fibonacci_cache', 'hessian_cache', 'knapsack_cache', 'lemmatization_cache', 'unique_paths_cache', 'edit_distance_cache', 'tower_of_hanoi_cache', 'reverse_string_cache', 'DFT_cache', 'merge_sort_cache', 'pca_cache', 'generate_permutations_cache', 'floyd_warshall_cache', 'convolve2d_cache'),
                                     'cached', 'lru_cached'))

# Recursive are the 'implementation' that are in this list
Recursive <- c("unique_paths",
               "fibonacci",
               'edit_distance',
               'tower_of_hanoi',
               'knapsack',
               'reverse_string',
               'merge_sort')

# Create a new column called 'category' that contains the value 'Recursive' when the value of 'function_name' is in the list of Recursive functions and 'Non-Recursive' when the value of 'function_name' is not in the list of Recursive functions
data$category <- ifelse(data$function_name %in% Recursive, 'Recursive', 'Non-Recursive')


############################### EXPLORATORY DATA ANALYSIS ###############################

# Summary of the dataset
summary(data)


#### BOX PLOTS ####

## Grouped by 'implementation'

# Make box plots of 'execution_time' grouped by 'implementation' in log scale
ggplot(data, aes(x = implementation, y = execution_time, fill = implementation)) +
  geom_boxplot() +
  scale_y_log10() +
  labs(title = "Execution Time of Implementations", x = "Implementation", y = "Execution Time (log scale)") +
  theme(legend.position = "top") +
  theme(legend.title = element_blank()) +
  theme(legend.text = element_text(size = 8)) +
  theme(axis.text.x = element_text(size = 8)) +
  theme(axis.text.y = element_text(size = 8)) +
  theme(axis.title.x = element_text(size = 10)) +
  theme(axis.title.y = element_text(size = 10)) +
  theme(plot.title = element_text(size = 12))

# Make box plots of 'average_cpu_usage' grouped by 'implementation'
ggplot(data, aes(x = implementation, y = average_cpu_usage, fill = implementation)) +
  geom_boxplot() +
  labs(title = "Average CPU Usage of Implementations", x = "Implementation", y = "Average CPU Usage") +
  theme(legend.position = "top") +
  theme(legend.title = element_blank()) +
  theme(legend.text = element_text(size = 8)) +
  theme(axis.text.x = element_text(size = 8)) +
  theme(axis.text.y = element_text(size = 8)) +
  theme(axis.title.x = element_text(size = 10)) +
  theme(axis.title.y = element_text(size = 10)) +
  theme(plot.title = element_text(size = 12))

# Make box plots of 'memory_usage' grouped by 'implementation'
ggplot(data, aes(x = implementation, y = memory_usage, fill = implementation)) +
  geom_boxplot() +
  labs(title = "Average Memory Usage of Implementations", x = "Implementation", y = "Average Memory Usage") +
  theme(legend.position = "top") +
  theme(legend.title = element_blank()) +
  theme(legend.text = element_text(size = 8)) +
  theme(axis.text.x = element_text(size = 8)) +
  theme(axis.text.y = element_text(size = 8)) +
  theme(axis.title.x = element_text(size = 10)) +
  theme(axis.title.y = element_text(size = 10)) +
  theme(plot.title = element_text(size = 12))

# Make box plots of 'energy_consumption' grouped by 'implementation'
ggplot(data, aes(x = implementation, y = energy_consumption, fill = implementation)) +
  geom_boxplot() +
  labs(title = "Energy Consumption of Implementations", x = "Implementation", y = "Energy Consumption") +
  theme(legend.position = "top") +
  theme(legend.title = element_blank()) +
  theme(legend.text = element_text(size = 8)) +
  theme(axis.text.x = element_text(size = 8)) +
  theme(axis.text.y = element_text(size = 8)) +
  theme(axis.title.x = element_text(size = 10)) +
  theme(axis.title.y = element_text(size = 10)) +
  theme(plot.title = element_text(size = 12))



## Grouped by 'function_name' and 'implementation'

# Make box plots of 'execution_time' grouped by 'function_name' and 'implementation' in log scale 
ggplot(data, aes(x = function_name, y = execution_time, fill = implementation)) +
  geom_boxplot() +
  scale_y_log10() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(title = "Execution Time of Functions", x = "Function Name", y = "Execution Time (log scale)") +
  theme(legend.position = "top") +
  theme(legend.title = element_blank()) +
  theme(legend.text = element_text(size = 8)) +
  theme(axis.text.x = element_text(size = 8)) +
  theme(axis.text.y = element_text(size = 8)) +
  theme(axis.title.x = element_text(size = 10)) +
  theme(axis.title.y = element_text(size = 10)) +
  theme(plot.title = element_text(size = 12))

# Make box plots of 'average_cpu_usage' grouped by 'function_name' and 'implementation'
ggplot(data, aes(x = function_name, y = average_cpu_usage, fill = implementation)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(title = "Average CPU Usage of Functions", x = "Function Name", y = "Average CPU Usage") +
  theme(legend.position = "top") +
  theme(legend.title = element_blank()) +
  theme(legend.text = element_text(size = 8)) +
  theme(axis.text.x = element_text(size = 8)) +
  theme(axis.text.y = element_text(size = 8)) +
  theme(axis.title.x = element_text(size = 10)) +
  theme(axis.title.y = element_text(size = 10)) +
  theme(plot.title = element_text(size = 12))

# Make box plots of 'energy_consumption' grouped by 'function_name' and 'implementation'
ggplot(data, aes(x = function_name, y = energy_consumption, fill = implementation)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(title = "Energy Consumption of Functions", x = "Function Name", y = "Energy Consumption") +
  theme(legend.position = "top") +
  theme(legend.title = element_blank()) +
  theme(legend.text = element_text(size = 8)) +
  theme(axis.text.x = element_text(size = 8)) +
  theme(axis.text.y = element_text(size = 8)) +
  theme(axis.title.x = element_text(size = 10)) +
  theme(axis.title.y = element_text(size = 10)) +
  theme(plot.title = element_text(size = 12))

# Make box plots of 'memory_usage' grouped by 'function_name' and 'implementation'
ggplot(data, aes(x = function_name, y = memory_usage, fill = implementation)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(title = "Memory Usage of Functions", x = "Function Name", y = "Memory Usage") +
  theme(legend.position = "top") +
  theme(legend.title = element_blank()) +
  theme(legend.text = element_text(size = 8)) +
  theme(axis.text.x = element_text(size = 8)) +
  theme(axis.text.y = element_text(size = 8)) +
  theme(axis.title.x = element_text(size = 10)) +
  theme(axis.title.y = element_text(size = 10)) +
  theme(plot.title = element_text(size = 12))


##### KDE PLOTS #####


# Plot the distribution of 'execution_time' grouped by 'function_name' and 'implementation' in log scale
ggplot(data, aes(x = execution_time, fill = implementation)) + geom_density(alpha = 0.5) +
  facet_wrap(~function_name) + 
  scale_x_log10() +
  theme_minimal() +
  labs(title = "Execution Time of Functions", x = "Function Name", y = "Execution Time (log scale)")

# Plot the distribution of 'average_cpu_usage' gropued by 'function_name' and 'implementation'
ggplot(data, aes(x = average_cpu_usage, fill = implementation)) + geom_density(alpha = 0.5) +
  facet_wrap(~function_name) + 
  theme_minimal() +
  labs(title = "Average CPU Usage of Functions", x = "Average CPU Usage", y = "Density")

# Plot the distribution of 'energy_consumption' grouped by 'function_name' and 'implementation' in log scale
ggplot(data, aes(x = energy_consumption, fill = implementation)) + geom_density(alpha = 0.5) +
  facet_wrap(~function_name) + 
  scale_x_log10() +
  theme_minimal() +
  labs(title = "Energy Consumption of Functions", x = "Energy Consumption (log scale)", y = "Density")

# Plot the distribution of 'memory_usage' grouped by 'function_name' and 'implementation'
ggplot(data, aes(x = memory_usage, fill = implementation)) + geom_density(alpha = 0.5) +
  facet_wrap(~function_name) + 
  theme_minimal() +
  labs(title = "Memory Usage of Functions", x = "Memory Usage", y = "Density")





# Plot the distribution of 'execution_time_1' by 'implementation' in log scale
ggplot(data, aes(x=execution_time_1, fill=implementation)) + 
  geom_density(color="black", alpha = 0.5) +
  scale_x_log10() +
  labs(title="Distribution of execution time of the first call by implementation",
       x="Execution time (log scale)",
       y="Density")


# Plot the distribution of 'execution_time_2' by 'implementation' in log scale
ggplot(data, aes(x=execution_time_2, fill=implementation)) + 
  geom_density(color="black", alpha = 0.5) +
  scale_x_log10() +
  labs(title="Distribution of execution time of the second call by implementation",
       x="Execution time (log scale)",
       y="Density")

# Plot the distribution of 'execution_time' by 'implementation' in log scale
ggplot(data, aes(x=execution_time, fill=implementation)) + 
  geom_density(color="black", alpha = 0.5) +
  scale_x_log10() +
  labs(title="Distribution of execution time of the whole run by implementation",
       x="Execution time (log scale)",
       y="Density")



# Show the distribution of 'execution_time' by 'category' in log scale
ggplot(data, aes(x=execution_time, fill=category)) + 
  geom_density(color="black") +
  labs(title="Execution Time Distribution", x="Execution Time", y="Density") + 
  scale_x_log10() +
  theme_minimal() + 
  facet_wrap(~category) +
  labs(fill="Category")

# Show the distribution of 'average_cpu_usage' by 'category'
ggplot(data, aes(x=average_cpu_usage, fill=category)) + 
  geom_density(color="black") +
  labs(title="Average CPU Usage Distribution", x="Average CPU Usage", y="Density") + 
  theme_minimal() + 
  facet_wrap(~category) +
  labs(fill="Category")

# Show the distribution of 'energy_consumption' by 'category' in log scale
ggplot(data, aes(x=energy_consumption, fill=category)) + 
  geom_density(color="black") +
  labs(title="Energy Consumption Distribution", x="Energy Consumption", y="Density") + 
  scale_x_log10() +
  theme_minimal() + 
  facet_wrap(~category) +
  labs(fill="Category")

# Show the distribution of 'memory_usage' by 'category'
ggplot(data, aes(x=memory_usage, fill=category)) + 
  geom_density(color="black") +
  labs(title="Memory Usage Distribution", x="Memory Usage", y="Density") + 
  theme_minimal() + 
  facet_wrap(~category) +
  labs(fill="Category")


##### 3D SCATTER PLOT #####

plot_ly(data, x = ~average_cpu_usage, y = ~energy_consumption, z = ~memory_usage, color = ~function_name, text = ~implementation, type = 'scatter3d', mode = 'markers')

plot_ly(data, x = ~average_cpu_usage, y = ~energy_consumption, z = ~memory_usage, color = ~implementation, text = ~function_name, type = 'scatter3d', mode = 'markers')


plot_ly(data, x = ~average_cpu_usage, y = ~energy_consumption, z = ~execution_time, color = ~function_name, text = ~implementation, type = 'scatter3d', mode = 'markers')

plot_ly(data, x = ~average_cpu_usage, y = ~energy_consumption, z = ~execution_time, color = ~implementation, text = ~function_name, type = 'scatter3d', mode = 'markers')



##### SCATTER PLOTS #####

# Plot the scatter plot of 'execution_time_1' vs 'energy_consumption' by 'function_name' and 'implementation'
ggplot(data, aes(x = execution_time_1, y = energy_consumption, color = implementation)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Execution Time 1 vs Energy Consumption", x = "Execution Time 1", y = "Energy Consumption") + 
  theme_minimal()

# Plot the scatter plot of 'execution_time_2' vs 'energy_consumption' by 'function_name' and 'implementation' 
ggplot(data, aes(x = execution_time_2, y = energy_consumption, color = implementation)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Execution Time 2 vs Energy Consumption", x = "Execution Time 2", y = "Energy Consumption") + 
  theme_minimal()

# Plot the scatter plot of 'execution_time' vs 'energy_consumption' by 'function_name' and 'implementation'
ggplot(data, aes(x = execution_time, y = energy_consumption, color = implementation)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Execution Time vs Energy Consumption", x = "Execution Time", y = "Energy Consumption") + 
  theme_minimal()

# Plot the scatter plot of 'execution_time' vs 'average_cpu_usage' by 'function_name' and 'implementation'
ggplot(data, aes(x = execution_time, y = average_cpu_usage, color = implementation)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Execution Time vs Average CPU Usage", x = "Execution Time", y = "Average CPU Usage") + 
  theme_minimal()

# Plot the scatter plot of 'execution_time' vs 'memory_usage' by 'function_name' and 'implementation'
ggplot(data, aes(x = execution_time, y = memory_usage, color = implementation)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Execution Time vs Memory Usage", x = "Execution Time", y = "Memory Usage") + 
  theme_minimal()

# Plot the scatter plot of 'average_cpu_usage' vs 'energy_consumption' by 'function_name' and 'implementation'
ggplot(data, aes(x = average_cpu_usage, y = energy_consumption, color = implementation)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Average CPU Usage vs Energy Consumption", x = "Average CPU Usage", y = "Energy Consumption") + 
  theme_minimal()

# Plot the scatter plot of 'average_cpu_usage' vs 'memory_usage' by 'function_name' and 'implementation'
ggplot(data, aes(x = average_cpu_usage, y = memory_usage, color = implementation)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Average CPU Usage vs Memory Usage", x = "Average CPU Usage", y = "Memory Usage") + 
  theme_minimal()

# Plot the scatter plot of 'energy_consumption' vs 'memory_usage' by 'function_name' and 'implementation'
ggplot(data, aes(x = energy_consumption, y = memory_usage, color = implementation)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Energy Consumption vs Memory Usage", x = "Energy Consumption", y = "Memory Usage") + 
  theme_minimal()


##### CORRELATION PLOTS #####

# Compute the correlation matrix
correlation_matrix <- cor(data[, c("execution_time", "average_cpu_usage", "energy_consumption", "memory_usage")])

# Plot the correlation matrix
corrplot(correlation_matrix, method = "color", type = "upper", addCoef.col = "black", tl.col = "black", tl.srt = 45, tl.cex = 0.8)



###################### STATISTICAL ANALYSIS ######################



##### ANOVA (NORMALITY ASSUMPTION) #####


# Perform an ANOVA test to compare the execution time of the first call between the different implementations
anova(lm(execution_time_1 ~ implementation, data = data))

#### NO SIGNIFICANT DIFFERENCE

# Perform an ANOVA test to compare the execution time of the second call between the different implementations
anova(lm(execution_time_2 ~ implementation, data = data))

#### REALLY SIGNIFICANT DIFFERENCE ≈99.9% CONFIDENCE


##### KRUSKAL-W ALLIS TEST (NO NORMALITY ASSUMPTION) #####

# Perform a Kruskal-Wallis test to compare the execution time of the first call between the different implementations
kruskal.test(execution_time_1 ~ implementation, data = data)

#### NO SIGNIFICANT DIFFERENCE

# Perform a Kruskal-Wallis test to compare the execution time of the second call between the different implementations
kruskal.test(execution_time_2 ~ implementation, data = data)

#### REALLY SIGNIFICANT DIFFERENCE ≈100% CONFIDENCE



##### WILCOXON RANK SUM TEST #####


# Small input
small <- data %>%
  filter(size_of_input == "small")

small_base <- small %>%
  filter(implementation == "base")

small_cached <- small %>%
  filter(implementation == "cached")

small_lru_cached <- small %>%
  filter(implementation == "lru_cached")


# Medium input
medium <- data %>%
  filter(size_of_input == "medium")

medium_base <- medium %>%
  filter(implementation == "base")

medium_cached <- medium %>%
  filter(implementation == "cached")

medium_lru_cached <- medium %>%
  filter(implementation == "lru_cached")


# Large input
large <- data %>%
  filter(size_of_input == "large")

large_base <- large %>%
  filter(implementation == "base")

large_cached <- large %>%
  filter(implementation == "cached")

large_lru_cached <- large %>%
  filter(implementation == "lru_cached")


### ALL THE FUNCTIONS ###


## BASE vs CACHED ##

# Performa a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the small input
wilcox.test(small_base$energy_consumption, small_cached$energy_consumption, alternative = "greater")

# Performa a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the medium input
wilcox.test(medium_base$energy_consumption, medium_cached$energy_consumption, alternative = "greater")

# Performa a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the large input
wilcox.test(large_base$energy_consumption, large_cached$energy_consumption, alternative = "greater")


## BASE vs LRU_CACHED ##

# Performa a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the small input
wilcox.test(small_base$energy_consumption, small_lru_cached$energy_consumption, alternative = "greater")

# Performa a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the medium input
wilcox.test(medium_base$energy_consumption, medium_lru_cached$energy_consumption, alternative = "greater")

# Performa a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the large input
wilcox.test(large_base$energy_consumption, large_lru_cached$energy_consumption, alternative = "greater")




### SPECIFIC FUNCTIONS ###


## 1) DFT function

dft <- data %>%
  filter(function_name == "DFT")

dft_base <- dft %>%
  filter(implementation == "base")

dft_cached <- dft %>%
  filter(implementation == "cached")

dft_lru_cached <- dft %>%
  filter(implementation == "lru_cached")


# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the DFT function
wilcox.test(dft_base$energy_consumption, dft_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the DFT function
wilcox.test(dft_base$energy_consumption, dft_lru_cached$energy_consumption, alternative = "greater")



## 2) merge_sort function

merge_sort <- data %>%
  filter(function_name == "merge_sort")

merge_sort_base <- merge_sort %>%
  filter(implementation == "base")

merge_sort_cached <- merge_sort %>%
  filter(implementation == "cached")

merge_sort_lru_cached <- merge_sort %>%
  filter(implementation == "lru_cached")


# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the merge_sort function
wilcox.test(merge_sort_base$energy_consumption, merge_sort_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the merge_sort function
wilcox.test(merge_sort_base$energy_consumption, merge_sort_lru_cached$energy_consumption, alternative = "greater")


## 3) pca function

pca <- data %>%
  filter(function_name == "pca")

pca_base <- pca %>%
  filter(implementation == "base")

pca_cached <- pca %>%
  filter(implementation == "cached")

pca_lru_cached <- pca %>%
  filter(implementation == "lru_cached")



# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the pca function
wilcox.test(pca_base$energy_consumption, pca_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the pca function
wilcox.test(pca_base$energy_consumption, pca_lru_cached$energy_consumption, alternative = "greater")


## 4) generate_permutation function

generate_permutation <- data %>%
  filter(function_name == "generate_permutations")

generate_permutation_base <- generate_permutation %>%
  filter(implementation == "base")

generate_permutation_cached <- generate_permutation %>%
  filter(implementation == "cached")

generate_permutation_lru_cached <- generate_permutation %>%
  filter(implementation == "lru_cached")



# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the generate_permutation function
wilcox.test(generate_permutation_base$energy_consumption, generate_permutation_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the generate_permutation function
wilcox.test(generate_permutation_base$energy_consumption, generate_permutation_lru_cached$energy_consumption, alternative = "greater")


## 5) reverse_string function

reverse_string <- data %>%
  filter(function_name == "reverse_string")

reverse_string_base <- reverse_string %>%
  filter(implementation == "base")

reverse_string_cached <- reverse_string %>%
  filter(implementation == "cached")

reverse_string_lru_cached <- reverse_string %>%
  filter(implementation == "lru_cached")



# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the reverse_string function
wilcox.test(reverse_string_base$energy_consumption, reverse_string_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the reverse_string function
wilcox.test(reverse_string_base$energy_consumption, reverse_string_lru_cached$energy_consumption, alternative = "greater")    

#### SIGNIFICANT DIFFERENCE ≈95% CONFIDENCE



## 6) unique_paths function

unique_paths <- data %>%
  filter(function_name == "unique_paths")

unique_paths_base <- unique_paths %>%
  filter(implementation == "base")

unique_paths_cached <- unique_paths %>%
  filter(implementation == "cached")

unique_paths_lru_cached <- unique_paths %>%
  filter(implementation == "lru_cached")



# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the unique_paths function
wilcox.test(unique_paths_base$energy_consumption, unique_paths_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the unique_paths function
wilcox.test(unique_paths_base$energy_consumption, unique_paths_lru_cached$energy_consumption, alternative = "greater")


## 7) dijkstra function

dijkstra <- data %>%
  filter(function_name == "dijkstra")

dijkstra_base <- dijkstra %>%
  filter(implementation == "base")

dijkstra_cached <- dijkstra %>%
  filter(implementation == "cached")

dijkstra_lru_cached <- dijkstra %>%
  filter(implementation == "lru_cached")



# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the dijkstra function
wilcox.test(dijkstra_base$energy_consumption, dijkstra_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the dijkstra function
wilcox.test(dijkstra_base$energy_consumption, dijkstra_lru_cached$energy_consumption, alternative = "greater")


## 8) edit_distance function

edit_distance <- data %>%
  filter(function_name == "edit_distance")

edit_distance_base <- edit_distance %>%
  filter(implementation == "base")

edit_distance_cached <- edit_distance %>%
  filter(implementation == "cached")

edit_distance_lru_cached <- edit_distance %>%
  filter(implementation == "lru_cached")



# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the edit_distance function
wilcox.test(edit_distance_base$energy_consumption, edit_distance_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the edit_distance function
wilcox.test(edit_distance_base$energy_consumption, edit_distance_lru_cached$energy_consumption, alternative = "greater")


## 9) fibonacci function

fibonacci <- data %>%
  filter(function_name == "fibonacci")

fibonacci_base <- fibonacci %>%
  filter(implementation == "base")

fibonacci_cached <- fibonacci %>%
  filter(implementation == "cached")

fibonacci_lru_cached <- fibonacci %>%
  filter(implementation == "lru_cached")



# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the fibonacci function
wilcox.test(fibonacci_base$energy_consumption, fibonacci_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the fibonacci function
wilcox.test(fibonacci_base$energy_consumption, fibonacci_lru_cached$energy_consumption, alternative = "greater")

#### BOTH SIGNIFICANT DIFFERENCE ≈95% CONFIDENCE



## 10) floyd_warshall function

floyd_warshall <- data %>%
  filter(function_name == "floyd_warshall")

floyd_warshall_base <- floyd_warshall %>%
  filter(implementation == "base")

floyd_warshall_cached <- floyd_warshall %>%
  filter(implementation == "cached")

floyd_warshall_lru_cached <- floyd_warshall %>%
  filter(implementation == "lru_cached")


# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the floyd_warshall function
wilcox.test(floyd_warshall_base$energy_consumption, floyd_warshall_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the floyd_warshall function
wilcox.test(floyd_warshall_base$energy_consumption, floyd_warshall_lru_cached$energy_consumption, alternative = "greater")


## 11) tower_of_hanoi function

tower_of_hanoi <- data %>%
  filter(function_name == "tower_of_hanoi")

tower_of_hanoi_base <- tower_of_hanoi %>%
  filter(implementation == "base")

tower_of_hanoi_cached <- tower_of_hanoi %>%
  filter(implementation == "cached")

tower_of_hanoi_lru_cached <- tower_of_hanoi %>%
  filter(implementation == "lru_cached")



# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the tower_of_hanoi function
wilcox.test(tower_of_hanoi_base$energy_consumption, tower_of_hanoi_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the tower_of_hanoi function
wilcox.test(tower_of_hanoi_base$energy_consumption, tower_of_hanoi_lru_cached$energy_consumption, alternative = "greater")


## 12) hessian function

hessian <- data %>%
  filter(function_name == "hessian")

hessian_base <- hessian %>%
  filter(implementation == "base")

hessian_cached <- hessian %>%
  filter(implementation == "cached")

hessian_lru_cached <- hessian %>%
  filter(implementation == "lru_cached")



# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the hessian function
wilcox.test(hessian_base$energy_consumption, hessian_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the hessian function
wilcox.test(hessian_base$energy_consumption, hessian_lru_cached$energy_consumption, alternative = "greater")


##### SIGNIFICANT DIFFERENCE ≈95% CONFIDENCE



## 13) knapsack function

knapsack <- data %>%
  filter(function_name == "knapsack")

knapsack_base <- knapsack %>%
  filter(implementation == "base")

knapsack_cached <- knapsack %>%
  filter(implementation == "cached")

knapsack_lru_cached <- knapsack %>%
  filter(implementation == "lru_cached")



# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the knapsack function
wilcox.test(knapsack_base$energy_consumption, knapsack_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the knapsack function
wilcox.test(knapsack_base$energy_consumption, knapsack_lru_cached$energy_consumption, alternative = "greater")


## 14) lemmatization function

lemmatization <- data %>%
  filter(function_name == "lemmatization")

lemmatization_base <- lemmatization %>%
  filter(implementation == "base")

lemmatization_cached <- lemmatization %>%
  filter(implementation == "cached")

lemmatization_lru_cached <- lemmatization %>%
  filter(implementation == "lru_cached")



# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the lemmatization function
wilcox.test(lemmatization_base$energy_consumption, lemmatization_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the lemmatization function
wilcox.test(lemmatization_base$energy_consumption, lemmatization_lru_cached$energy_consumption, alternative = "greater")


## 15) convolve2d function

convolve2d <- data %>%
  filter(function_name == "convolve2d")

convolve2d_base <- convolve2d %>%
  filter(implementation == "base")

convolve2d_cached <- convolve2d %>%
  filter(implementation == "cached")

convolve2d_lru_cached <- convolve2d %>%
  filter(implementation == "lru_cached")


# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'cached' implementations for the convolve2d function
wilcox.test(convolve2d_base$energy_consumption, convolve2d_cached$energy_consumption, alternative = "greater")

# Perform a Wilcoxon rank sum test to compare the energy consumption between the 'base' and 'lru_cached' implementations for the convolve2d function
wilcox.test(convolve2d_base$energy_consumption, convolve2d_lru_cached$energy_consumption, alternative = "greater")





# Download the data
write.csv(data, "data.csv", row.names = FALSE)

