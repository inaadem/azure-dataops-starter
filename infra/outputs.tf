output "resource_group" {
  value = azurerm_resource_group.data_rg.name
}
output "datalake_account" {
  value = azurerm_storage_account.datalake.name
}
output "data_factory" {
  value = azurerm_data_factory.adf.name
}
output "sql_server" {
  value = azurerm_mssql_server.sql_server.name
}
output "sql_db" {
  value = azurerm_mssql_database.sqldb.name
}
