# ☁️ Google Cloud Daily Briefing — November 09, 2026

## ⚡ Executive Summary
Found 8 updates across Google Cloud in the past 24 hours.

## 🛠️ Release Notes
### AI Hypercomputer
- **[Feature]**: Generally available : Pathways on Cloud is now generally available on Google Kubernetes Engine (GKE). Major features include
the following: Single-controller execution model : Coordinate multi-slice and multi-host
Cloud TPU workloads from a single Python client process. Pathways uses
asynchronous dispatch and centralized scheduling to support both Single
Program, Multiple Data (SPMD) and Multiple Program, Multiple Data (MPMD)
workloads. For example, training and reinforcement learning (RL) loops. Resilient and elastic training : Keep training jobs running across hardware
interruptions with resilient training ,
including the following capabilities: Elastic training :
Dynamically scale down to healthy Cloud TPU slices during unplanned
hardware failures and scale back up when replacement slices rejoin without
restarting the entire job. Suspend-resume : Automatically save and restore high-bandwidth memory
(HBM) state to Cloud Storage during planned GKE preemption
events. Hot-swapping : Remap interrupted workloads onto standby or lower-priority
Cloud TPU slices. Colocated Python sidecar containers :
Run custom Python code directly on Cloud TPU host VMs alongside
Pathways workers. For example, multi-host data loading with Grain or RemoteIterator , and distributed
asynchronous checkpointing with Orbax . Interactive mode and Shared Pathways Service : Run, inspect, and debug JAX
workloads interactively from a notebook or terminal using interactive mode ,
or share a long-running pool of Cloud TPU slices on demand across
multiple users and jobs with the Shared Pathways Service . Cluster Director, Cluster Toolkit, and GKE integration :
Launch JAX workloads on the Pathways runtime using Cluster Director or Cluster Toolkit ( gcluster with --pathways and --pathways-headless ), or by deploying
Kubernetes JobSet manifests on GKE. pathwaysutils utility package : Use the pathwaysutils Python
package for advanced features such as the Shared Pathways Service, elasticity ,
and experimental.reshard for device-side data transfers across hosts over Inter-Chip Interconnect (ICI)
or Data Center Network (DCN). Standard libtpu.so layering and custom libtpu.so support : Pathways is
layered over the standard libtpu.so shared library and provides a way to
dynamically link in a user-provided libtpu.so at runtime using PathwaysJobSet.with_custom_libtpu in pathwaysutils . Single-process profiling, observability, and compilation cache : Capture
end-to-end JAX profiler traces across the client, proxy, resource manager, and
Cloud TPU hosts from a single process. Reuse compiled XLA modules
with a persistent compilation cache on Cloud Storage, and view
Pathways control and data plane metrics in Cloud Monitoring. Agentic workload debugging : Troubleshoot failed, crashing, or stalled
Pathways workloads on GKE using the pathways-workload agent skill .
With this skill, AI agents can inspect Cloud Logging container logs, node
kernel logs, and GKE events to help identify root causes and
fixes. Supported Cloud TPU versions, JAX versions, and container images :
Supports TPU7x (Ironwood), TPU v6e (Trillium), TPU v5p, and TPU v5e for JAX
versions 0.12.0.1, 0.12.0, 0.11.2, 0.11.1, 0.11.0, 0.10.2, and 0.10.1, with
container images published in Artifact Registry: Image locations : Pathways resource manager and worker : us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/server: TAG IFRT proxy server : us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/proxy_server: TAG Colocated Python sidecar : us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/colocated_python_sidecar: TAG Image tags : Replace TAG with one of the
following tags, which are created automatically when a Pathways build
passes qualification tests and is promoted to production: YYYYMMDD -jax_ JAX_VERSION :
Pinned tag created by combining the UTC promotion date
( YYYYMMDD ) with -jax_ and the verified
JAX version ( JAX_VERSION ) after
per-version qualification tests pass. For example, 20261108-jax_0.12.0.1 . jax- JAX_VERSION : Rolling tag updated
after per-version qualification tests pass to point to the most recent
verified image for that JAX release. For example, jax-0.12.0.1 or jax-0.12.0 . latest : Rolling tag updated when a build passes qualification tests
against the most recent supported JAX release. Elastic training :
Dynamically scale down to healthy Cloud TPU slices during unplanned
hardware failures and scale back up when replacement slices rejoin without
restarting the entire job. Suspend-resume : Automatically save and restore high-bandwidth memory
(HBM) state to Cloud Storage during planned GKE preemption
events. Hot-swapping : Remap interrupted workloads onto standby or lower-priority
Cloud TPU slices. Image locations : Pathways resource manager and worker : us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/server: TAG IFRT proxy server : us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/proxy_server: TAG Colocated Python sidecar : us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/colocated_python_sidecar: TAG Image tags : Replace TAG with one of the
following tags, which are created automatically when a Pathways build
passes qualification tests and is promoted to production: YYYYMMDD -jax_ JAX_VERSION :
Pinned tag created by combining the UTC promotion date
( YYYYMMDD ) with -jax_ and the verified
JAX version ( JAX_VERSION ) after
per-version qualification tests pass. For example, 20261108-jax_0.12.0.1 . jax- JAX_VERSION : Rolling tag updated
after per-version qualification tests pass to point to the most recent
verified image for that JAX release. For example, jax-0.12.0.1 or jax-0.12.0 . latest : Rolling tag updated when a build passes qualification tests
against the most recent supported JAX release. Pathways resource manager and worker : us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/server: TAG IFRT proxy server : us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/proxy_server: TAG Colocated Python sidecar : us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/colocated_python_sidecar: TAG YYYYMMDD -jax_ JAX_VERSION :
Pinned tag created by combining the UTC promotion date
( YYYYMMDD ) with -jax_ and the verified
JAX version ( JAX_VERSION ) after
per-version qualification tests pass. For example, 20261108-jax_0.12.0.1 . jax- JAX_VERSION : Rolling tag updated
after per-version qualification tests pass to point to the most recent
verified image for that JAX release. For example, jax-0.12.0.1 or jax-0.12.0 . latest : Rolling tag updated when a build passes qualification tests
against the most recent supported JAX release. For more information, see Introduction to Pathways on Cloud . [Doc](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro) [Doc](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training) [Doc](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training#elastic-training) [Doc](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads#colocated-python) [Doc](https://github.com/google/grain) [Doc](https://github.com/google/orbax) [Doc](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode) [Doc](https://github.com/AI-Hypercomputer/pathways-utils/tree/main/pathwaysutils/experimental/shared_pathways_service) [Doc](https://docs.cloud.google.com/cluster-director/docs/overview) [Doc](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/run-workloads-pathways) [Doc](https://github.com/AI-Hypercomputer/pathways-utils) [Doc](https://github.com/AI-Hypercomputer/pathways-utils/blob/main/pathwaysutils/experimental/reshard.py) [Doc](https://github.com/AI-Hypercomputer/pathways-utils/tree/main/pathwaysutils/experimental/gke) [Doc](https://github.com/google/skills/tree/main/skills/cloud/pathways-workload)

### Anthos Config Management
- **[Change]**: Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.
- **[Change]**: Upgraded the git-sync dependency from v4.4.2 to v4.5.0 to pick up vulnerability fixes. For more details, see git-sync releases . [Doc](https://github.com/kubernetes/git-sync/releases)
- **[Change]**: Upgraded the Open Telemetry image from 0.152.0 to 0.159.0 to pick up vulnerability fixes. To understand the changes in each release, review the full changelog for opentelemetry-collector-contrib . [Doc](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/CHANGELOG.md)

### Anti Money Laundering AI
- **[Announcement]**: New minor engine version released for the commercial line of business within the v004.009 version line ( aml-commercial.default.v004.009.202610-000 ). This version extends support for the major engine version and includes no significant changes compared to the previous minor version.

### BigQuery
- **[Feature]**: When you create or schedule a pipeline, you can specify the maximum number of
concurrently executed pipeline tasks. This feature is generally available (GA). [Doc](https://docs.cloud.google.com/bigquery/docs/create-pipelines) [Doc](https://docs.cloud.google.com/bigquery/docs/schedule-pipelines) [Doc](https://cloud.google.com/products#product-launch-stages)

### Bigtable
- **[Feature]**: You can use the Google Cloud console to create and manage Apache Avro schema
bundles for your Bigtable tables. You can also view Avro schema bundle
definitions in Bigtable Studio. This feature is in Preview . For more
information, see Create and manage Avro schemas . [Doc](https://cloud.google.com/products#product-launch-stages) [Doc](https://docs.cloud.google.com/bigtable/docs/create-manage-avro-schemas)

### Dataform
- **[Feature]**: You can limit how many actions run concurrently within a single workflow
execution or workflow configuration schedule .
This feature is generally available (GA). [Doc](https://docs.cloud.google.com/dataform/docs/trigger-execution#limit-concurrent-actions) [Doc](https://docs.cloud.google.com/dataform/docs/schedule-runs#create-workflow-configuration) [Doc](https://cloud.google.com/products#product-launch-stages)
