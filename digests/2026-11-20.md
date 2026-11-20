# ☁️ Google Cloud Daily Briefing — November 20, 2026

## ⚡ Executive Summary
Found 5 updates across Google Cloud in the past 24 hours.

## 🛠️ Release Notes
### App Engine flexible environment Java
- **[Security]**: The following runtime language contains important security updates: Java 17 and later : 17.0.21.1+2 , 21.0.13.1+2 , 25.0.5.1+2 Take immediate action by rebuilding and redeploying your applications to pick up
the patched Java runtime, and then remove any temporary JDK_JAVA_OPTIONS mitigation flags. For more information, see security bulletin GCP-2026-082 . [Doc](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#java) [Doc](https://docs.cloud.google.com/support/bulletins#gcp-2026-082)

### App Engine standard environment Java
- **[Security]**: The following runtime language contains important security updates: Java 17 and later : 17.0.21.1+2 , 21.0.13.1+2 , 25.0.5.1+2 Applications receive the patched runtime automatically with no action required. To refresh warm instances immediately, redeploy your application. If you added a temporary JDK_JAVA_OPTIONS mitigation flag in app.yaml or appengine-web.xml , remove it and redeploy. For more information, see security bulletin GCP-2026-082 . [Doc](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#java) [Doc](https://docs.cloud.google.com/support/bulletins#gcp-2026-082)

### Buildpacks
- **[Security]**: The following runtime language contains important security updates: Java 17 and later : 17.0.21.1+2 , 21.0.13.1+2 , 25.0.5.1+2 Take immediate action by rebuilding and redeploying your applications to pick up
the patched Java runtime, and then remove any temporary JDK_JAVA_OPTIONS mitigation flags. For more information, see security bulletin GCP-2026-082 . [Doc](https://docs.cloud.google.com/docs/buildpacks/runtime-support#java) [Doc](https://docs.cloud.google.com/support/bulletins#gcp-2026-082)

### Cloud Run
- **[Security]**: The following runtime language contains important security updates: Java 17 and later : 17.0.21.1+2 , 21.0.13.1+2 , 25.0.5.1+2 Workloads with automatic base image updates enabled receive the patched runtime
automatically with no action required. To refresh warm instances immediately,
redeploy your workload. For custom containers, Cloud Run jobs and worker pools, and deployments without
automatic base image updates, rebuild and redeploy your workloads with a patched
JDK or base image, and then remove any temporary JDK_JAVA_OPTIONS mitigation
flags. For more information, see security bulletin GCP-2026-082 . [Doc](https://docs.cloud.google.com/run/docs/runtime-support#java) [Doc](https://docs.cloud.google.com/support/bulletins#gcp-2026-082)

### Cloud Run functions
- **[Security]**: The following runtime language contains important security updates: Java 17 and later : 17.0.21.1+2 , 21.0.13.1+2 , 25.0.5.1+2 Functions with automatic base image updates enabled receive the patched runtime
automatically with no action required. To refresh warm instances immediately,
redeploy your function. For functions without automatic base image updates, redeploy your functions to
pick up the patched runtime, and then remove any temporary JDK_JAVA_OPTIONS mitigation flags. For more information, see security bulletin GCP-2026-082 . [Doc](https://docs.cloud.google.com/functions/docs/runtime-support#java) [Doc](https://docs.cloud.google.com/support/bulletins#gcp-2026-082)
