variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "student-dataops-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "westeurope"
}

variable "datalake_name" {
  description = "Name of the Data Lake Storage account (leave blank to auto-generate)"
  type        = string
  default     = ""
}

variable "data_factory_name" {
  description = "Name of the Data Factory"
  type        = string
  default     = "student-adf"
}

variable "sql_server_name" {
  description = "Name of the SQL Server"
  type        = string
  default     = "studentsqlsrv"
}

variable "sql_admin_user" {
  description = "SQL admin username"
  type        = string
  default     = "sqladminuser"
}

variable "sql_admin_password" {
  description = "SQL admin password"
  type        = string
  sensitive   = true
}

variable "sql_db_name" {
  description = "Name of the SQL Database"
  type        = string
  default     = "studentdb"
}

resource "random_integer" "suffix" {
  min = 10000
  max = 99999
}
