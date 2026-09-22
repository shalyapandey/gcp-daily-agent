# ☁️ Google Cloud Daily Briefing — September 22, 2026

## ⚡ Executive Summary
<<<<<<< HEAD
Found 5 updates across Google Cloud in the past 24 hours.
=======
Found 41 updates across Google Cloud in the past 48 hours.
>>>>>>> a1a0b75 (feat: add SnowNews RSS integration for Medium community articles and Workspace updates)

## 🛠️ Release Notes
### Cloud Trace
- **[Feature]**: The following remote Google Cloud MCP servers automatically generate a trace span for tools/call operations. Identity and Access Management Organization Policy Service Policy Analyzer Security Command Center Spanner Unified Maintenance These spans can help you understand the behavior of
your agentic applications. For more information, see Investigate MCP calls using Trace . [Doc](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls)
- **[Feature]**: You can use Terraform to configure resources managed by the Observability API.
For example, you can use Terraform to create and update observability buckets,
create links on datasets, and configure default settings. For more information, see the following documents: Set defaults for observability buckets Create observability buckets Update observability buckets List buckets and manage datasets [Doc](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets) [Doc](https://docs.cloud.google.com/stackdriver/docs/observability/create-observability-buckets) [Doc](https://docs.cloud.google.com/stackdriver/docs/observability/update-observability-buckets) [Doc](https://docs.cloud.google.com/stackdriver/docs/observability/storage-manage)

### Compute Engine
- **[Deprecated]**: As of September 15, 2026, NVIDIA P100 ( nvidia-tesla-p100 and nvidia-tesla-p100-vws ) GPUs have reached end of support (EOS) and are shut
down. You can no longer create, launch, or access Compute Engine
instances or other Google Cloud resources that use NVIDIA P100 GPUs. For information about migrating your workloads to supported GPU alternatives
such as the G2 (NVIDIA L4) or G4 (NVIDIA RTX PRO 6000) machine series, see NVIDIA P100 end of support . [Doc](https://docs.cloud.google.com/compute/docs/eol/p100-eos)
- **[Deprecated]**: NVIDIA T4 ( nvidia-tesla-t4 and nvidia-tesla-t4-vws ) and NVIDIA P4
( nvidia-tesla-p4 and nvidia-tesla-p4-vws ) GPUs are deprecated and will reach
end of support (EOS) on August 1, 2027. After August 1, 2027, you won't be able
to create, launch, or access Compute Engine instances or other
Google Cloud resources that run NVIDIA T4 or P4 GPUs. In addition, you can no
longer purchase or renew 3-year committed use discounts (CUDs) for NVIDIA T4 or
P4 GPUs. To transition your workloads to supported GPU models such as the G2 (NVIDIA L4)
or G4 (NVIDIA RTX PRO 6000) machine series before the EOS date, see NVIDIA T4 end of support and NVIDIA P4 end of support . [Doc](https://docs.cloud.google.com/compute/docs/eol/t4-eos) [Doc](https://docs.cloud.google.com/compute/docs/eol/p4-eos)

<<<<<<< HEAD
### Gemini Enterprise Agent Platform
- **[Feature]**: Anthropic's Claude Opus 5.5 Claude Opus 5.5 is available in Model Garden. [Doc](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/opus-5-5)
=======
### Access Context Manager
- **[Feature]**: Access Context Manager supports extended session length for Workforce Identity
Federation. This feature is in Preview for Looker
(Google Cloud core) customers. For more information, see Configure extended session length for Workforce Identity Federation . [Doc](https://cloud.google.com/products#product-launch-stages) [Doc](https://docs.cloud.google.com/access-context-manager/docs/extended-session-length-for-workforce-identity-federation)

### Agent Platform Workbench
- **[Change]**: Installed latest packages from upstream dependencies.
- **[Feature]**: JupyterLab now forwards client-side logs (console errors, uncaught exceptions, unhandled promise rejections, and failed network requests) to the instance backend, where they surface in Cloud Logging for easier debugging.
- **[Change]**: Installed latest packages from upstream dependencies.
- **[Feature]**: JupyterLab now forwards client-side logs (console errors, uncaught exceptions, unhandled promise rejections, and failed network requests) to the instance backend, where they surface in Cloud Logging for easier debugging.

### AlloyDB for PostgreSQL
- **[Feature]**: You can now use the AlloyDB Columnar Engine as a read-optimized, in-memory
cache for HNSW vector indexes. This feature is generally available
( GA ). It accelerates vector search
performance and increases queries per second (QPS) for vector workloads. For more information, see Accelerate queries with the Columnar Engine . [Doc](https://cloud.google.com/products#product-launch-stages) [Doc](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-with-ce)

### Apigee X
- **[Announcement]**: On September 21st, 2026, we began maintenance updates of Apigee instances configured for maintenance windows . If you set a preferred window for maintenance for your instance, and your instance version is
below 1-18-0-apigee-4 , your instance will be updated to 1-18-0-apigee-4 within the
next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days. Note: Instances that meet either of the following two criteria will not be updated: Your instance has a DNS misconfiguration, as described in Known Issue 445936920 . Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025 . For more information on participating in scheduled maintenance windows, see Maintenance overview and Manage Apigee instance maintenance windows . [Doc](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows) [Doc](https://docs.cloud.google.com/apigee/docs/release/known-issues) [Doc](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025) [Doc](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance)
- **[Announcement]**: On September 21st, 2026, we released an updated version of Apigee (1-18-0-apigee-5). Note: Rollouts of this release began today and can take four or more business days to be completed across all Google Cloud zones. Your instances might not have the features and fixes available until the rollout is complete.
- **[Security]**: Bug ID Description 560130499 Security fix for Apigee. Fixed a security issue in the Java Callout policy. 547681234 Security fix for Apigee. Patched CVE-2026-69247 by upgrading a third-party library used by the Apigee model-security engine. 556568593 Security fix for Apigee. Patched CVE-2026-84304 by upgrading gRPC. N/A Security fix for Apigee infrastructure. [Doc](https://nvd.nist.gov/vuln/detail/CVE-2026-69247) [Doc](https://nvd.nist.gov/vuln/detail/CVE-2026-84304)
- **[Fixed]**: Bug ID Description 559009293 Fixed elevated OAuth and VerifyAPIKey latency and Cassandra read load for AppGroup apps by caching the AppGroup entity in the Message Processor runtime, matching Developer-app behavior. 558888960 Fixed distributed tracing so that the target URL is included as a span attribute in all scenarios. 556750755 Fixed EventFlow (Server-Sent Events) dropping or truncating events that follow a large (greater than 16 KB) event under load on the http-adaptor data path. 553931019 The MCP tools/list method now aggregates tools across all approved API products. 531783017 Implemented the <Enforce>true</Enforce> element of SSLInfo for a Syslog endpoint, so that the syslog target's TLS server identity is verified. 554114419 Policies can now change request pseudo-headers (for example, :path and :authority) when HTTP/2 is in use. 548763108 Blocked outbound HTTP from the Message Processor to Kubernetes-internal targets. 513032450 Restored a 15-second TCP keep-alive on the Apigee Connect control-plane connection so that a silently dropped connection recovers in seconds rather than approximately two hours. N/A Updates to infrastructure and libraries.

### BigQuery
- **[Feature]**: The Query results pane in the BigQuery Studio query editor lets you view a short history of recent runs for a query , including
multi-statement queries, without having to navigate to the Job history tab.
This feature is generally available (GA). [Doc](https://docs.cloud.google.com/bigquery/docs/multi-statement-queries#view_multi_statement_query_results) [Doc](https://cloud.google.com/products/#product-launch-stages)
- **[Feature]**: BigQuery generative AI functions now support the gemini-3.8-flash Gemini model. [Doc](https://docs.cloud.google.com/bigquery/docs/generative-ai-overview#locations)

### Dataform
- **[Feature]**: The Dataform remote Model Context Protocol (MCP) server now supports pipeline
authoring in development workspaces and Git repository operations. AI agents can
create and list workspaces, search and edit files, commit changes and push
commits to remote Git providers, update repository settings, and organize
repositories in folders. For more information, see Use the Dataform remote MCP server and the Dataform MCP reference .
This feature is generally available (GA). [Doc](https://docs.cloud.google.com/dataform/docs/use-dataform-mcp) [Doc](https://docs.cloud.google.com/dataform/docs/reference/mcp) [Doc](https://cloud.google.com/products#product-launch-stages)

### Gemini Enterprise
- **[Feature]**: Gemini Enterprise: Transfer ownership of shared agents Administrators can transfer ownership of shared employee-made agents to another
user or to themselves in the Google Cloud console. This is useful when
reassigning agents created by departing employees or when temporary workers
hand over agents to full-time staff. Key characteristics and requirements include: Administrator only: Only users with the Gemini Enterprise Admin role
( roles/discoveryengine.agentspaceAdmin or roles/discoveryengine.admin ) can
transfer agent ownership. Agent owners cannot transfer ownership unless they
are also administrators. Shared agents only: Ownership transfer is supported only for agents that
are already shared. Private agents cannot be transferred. Single owner: Each agent has only one owner at a time. When ownership is
transferred, the selected user becomes the sole owner, and the previous owner
is retained as a permissioned user with the agentUser role. Agents with schedules or triggers: If the transferred agent has a schedule
trigger or event trigger, the transfer operation marks them as disabled
schedules or events. The new owner must enable it before being able to use
the agent. Identity formats: Administrators can transfer ownership to users with
Google accounts (using email addresses) or to users in a Workforce Identity
Federation (WIF) pool (using workforce identity principal identifiers). For more information, see Transfer agent
ownership . [Doc](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents#transfer-ownership)

### Google Cloud Contact Center as a Service
- **[Announcement]**: Google Cloud CCaaS prerelease notes 6.15 Here are the pre-release notes for what we expect to be the next version
of Google Cloud CCaaS. When we release this version, we expect the new
capabilities to be as shown here. Important: The next version of Google Cloud CCaaS could be greater than 6.15.
- **[Feature]**: Remove a user from all teams at once Using the new Remove from all teams button, you can remove a user from all
of the teams that they belong to. Administrators: There's a new Remove from all teams button in the Teams section of the Edit User dialog.
- **[Fixed]**: This release addresses the following issues: Fixed an issue that led to increased startup latency and errors for mobile
and web chat sessions. Fixed an issue where agents were incorrectly demoted to an Unresponsive status and removed from the routing pool despite successfully receiving call
offers. Fixed an issue where dialed numbers on Twilio BYOC SIP inbound calls were
incorrectly formatted with extra digits from the SIP host and port. Fixed an issue that prevented chat transcripts from being generated and
delivered for sessions containing structured message content. Fixed an issue where the call adapter incorrectly showed a call as on hold
after a carrier failed to process the hold request, leaving the audio
channel open between the agent and the customer. Fixed an issue where a failed media download caused the service to restart
unexpectedly. Fixed an issue that caused queue-specific wrap-up and disposition settings
to reset to global defaults after changing unrelated fields on the Queue
Settings page. Fixed an issue where machine translation didn't activate for chats that were
transferred into a non-English language queue if the session originated with
a virtual agent. Fixed an issue where generative knowledge assist answers that contain long
URLs were cut off at the edge of the panel. Fixed an issue where queued calls were neither routed to available agents
nor offered a callback. Fixed an issue where voicemails were automatically dismissed and marked as
read if a playback error occurred. Fixed an issue where agent call recordings were missing or attached to the
wrong call record after a virtual agent deflection. Fixed an issue where unanswered DCR calls that were routed using Nexmo
disconnected the caller instead of requeuing the call. Fixed an issue that prevented virtual agents from transferring calls to a
human-agent queue. Fixed an issue where calls lacking a carrier hangup reason were incorrectly
categorized as "customer abandoned", even when the call center didn't answer
the call. Fixed an issue where the call event API payload for DCR calls contained
incorrect virtual agent parameters. Fixed an issue where custom data from chat interactions wasn't recorded in
Salesforce records. Fixed an issue where Mexico time zones were incorrectly applying daylight
saving time adjustments. Fixed an issue where agents and end-users were joined to separate
conferences, preventing audio communication between them. Fixed an issue where call recording deletion tasks entered an endless loop
if the provider didn't return a successful response. Fixed an issue where IVR voice calls didn't send custom wrap-up events to
Dialogflow CX under certain configurations. Fixed an issue where a trailing slash in the host URL caused the web SDK to
unexpectedly re-enable features that had been previously disabled for
specific deployments.

## 📚 Community Insights & Ecosystem Updates (via SnowNews)
- **[Medium]** [How to build a Jev-style classifier with DiffusionGemma and vLLM](https://medium.com/google-cloud/how-to-build-a-jev-style-classifier-with-diffusiongemma-and-vllm-ef2e0bfa9ad7?source=rss----e52cf94d98af---4)
- **[Google Workspace Updates]** [Quick notes in Take notes for me](http://workspaceupdates.googleblog.com/2026/09/quick-notes-in-take-notes-for-me.html)
- **[Google Workspace Updates]** [Introducing the new Confluence integration with Google Chat](http://workspaceupdates.googleblog.com/2026/09/new-confluence-app-for-google-chat.html)
- **[Medium]** [Scheduling Tasks in Antigravity](https://medium.com/google-cloud/scheduling-tasks-in-antigravity-b37f6c9b61ca?source=rss----e52cf94d98af---4)
- **[Google Workspace Updates]** [Manually reorder and custom sort pivot tables in Google Sheets](http://workspaceupdates.googleblog.com/2026/09/manually-reorder-and-custom-sort-pivot.html)
- **[Google Workspace Updates]** [Study notebooks in Gemini are now available for Google Workspace accounts](http://workspaceupdates.googleblog.com/2026/09/study-notebooks-in-gemini-are-now-available-for-Google-Workspace-accounts.html)
- **[Medium]** [Enhancing SAP Data with Google Cortex and SAP BDC Connect for BigQuery](https://medium.com/google-cloud/enhancing-sap-data-with-google-cortex-and-sap-bdc-connect-for-bigquery-1d88fd433023?source=rss----e52cf94d98af---4)
- **[Medium]** [Building generative media agents: model, harness, tools](https://medium.com/google-cloud/building-generative-media-agents-model-harness-tools-b405dad35aee?source=rss----e52cf94d98af---4)
- **[Medium]** [Inside Google Cloud’s Patchamomma 2026: 3,500 Professionals & Aspiring Entrepreneurs Powering the…](https://medium.com/google-cloud/inside-google-clouds-patchamomma-2026-3-500-professionals-aspiring-entrepreneurs-powering-the-9f5bd605b498?source=rss----e52cf94d98af---4)
- **[Medium]** [Google Cloud Knowledge Catalog: Power AI Agents To Execute Complex Tasks with Accuracy](https://medium.com/google-cloud/google-cloud-knowledge-catalog-power-ai-agents-to-execute-complex-tasks-with-accuracy-ead1773eaf5e?source=rss----e52cf94d98af---4)
- **[Medium]** [️️ How We Built an Autonomous AI Vulnerability Remediation Engine on Google Cloud with Gemini 3.7](https://medium.com/google-cloud/%EF%B8%8F%EF%B8%8F-how-we-built-an-autonomous-ai-vulnerability-remediation-engine-on-google-cloud-with-gemini-3-7-802d88430acb?source=rss----e52cf94d98af---4)
- **[Medium]** [Beyond Traditional Vector DBs: An Empirical Benchmark of In-Warehouse using native Google BigQuery…](https://medium.com/google-cloud/beyond-traditional-vector-dbs-an-empirical-benchmark-of-in-warehouse-local-cpu-and-just-in-time-e9d14ed5a64a?source=rss----e52cf94d98af---4)
- **[Medium]** [Always On Air: How AI RJ Studio Is Rebuilding Radio to Beat Audience Churn](https://medium.com/google-cloud/always-on-air-how-ai-rj-studio-is-rebuilding-radio-to-beat-audience-churn-b0980ff6afc5?source=rss----e52cf94d98af---4)
- **[Medium]** [How to Run Open Models in the Cloud Without Going Broke](https://medium.com/google-cloud/how-to-run-open-models-in-the-cloud-without-going-broke-0b026307d1d5?source=rss----e52cf94d98af---4)
- **[Medium]** [Gemma 4 QAT on a Tesla T4](https://medium.com/google-cloud/gemma-4-qat-on-a-tesla-t4-4682b77cd0fb?source=rss----e52cf94d98af---4)
- **[Medium]** [The Pragmatic Guide to Agent Skills](https://medium.com/google-cloud/the-pragmatic-guide-to-agent-skills-b0ee837043e7?source=rss----e52cf94d98af---4)
- **[Google Workspace Updates]** [New manual calculation setting in Google Sheets](http://workspaceupdates.googleblog.com/2026/09/new-manual-calculation-setting-in-Google-Sheets.html)
- **[Google Workspace Updates]** [Use AI to supercharge your financial analysis with Workday for Google Sheets](http://workspaceupdates.googleblog.com/2026/09/use-ai-to-supercharge-your-financial-analysis-with-Workday-for-Google-Sheets.html)
- **[Cloud Blog]** [Strengthen your CI/CD pipeline with new Secure Source Manager capabilities](https://cloud.google.com/blog/products/identity-security/strengthen-your-cicd-pipeline-with-new-secure-source-manager-capabilities/)
- **[Cloud Blog]** [Maximizing Apache Spark availability: Mitigating compute stockouts with flexible VMs and other best practices](https://cloud.google.com/blog/products/data-analytics/maximize-apache-spark-availability-with-flexible-vms/)
- **[Cloud Blog]** [Global AI routing with <1% overhead on multi-cluster GKE Inference Gateway](https://cloud.google.com/blog/products/containers-kubernetes/gpu-and-tpu-utilization-with-multi-cluster-gke-inference-gateway/)
- **[Cloud Blog]** [Scale your AI workloads faster and more efficiently with GKE Pod snapshots](https://cloud.google.com/blog/products/containers-kubernetes/gke-pod-snapshots/)
>>>>>>> a1a0b75 (feat: add SnowNews RSS integration for Medium community articles and Workspace updates)
