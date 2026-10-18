## cloud_computing
term: Cloud Computing
category: Cloud & Infrastructure
eli5: Renting computing power, storage and software over the internet instead of owning the hardware.
analogy: Like drawing electricity from the grid instead of running your own generator.
enables: virtual_machine, serverless

## virtual_machine
term: Virtual Machine (VM)
category: Cloud & Infrastructure
eli5: A computer made of software that runs inside a real one, with its own operating system.
analogy: Like an apartment block: one building, many separate homes, each with its own lock.
precursors: cloud_computing
enables: container

## container
term: Container
category: Cloud & Infrastructure
eli5: A lightweight package holding an app and everything it needs, so it runs the same anywhere.
analogy: Like a shipping container: whatever is inside, it fits any ship, truck or crane.
precursors: virtual_machine
enables: kubernetes
related: microservices

## kubernetes
term: Kubernetes
category: Cloud & Infrastructure
eli5: A system that starts, stops, scales and repairs containers across many machines automatically.
analogy: Like an air traffic controller assigning planes to runways and rerouting when one is blocked.
precursors: container
related: load_balancer, high_availability

## load_balancer
term: Load Balancer
category: Cloud & Infrastructure
eli5: Spreads incoming requests across several servers so none of them gets overwhelmed.
analogy: Like a host at a busy cafe sending each new group to the table with the shortest wait.
enables: high_availability
related: scalability, kubernetes

## cdn
term: Content Delivery Network (CDN)
category: Cloud & Infrastructure
eli5: A worldwide network of servers that keep copies of content close to each user.
analogy: Like branch libraries holding popular books so nobody has to travel to the main building.
precursors: cache
related: load_balancer

## serverless
term: Serverless
category: Cloud & Infrastructure
eli5: A way to run code where the provider manages the servers and you pay only while your code runs.
analogy: Like taking a taxi instead of owning a car: you pay only for the trip.
precursors: cloud_computing
related: event_driven

## infrastructure_as_code
term: Infrastructure as Code
category: Cloud & Infrastructure
eli5: Describing servers and networks in text files so scripts can create and change them reliably.
analogy: Like an architect's blueprint that lets builders put up identical houses again and again.
precursors: version_control
related: ci_cd, cloud_computing
