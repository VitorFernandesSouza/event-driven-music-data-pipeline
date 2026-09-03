# Architecture Decision Records

**Purpose:** Record architectural decisions as the project evolves.

**Status:** Initial placeholder; decisions will be added in future phases.

## ADR-001: Event-driven ingestion architecture

**Status:** Accepted

**Decision:** Use Amazon S3 ObjectCreated events to initiate the ingestion workflow.

**Reason:** Reduce manual intervention and demonstrate event-driven data engineering.
