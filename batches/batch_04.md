## monolith
term: Monolith
category: Architecture
eli5: An application built and deployed as one single unit.
analogy: Like one large building that houses every department under the same roof.
related: microservices

## microservices
term: Microservices
category: Architecture
eli5: An application split into small, independent services that each do one job.
analogy: Like a high street of small specialist shops instead of one giant department store.
precursors: api
related: monolith, container, event_driven, loose_coupling

## event_driven
term: Event-Driven Architecture
category: Architecture
eli5: Parts of a system react when something happens, instead of being called directly.
analogy: Like a doorbell: whoever is home responds when it rings, and nobody waits at the door.
precursors: message_queue
related: microservices, serverless, webhook

## scalability
term: Scalability
category: Architecture
eli5: How well a system keeps working as the amount of demand grows.
analogy: Like a road that can add lanes as traffic builds up.
related: load_balancer, microservices

## loose_coupling
term: Loose Coupling
category: Architecture
eli5: Designing parts so each one depends on the others as little as possible.
analogy: Like Lego bricks: swap one piece without rebuilding the whole model.
precursors: api
related: microservices, event_driven

## rfc
term: Request for Comments (RFC)
category: Architecture
eli5: A written proposal shared early so others can review and improve a design.
analogy: Like showing neighbours a draft floor plan before you start building.
enables: adr
related: code_review

## adr
term: Architecture Decision Record (ADR)
category: Architecture
eli5: A short note capturing a design decision, the options considered and why one was chosen.
analogy: Like a ship captain's log entry explaining why the course was changed.
precursors: rfc
related: tech_stack

## tech_stack
term: Tech Stack
category: Architecture
eli5: The set of languages, frameworks and tools a product is built with.
analogy: Like the tools and materials in a workshop: they shape what you can make.
related: adr, infrastructure_as_code
