# Planned Architecture

**Purpose:** Document the target organization of the platform.

**Status:** Initial structure only. This document will be expanded in future implementation phases.

The current implementation target is local. AWS and Snowflake are future architecture options and are not part of the active repository structure.

| Component | Planned responsibility |
| --- | --- |
| Public sources | Provide music-related files; exact sources are to be defined. |
| S3 Raw | Retain source inputs in the data lake. |
| S3 ObjectCreated | Emit an event for new objects. |
| Lambda | Inspect the event and initiate processing. |
| AWS Glue/PySpark | Validate, transform, and classify input data. |
| S3 Curated | Store validated downstream-ready data. |
| Snowflake | Provide warehouse storage and query access. |
| dbt | Build analytical transformations and tests. |
| Power BI | Consume analytical models for reporting. |

Implementation details, permissions, retries, and infrastructure provisioning remain planned.
