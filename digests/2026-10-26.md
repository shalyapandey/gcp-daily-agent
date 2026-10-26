# ☁️ Google Cloud Daily Briefing — October 26, 2026

## ⚡ Executive Summary
Found 2 updates across Google Cloud in the past 24 hours.

## 🛠️ Release Notes
### Cloud Database Migration Service
- **[Feature]**: You can now create heterogeneous conversion workspaces by importing database
schema metadata files from a Cloud Storage bucket without requiring direct
network connectivity between Database Migration Service and your source database during
the schema conversion phase. For more information, see the following pages: Create a conversion workspace for Oracle to Cloud SQL for PostgreSQL Createa a conversion workspace for Oracle to AlloyDB for PostgreSQL Createa a conversion workspace for SQL Server to Cloud SQL for PostgreSQL Createa a conversion workspace for SQL Server to AlloyDB for PostgreSQL [Doc](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace#use-cloud-storage) [Doc](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-conversion-workspace#use-cloud-storage) [Doc](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-conversion-workspace#use-cloud-storage) [Doc](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-conversion-workspace#use-cloud-storage)

### Model Armor
- **[Feature]**: Model Armor enforces the constraints/modelarmor.managed.requireTemplateDataResidencyCompliance managed
Organization Policy Service constraint by default. When you create or update a template,
this constraint prevents you from setting data_residency_compliant to false or clearing the Enforce data residency option unless an Organization Policy
Administrator disables the constraint. This feature is generally available
( GA ). For more
information, see Disable the organization policy constraint for data
residency . [Doc](https://cloud.google.com/products#product-launch-stages) [Doc](https://docs.cloud.google.com/model-armor/manage-templates#disable-data-residency-constraint)
