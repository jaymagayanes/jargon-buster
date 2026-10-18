## authentication
term: Authentication
category: Security & Identity
eli5: Proving who you are.
analogy: Like showing your ID at the door.
enables: authorization, sso, mfa, token

## authorization
term: Authorization
category: Security & Identity
eli5: Deciding what a person who has been identified is allowed to do.
analogy: Like a hotel key card that opens your room but not anyone else's.
precursors: authentication
related: least_privilege, oauth

## sso
term: Single Sign-On (SSO)
category: Security & Identity
eli5: Signing in once to reach many apps, without logging in separately each time.
analogy: Like a festival wristband that is checked at every gate after one registration.
precursors: authentication
related: oauth, mfa

## mfa
term: Multi-Factor Authentication (MFA)
category: Security & Identity
eli5: Using two or more proofs of identity, such as a password plus a code from your phone.
analogy: Like a safe that needs both a key and a combination.
precursors: authentication
related: sso

## oauth
term: OAuth
category: Security & Identity
eli5: A standard that lets one app act for you in another without ever seeing your password.
analogy: Like a valet key that starts the car but does not open the trunk.
precursors: authorization
related: token, sso, api

## encryption
term: Encryption
category: Security & Identity
eli5: Scrambling data so that only someone with the right key can read it.
analogy: Like writing a letter in a code only you and the reader know.
enables: secrets_management

## least_privilege
term: Least Privilege
category: Security & Identity
eli5: Giving people and systems only the access they need, and no more.
analogy: Like giving a cleaner the key to one floor instead of the whole building.
precursors: authorization
related: secrets_management

## secrets_management
term: Secrets Management
category: Security & Identity
eli5: Storing passwords, keys and tokens safely, outside of code and chat messages.
analogy: Like keeping keys in a locked cabinet instead of on a sticky note.
precursors: encryption
related: least_privilege, token
