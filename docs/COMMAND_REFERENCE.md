# Command reference

Commands below are run from PowerShell. Replace the context or namespace only when intentionally targeting a different cluster.

| Command | Purpose |
|---|---|
| `kubectl config get-contexts` | Lists configured Kubernetes contexts. |
| `kubectl config current-context` | Shows the context currently used by kubectl. |
| `kubectl config use-context docker-desktop` | Selects Docker Desktop Kubernetes. |
| `kubectl --context docker-desktop get nodes` | Lists nodes in the specified cluster. |
| `kubectl --context docker-desktop create namespace microservices-lab` | Creates an isolated namespace for this lab. |
| `kubectl --context docker-desktop apply -f deployment.yaml -n microservices-lab` | Creates/updates resources described in the YAML file. |
| `kubectl --context docker-desktop get pods -n microservices-lab` | Lists Pods in the lab namespace. |
| `kubectl --context docker-desktop get pods -n microservices-lab -o wide` | Adds Pod IP and node placement columns. |
| `kubectl --context docker-desktop get pods -n microservices-lab -w` | Watches Pod state changes until interrupted with Ctrl+C. |
| `kubectl --context docker-desktop get deployments -n microservices-lab` | Shows desired, updated, and available replicas. |
| `kubectl --context docker-desktop scale deployment catalog-deployment --replicas=3 -n microservices-lab` | Sets the Catalog Deployment's desired replica count to three. |
| `kubectl --context docker-desktop rollout status deployment/catalog-deployment -n microservices-lab` | Waits for the Catalog Deployment rollout to finish. |
| `kubectl --context docker-desktop get services -n microservices-lab` | Lists Services and their cluster IPs/ports. |
| `kubectl --context docker-desktop get endpointslices -n microservices-lab -l kubernetes.io/service-name=catalog-service` | Lists backend endpoints selected by the Catalog Service. |
| `kubectl --context docker-desktop port-forward -n microservices-lab service/frontend-service 8080:80` | Exposes the frontend Service on local port 8080. Keep this command running. |
| `kubectl --context docker-desktop logs deployment/catalog-deployment -n microservices-lab` | Displays Catalog container logs. |
| `kubectl --context docker-desktop describe deployment catalog-deployment -n microservices-lab` | Displays detailed Deployment and resource configuration. |
| `kubectl --context docker-desktop delete namespace microservices-lab` | Deletes all namespaced resources in this lab; use only for cleanup. |

## Important notes

- `kubectl` acts on the current context unless `--context` is supplied.
- The two clusters `kind-microservices-lab` and `docker-desktop` are independent.
- A `port-forward` command must remain active while using the local browser URL.
- Use `Ctrl+C` to stop the port-forward or a `get ... -w` watch. This does not delete the Kubernetes workload.
