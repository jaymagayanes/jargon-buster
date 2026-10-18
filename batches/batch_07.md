## api
term: API
category: Integration & APIs
eli5: A defined way for one piece of software to ask another to do something or share data.
analogy: Like a wall socket: a standard shape that lets any matching plug connect.
enables: rest_api, webhook, api_gateway

## rest_api
term: REST API
category: Integration & APIs
eli5: A common style of API that uses web addresses and simple actions like GET and POST.
analogy: Like the postal service: write an address, pick an action, and receive a reply.
precursors: api
related: json, webhook

## json
term: JSON
category: Integration & APIs
eli5: A lightweight text format for sending structured data between systems.
analogy: Like a neatly labelled list both sides can read: name, age, city.
related: rest_api, schema

## webhook
term: Webhook
category: Integration & APIs
eli5: An automatic message one system sends to another the moment something happens.
analogy: Like a doorbell camera alerting your phone the second someone arrives, so you do not keep checking.
precursors: api
related: event_driven, rest_api

## api_gateway
term: API Gateway
category: Integration & APIs
eli5: A single front door that receives API requests, checks them and routes them to the right service.
analogy: Like a reception desk that checks visitors and points them to the right floor.
precursors: api
related: rate_limiting, microservices

## message_queue
term: Message Queue
category: Integration & APIs
eli5: A waiting line that holds messages until the receiver is ready to handle them.
analogy: Like a mailbox where letters wait until the recipient comes to collect them.
enables: event_driven
related: idempotency

## rate_limiting
term: Rate Limiting
category: Integration & APIs
eli5: Capping how many requests a user or app can make in a given amount of time.
analogy: Like a turnstile that lets in a few people a minute to prevent a crush.
related: api_gateway, circuit_breaker

## idempotency
term: Idempotency
category: Integration & APIs
eli5: An action that gives the same result no matter how many times you repeat it.
analogy: Like pressing an elevator call button twice: the lift is still called only once.
related: message_queue, rest_api
