# Failure Scenarios

**Purpose:** Record expected behavior for future failure handling.

**Status:** Planned; no failure handling is implemented.

| Scenario | Expected Behavior | Status |
| --- | --- | --- |
| Duplicate file | Detect and avoid unintended duplicate processing. | Planned |
| Corrupted file | Reject safely and preserve diagnostic context. | Planned |
| Invalid schema | Route for review without publishing invalid data. | Planned |
| Empty file | Detect and classify according to a future policy. | Planned |
| Concurrent files | Process concurrent arrivals without data loss or conflicts. | Planned |
| Glue failure | Record failure and support controlled retry or reprocessing. | Planned |
| Snowflake load failure | Preserve input and expose the load failure for recovery. | Planned |
