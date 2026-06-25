# Runner API (Planned)

Implemented

✅ runner(df, bib_number)


Returns the complete race record for a single runner.



Purpose

The Runner API provides answers about an individual runner,
while the Race API provides answers about the entire race.

Design Question

How should a runner be identified?

Current decision (MVP)

Use Bib Number as the unique runner identifier.

Future

The platform may introduce a permanent Runner ID,
but Bib Number is sufficient for the first version.

