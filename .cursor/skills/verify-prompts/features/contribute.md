# Contribution route

## Sub-features

Local guide, pull-request template and repository-specific pull-request destination.

## How to get to it (user POV)

At the README contribution section, open contributing.md, then use the pull-request link when intentionally contributing.

## Driving it with Python

The helper checks guide/template presence, guide's README editing instructions and absence of the old YOUR_REPO placeholder. It does not submit any pull request.

## Gotchas

Creating a contribution is an external write, not a safe verification action by default. External link health and permissions are separate checks; placeholder or absent local guide is a real failure.
