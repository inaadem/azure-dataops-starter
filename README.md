# Azure Data Engineering & DataOps Project (Student Edition)

This project provides a practical, real-world template for deploying a modern data engineering and DataOps solution on Azure using Terraform. 
## Features
- **Infrastructure-as-Code (Terraform):**
  - Azure Data Lake Storage Gen2
  - Azure Data Factory
  - Azure SQL Database
  - Azure Storage Account
- **Sample Data Pipeline:**
  - Python ETL script to move and transform data
- **CI/CD for DataOps:**
  - GitHub Actions workflow for Terraform deployment and pipeline automation
- **Student Friendly:**
  - Clear documentation, comments, and folder structure
  - Visual diagrams and markdown visuals

## Quick Start
1. Clone this repo and open in VS Code.
2. Review the `infra/` folder for Terraform code.
3. Update variables in `infra/terraform.tfvars` as needed.
4. Run `terraform init` and `terraform apply` in the `infra/` folder to deploy Azure resources.
5. Review and run the sample ETL pipeline in `pipeline/`.
6. Check `.github/workflows/` for CI/CD automation.

## Folder Structure
- `infra/` - Terraform IaC for Azure
- `pipeline/` - Sample Python ETL pipeline
- `.github/workflows/` - CI/CD automation
- `docs/` - Diagrams and extra documentation

## Requirements
- Azure subscription (student credits work!)
- Terraform
- Python 3.8+

## Learn More
- [Azure for Students](https://azure.microsoft.com/en-us/free/students/)
- [Terraform Docs](https://www.terraform.io/docs/)
- [Azure Data Factory](https://docs.microsoft.com/en-us/azure/data-factory/)

---

> **Note:** This project is for learning and demonstration. Clean up resources after use to avoid unnecessary costs.
