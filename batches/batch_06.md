## monitoring
term: Monitoring
category: Reliability & Operations
eli5: Watching a system's health through measurements and alerts, so problems are noticed quickly.
analogy: Like a car dashboard showing speed, fuel and warning lights.
enables: slo, incident_response, observability

## observability
term: Observability
category: Reliability & Operations
eli5: How well you can tell what is happening inside a system from the signals it gives out.
analogy: Like a doctor using temperature and test results to diagnose without opening you up.
precursors: monitoring
related: incident_response

## slo
term: Service Level Objective (SLO)
category: Reliability & Operations
eli5: An internal target for how well a service should perform, such as 99.9% uptime.
analogy: Like a runner's personal-best goal for each race.
precursors: monitoring
enables: sla

## sla
term: Service Level Agreement (SLA)
category: Reliability & Operations
eli5: A promise to customers about service levels, often with consequences if it is missed.
analogy: Like a delivery promise: arrives in two days or you get your money back.
precursors: slo
related: mttr

## incident_response
term: Incident Response
category: Reliability & Operations
eli5: The steps a team follows to spot, fix and communicate about a service problem.
analogy: Like a fire drill: when the alarm sounds, everyone knows their role.
precursors: monitoring
enables: postmortem, mttr
related: rollback

## postmortem
term: Postmortem
category: Reliability & Operations
eli5: A blame-free review after an incident to learn what happened and how to prevent it.
analogy: Like a sports team watching the match footage to play better next time.
precursors: incident_response

## mttr
term: Mean Time to Recovery (MTTR)
category: Reliability & Operations
eli5: The average time it takes to restore service after something breaks.
analogy: Like measuring how long a garage takes to get your car back on the road.
precursors: incident_response
related: sla

## high_availability
term: High Availability
category: Reliability & Operations
eli5: Designing a service so it stays up even when parts of it fail.
analogy: Like a hospital with backup generators, so the lights stay on in a power cut.
precursors: load_balancer
related: disaster_recovery, kubernetes

## disaster_recovery
term: Disaster Recovery
category: Reliability & Operations
eli5: The plan and tools for restoring a service after a major failure, such as losing a data center.
analogy: Like keeping copies of important papers in a safe at a different address.
related: high_availability

## circuit_breaker
term: Circuit Breaker
category: Reliability & Operations
eli5: A pattern that stops calling a failing service for a while, so the failure does not spread.
analogy: Like a fuse in a house that trips to protect the wiring.
related: rate_limiting, high_availability
