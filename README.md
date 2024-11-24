# customer-segmentation
Clustering project to segment customers based on price sensitivity and purchasing behaviour for effective pricing strategies.
# Harnessing Price Sensitivity for Effective Customer Segmentation with K-Means Clustering

## Overview
This project explores customer segmentation using **K-Means Clustering** to analyse **price sensitivity** and **purchasing behavior**. By dividing customers into distinct segments, businesses can craft more effective pricing strategies and improve overall customer satisfaction.

For more details, check out:
- The full [Medium article](https://medium.com/@cynthiaakiotu/harnessing-price-sensitivity-for-effective-customer-segmentation-with-k-means-clustering-c08ccc2a5e6e).
- The complete [YouTube video walkthrough](https://youtu.be/Rt7ySuJcuA4?si=NoMVjV9ziadJydLh).


---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Cluster Insights and Strategies](#cluster-insights-and-strategies)
- [How to Use](#how-to-use)
- [Folder Structure](#folder-structure)
- [Blog Post](#blog-post)
- [Video Walkthrough](#video-walkthrough)
- [License](#license)


---

## Features
- Cluster customers into distinct groups based on purchasing behavior.
- Analyse metrics such as unit price, total sales, and quantity purchased.
- Determine the optimal number of clusters using:
  - **Elbow Method**
  - **Silhouette Scores**
  - **Davies-Bouldin Index**
- Provide actionable insights for improving pricing strategies.

---

## Dataset
- **Source:** Proprietary data.
- **Key Features:**
  - `UnitPrice`: Price per unit of a product.
  - `TotalSales`: Total monetary value of sales per customer.
  - `Quantity`: Total number of items purchased.
  - Any other relevant features used for clustering.

---

## Methodology
1. **Exploratory Data Analysis (EDA):**
   - Identified outliers and visualised feature distributions.
2. **Data Preprocessing:**
   - Scaled features using **StandardScaler** to ensure uniformity.
   - Selected relevant features (`UnitPrice`, `TotalSales`) for clustering.
3. **Clustering:**
   - Used **K-Means Clustering** to group customers into distinct segments.
   - Determined the optimal number of clusters using:
     - **Elbow Method**: To analyse the inertia curve.
     - **Silhouette Method**: To measure intra-cluster cohesion and inter-cluster separation.
     - **Davies-Bouldin Index**: To evaluate cluster compactness and separation.
4. **Visualisation:**
   - Visualised customer clusters using scatterplots.
   - Analysed cluster characteristics (e.g., average sales, unit price).

---

## Cluster Insights and Strategies

This section outlines the key characteristics of each customer cluster and tailored strategies to effectively engage and maximize value from these segments.

---

### **Cluster 0 Purple Group (Price-Sensitive Customers)**
- **Characteristics**: 
  - Largest cluster, comprising 1,866 customers.
  - Prefer lower-priced items (average unit price: 2.25).
  - Moderate purchase quantities (average: 363.23 items) and low total sales (average: 490.76).
  - Exhibit strong price sensitivity, favoring affordability and frequent transactions but prone to returns.

- **Sales Strategies**:
  - Implement regular discounts and promotions to attract them.
  - Introduce loyalty programs with rewards for frequent purchases.
  - Create value bundles or packs to encourage bulk buying.
  - Highlight cost savings and value in marketing campaigns.
  - Ensure clear return policies and address issues with products/services proactively.

---

### **Cluster 1 Teal Group (Balanced Customers)**
- **Characteristics**: 
  - Comprises 737 customers who prefer mid-priced items (average unit price: 3.04).
  - High purchase quantities (average: 1,229.76 items) and significant total sales (average: 2,164.64).
  - Strikes a balance between price sensitivity and purchase volume, contributing substantially to total sales.

- **Sales Strategies**:
  - Offer bulk discounts and tiered pricing models to encourage larger purchases.
  - Provide exclusive deals and early access to promotions for customer retention.
  - Use personalised marketing campaigns that emphasise both value and quantity.
  - Highlight the cost-effectiveness of purchases in communications.

---

### **Cluster 2 Yellow Group (Quality-Oriented Customers)**
- **Characteristics**: 
  - Comprises customers who prefer premium, higher-priced items (average unit price: 4.36).
  - Lower purchase quantities (average: 244.55 items) and moderate total sales (average: 555.86).
  - Willing to pay more for quality and exclusivity, valuing premium experiences.

- **Sales Strategies**:
  - Market premium products by emphasising quality, uniqueness, and exclusivity.
  - Develop loyalty programs offering exclusive benefits (e.g., first access to products, special events).
  - Enhance customer experience with exceptional service, premium packaging, and seamless online/offline shopping.
  - Highlight the unique features of products in marketing efforts to attract and retain this segment.

---

By tailoring strategies to each cluster, businesses can maximise engagement, enhance customer satisfaction, and drive sustainable growth.

### Key Visualizations
1. **Customer Segmentation:**
   ![Customer Segmentation](results/figures/customer_segmentation.png)

2. **Optimal K Determination:**
   ![Optimal K Methods](results/figures/optimal_k_methods.png)

3. **Cluster Characteristics:**
   ![Cluster Analysis Summary](results/figures/cluster_analysis_summary.png)

---

## How to Use
1. **Clone the repository:**
   ```bash
   git clone https://github.com/CynthiaTheDataTechie/customer-segmentation.git
   cd customer_segmentation
pip install -r requirements.txt
jupyter notebook Harnessing_Price_Sensitivity_for_Effective_Customer_Segmentation_with_K_Means_Clustering.ipynb
## Folder Structure

customer_segmentation/
├── src/                     # Reusable Python scripts
│   ├── data_preprocessing.py
│   ├── clustering.py
│   ├── visualization.py
│   ├── README.md
├── results/                 # Analysis outputs
│   ├── figures/             # Saved plots and visualisations
│   ├── README.md
├── Harnessing_Price_Sensitivity_for_Effective_Customer_Segmentation_with_K_Means_Clustering.ipynb  # Main notebook
├── requirements.txt         # Python dependencies
├── LICENSE                  # License for the project
├── README.md                # Main README


---

## Blog Post

This project is detailed in a comprehensive blog post that covers:
- Step-by-step methodologies for clustering and segmentation.
- How to use evaluation metrics like the Elbow Method and Silhouette Score.
- Visualisations and insights into customer purchasing behavior.

Read the full blog post here:

[Harnessing Price Sensitivity for Effective Customer Segmentation with K-Means Clustering](https://medium.com/@cynthiaakiotu/harnessing-price-sensitivity-for-effective-customer-segmentation-with-k-means-clustering-c08ccc2a5e6e)

---

## Video Walkthrough

Watch the complete walkthrough of the project, including methodologies, results, and visualisations, in the video:

[![YouTube Video](https://img.youtube.com/vi/Rt7ySuJcuA4&t=1256s/0.jpg)](https://youtu.be/Rt7ySuJcuA4?si=NoMVjV9ziadJydLh)

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.





