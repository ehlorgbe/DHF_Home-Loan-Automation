# Dream Housing Finance Home Loan Approval Analysis  
**Author**: Elliot K. Hlorgbe  
 

---

## 📌 **Project Overview**  
**Objective**: Analyze loan approval trends for Dream Housing Finance to identify key drivers of loan decisions and support real-time automation of the approval process.  
**Dataset**: [Home Loan Approval Dataset](https://www.kaggle.com/datasets/prepinstaprime/home-loan-approval) (499 observations, 13 variables).  
**Tools**: IBM SPSS Statistics, Excel, Kaggle.  

---

## 🔍 **Key Findings**  
1. **Loan Approval Rate**: 68.3% of loans were approved.  
2. **Property Area Impact**: Semi-urban areas had the highest approval rate (44.6%).  
3. **Income-Loan Correlation**: Applicant income and loan amount showed a strong positive correlation (*r = 0.504, p < 0.001*).  
4. **Marital Status**: Married applicants requested significantly larger loan amounts (*p < 0.001*).  

---

## 📊 **Methodology & Analysis**  

### **1. Data Preprocessing**  
- **Missing Values**:  
  - Categorical variables: Rows with missing values removed.  
  - Numerical variables (e.g., `LoanAmount`): Imputed with mean values.  
- **Recoding**: Converted text-based variables (e.g., `Property_Area`) into numerical formats for analysis.  

---

### **2. Frequency Analysis**  
Examined categorical variables to identify dominant trends:  

**Table 1: Categorical Variable Distribution**  
| Variable          | Category      | Frequency | Percent (%) |  
|-------------------|---------------|-----------|-------------|  
| **Gender**        | Male          | 411       | 82.4        |  
|                   | Female        | 88        | 17.6        |  
| **Married**       | No            | 175       | 35.1        |  
|                   | Yes           | 324       | 64.9        |  
| **Education**     | Not Graduate  | 104       | 20.8        |  
|                   | Graduate      | 395       | 79.2        |  

**Insight**: Male applicants (82.4%) and graduates (79.2%) dominated the dataset.  
**[Insert Image 1: Bar chart showing gender vs. loan approval rate]**  

---

### **3. Descriptive Analysis**  
Summarized numerical variables to understand central tendencies and variability:  

**Table 2: Descriptive Statistics**  
| Variable             | Mean      | Std. Deviation | Min   | Max    |  
|----------------------|-----------|----------------|-------|--------|  
| Applicant Income     | $5,336    | $5,618         | 150   | 81,000 |  
| Loan Amount          | $144,735  | $78,957        | 9     | 600    |  

**Insight**: High variability in income suggests diverse applicant profiles.  
**[Insert Image 2: Boxplot of loan amounts by property area]**  

---

### **4. Correlation Analysis**  
Used **Spearman’s Rank-Order** correlation due to non-normal data distribution:  

**Table 3: Correlation Matrix**  
| Variables              | Applicant Income | Loan Amount | Loan Term |  
|------------------------|------------------|-------------|-----------|  
| **Applicant Income**   | 1                | 0.504***    | -0.038    |  
| **Loan Amount**        | -                | 1           | 0.036     |  

***p < 0.001*  

**Insight**: Income and loan amount are strongly correlated.  
**[Insert Image 3: Heatmap of correlations]**  

---

### **5. Chi-Square Test: Loan Status vs. Property Area**  
Tested independence between loan approval and property location:  
- **Result**: Significant association (*χ² = 13.948, p < 0.001*).  
- **Approval Rates**:  
  - Semi-urban: 44.6%  
  - Urban: 29.6%  
  - Rural: 25.8%  

**[Insert Image 4: Stacked bar chart of approval rates by property area]**  

---

### **6. Mann-Whitney U Test: Loan Amount by Marital Status**  
Compared loan amounts for married vs. unmarried applicants:  
- **Result**: Married applicants requested larger loans (*MWU = 21,513.5, p < 0.001*).  

---

### **7. Multiple Regression Analysis**  
Predicted `Loan_Amount` using key variables:  

**Table 4: Regression Results**  
| Variable          | Coefficient (β) | p-value  |  
|-------------------|-----------------|----------|  
| Dependents        | 8.600**         | 0.004    |  
| Applicant Income  | 0.007***        | <0.001   |  
| Credit History    | -2.712          | 0.744    |  

***R² = 0.313***  

**Insight**: Income and dependents significantly influence loan amounts.  

---

### **8. Logistic Regression: Loan Approval Predictors**  
Tested if `Self_Employed`, `ApplicantIncome`, and `Loan_Amount` predict approval:  
- **Result**: Model not significant (*Nagelkerke R² = 0.007, p = 0.463*).  
- **Key Trend**: Self-employed applicants had slightly lower approval odds (*OR = 0.897*).  

---

## 🚀 **Business Implications**  
1. **Target Semi-Urban Areas**: Prioritize marketing in semi-urban regions with higher approval rates.  
2. **Income-Driven Strategies**: Use income as a key criterion for loan amount decisions.  
3. **Credit History Focus**: Strengthen credit education programs for applicants with no credit history.  

---

## 📂 **GitHub Repository Structure**  
```plaintext
Loan-Approval-Analysis/  
├── Report/  
│   ├── Loan_Project_Report.pdf        # Final report  
├── Analysis_Scripts/  
│   ├── Data_Cleaning_Steps.docx       # SPSS/Excel workflows  
│   ├── Visualizations/                # Charts/Graphs  
├── README.md                          # Project overview  
