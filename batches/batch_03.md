## version_control
term: Version Control
category: Engineering & DevOps
eli5: A tool that records every change to files, so you can compare, undo and work in parallel.
analogy: Like the history panel of a shared document, but built for code.
enables: code_review, ci_cd, infrastructure_as_code, rollback
related: branch

## code_review
term: Code Review
category: Engineering & DevOps
eli5: Teammates read a proposed change before it is merged, to catch mistakes and share knowledge.
analogy: Like an editor reading a draft before it goes to print.
precursors: version_control
related: unit_test, rfc

## unit_test
term: Unit Test
category: Engineering & DevOps
eli5: A small automated check that one piece of code does what it should.
analogy: Like trying each light switch in a house before turning the main power on.
enables: ci_cd, refactoring
related: code_review, bug

## ci_cd
term: CI/CD
category: Engineering & DevOps
eli5: Automatically building, testing and releasing code every time it changes.
analogy: Like a conveyor belt with inspection stations between the raw parts and the loading dock.
precursors: version_control, unit_test
enables: staging_environment
related: rollback

## staging_environment
term: Staging Environment
category: Engineering & DevOps
eli5: A near-copy of the live system where changes are tried out before real users see them.
analogy: Like a dress rehearsal on the real stage before opening night.
precursors: ci_cd
related: rollback, feature_flag, sandbox

## feature_flag
term: Feature Flag
category: Engineering & DevOps
eli5: A switch that turns a feature on or off without shipping new code.
analogy: Like a wall switch for one room: you can test the lights without rewiring the house.
related: rollback, staging_environment

## rollback
term: Rollback
category: Engineering & DevOps
eli5: Returning a system to its last known working version after a bad release.
analogy: Like pressing undo right after a wrong edit.
precursors: version_control
related: ci_cd, incident_response

## technical_debt
term: Technical Debt
category: Engineering & DevOps
eli5: The future cost of the quick shortcuts taken in code or design today.
analogy: Like skipping a car's servicing: you save time now and pay more later.
related: refactoring

## refactoring
term: Refactoring
category: Engineering & DevOps
eli5: Cleaning up the structure of code without changing what it does.
analogy: Like reorganizing a toolbox so the same tools are easier to find.
precursors: unit_test
related: technical_debt
