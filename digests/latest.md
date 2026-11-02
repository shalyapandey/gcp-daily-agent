# ☁️ Google Cloud Daily Briefing — November 02, 2026

## ⚡ Executive Summary
Found 6 updates across Google Cloud in the past 24 hours.

## 🛠️ Release Notes
### Cloud Load Balancing
- **[Feature]**: Distributed tracing with Cloud Trace is available in Preview for
Global external Application Load Balancers, Regional external Application Load Balancers,
Regional internal Application Load Balancers, and Cross-region internal Application Load Balancers. Attach a
telemetry policy to a load balancer's forwarding rule to generate trace spans
that conform to W3C Trace Context and OpenTelemetry, and get end-to-end
visibility into requests from clients through the load balancer to your
backends. For more information, see Distributed tracing overview . [Doc](https://cloud.google.com/products#product-launch-stages) [Doc](https://docs.cloud.google.com/load-balancing/docs/distributed-tracing-overview)
- **[Feature]**: For mutual TLS (mTLS) on Application Load Balancers,
frontend mTLS validation relaxations are generally available . The ALLOW_VALIDATION_RELAXATIONS client validation mode on the
Client Authentication ( ServerTlsPolicy ) resource allows you to
configure specific X.509 certificate validation exceptions to
standard client certificate validation rules.
This simplifies migrations of legacy workloads while
maintaining an active security posture. This mode supports the following client certificate validation relaxation
parameters: ALLOW_MISSING_EKU : Bypasses Extended Key Usage validation if the EKU
extension is absent in the client certificate. ALLOW_SHA1_HASHING : Permits client certificates signed with the legacy
SHA-1 algorithm. ALLOW_EXPIRED_LEAF_CERTIFICATE : Evaluates expired leaf certificates by
validating them as of 1 second prior to their actual expiration time. ALLOW_MISSING_EKU : Bypasses Extended Key Usage validation if the EKU
extension is absent in the client certificate. ALLOW_SHA1_HASHING : Permits client certificates signed with the legacy
SHA-1 algorithm. ALLOW_EXPIRED_LEAF_CERTIFICATE : Evaluates expired leaf certificates by
validating them as of 1 second prior to their actual expiration time. This feature is available for all Application Load Balancer types. For more information, see Client validation modes . [Doc](https://docs.cloud.google.com/load-balancing/docs/mtls#client-validation-mode)

### Datastream
- **[Feature]**: Datastream is now available in the africa-south1 (Johannesburg)
region. For the list of all available regions, see IP allowlists and regions . [Doc](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions)
- **[Feature]**: Datastream is now available in the asia-southeast3 (Bangkok)
region. For the list of all available regions, see IP allowlists and regions . [Doc](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions)

### Model Armor
- **[Feature]**: Support for template-specific exclusion rules in streaming sanitization
( StreamSanitizeUserPrompt and StreamSanitizeModelResponse ) is available in Preview . You can use
dictionary and regular expression exclusion rules in buffered mode
( STREAMING_MODE_BUFFERED ) with partial or full matching, and in real-time mode
( STREAMING_MODE_REALTIME ) with partial matching, to mitigate false-positive
detections for prompt injection and jailbreak detection and responsible AI
filters. For more information, see Exclusion rules in streaming
sanitization . [Doc](https://cloud.google.com/products#product-launch-stages) [Doc](https://docs.cloud.google.com/model-armor/configure-exclusion-rules#exclusion-rules-streaming)

### Oracle Database@Google Cloud
- **[Feature]**: Oracle Database@Google Cloud supports creating custom DNS domains for your ODB Networks. You can use custom Domain Name Systems (DNS) to control the names of your resources and delegate DNS resolution within your organization. For more information, see Create and manage custom DNS domains . You can use custom DNS domains only for Exadata VM clusters . This feature is generally available (GA) . [Doc](https://docs.cloud.google.com/oracle/database/docs/create-manage-custom-dns) [Doc](https://docs.cloud.google.com/oracle/database/docs/create-clusters) [Doc](https://cloud.google.com/products#product-launch-stages)
