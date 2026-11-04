# AI-assisted job workflow: testing offer-selection rules

## Problem

A job-collection workflow needs to distinguish actionable offers from applications already sent, closed or discarded opportunities, and entries requiring manual review. Otherwise, the review queue can repeatedly surface unsuitable records.

## My role

I define workflow requirements, instruct AI coding agents, review their outputs and correct behaviour against real user needs. This case study shows selected Python logic from my working job-agent project and a small executable validation suite. It demonstrates requirements, agent delegation and output review; it does not claim that I manually authored every line of agent-assisted code.

## Selected implementation

- [Offer-selection functions](../examples/job_offer_rules/offer_valid.py): functions copied unchanged from the working agent.
- [Status definitions](../examples/job_offer_rules/schema.py): only the two status sets needed by those functions.
- [Validation tests](../examples/job_offer_rules/test_offer_valid.py): newly added portfolio tests using synthetic data.

The live workflow includes collection, classification and CRM stages. This standalone example isolates selection rules so reviewers can run it without credentials, an inbox or a workbook. It does not implement scraping or autonomous application submission.

## Rules under test

An actionable offer must be Priority, explicitly remote-compatible, contain a URL, have no application date, and have neither a terminal nor a manual-review status. Already-applied status variants are excluded.

Manual-review entries need a URL, must not already be terminal/applied, and either have a review status or a review/skipped marker in their notes. Synthetic tests cover normalization, missing information and status transitions.

## Run locally

Requires Python 3.9 or later, with no third-party dependencies.

```bash
cd examples/job_offer_rules
python -m unittest -v
```

## Validation and limits

The test suite checks the published selection functions with fabricated records. It does not certify the entire collection pipeline, prove every incoming offer is correctly classified, or validate a live CRM. A present URL is checked for non-empty text, not network availability or URL syntax. These boundaries keep the example's results specific and reproducible.

No employer test assets, personal application records, email contents, credentials or operational Git history are included.
