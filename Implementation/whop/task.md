# Exercise

## Background

Corporate card transactions require receipts for compliance and expense tracking. Manually matching receipts to transactions is time-consuming, so we want to automate it as much as we can.

## Goal

Develop a **minimum-viable** real-time receipt matching system. 

## Functional Requirements

Your system shall:

- Accept transaction webhook JSON payloads.
- Accept receipt webhook JSON payloads.
- Log matches with: receipt ID, transaction ID, and simulated timestamp of when the matching decision was made.
    - The log timestamp `t_m` means that the receipt/transaction data with timestamps `ts <= t_m` were available when matching.
    - Example: given transaction `{"timestamp": 10001, …}` and matching receipt `{"timestamp": 10020, ...}`, your log could use timestamp `10020`.
- Process events as a **stream**, not as a batch. Simulate a real-time system that reacts to each event.

## Data

Provided in `data/` are three sample files:

- `transactions.jsonl`: Transaction webhook JSON payloads. These are received when we process a transaction.
- `receipts.jsonl` : Receipt webhook JSON payloads. These are received after we receive a cardholder-submitted receipt, and contain the OCR-extracted data.
- `users.db`: SQLite file containing user and card mapping tables to help you link transactions to cardholders.

**Hint**: In the sample dataset, the majority of receipts have matching transactions; users are submitting them for a reason!

## Interface

Up to you, but can be as simple as a CLI that accepts the 3 files and writes to a log file.

```sh
./matcher transactions.jsonl receipts.jsonl users.db -o matches-log.jsonl
```


## Extension Ideas

If you complete the MVP, use any remaining time to explore areas that interest you, such as:

- Features that could improve user experience
- Testing
- Data analysis
- Code quality

## Things to Consider

As you work through the exercise, here are some examples of considerations that may be relevant:

- The demo dataset is tiny. How would you think about scale as more transactions and receipts are ingested?
- What are the tradeoffs in your implementation approach?
- How is AI helping (or hindering) your problem-solving process?



----------
notes:

- matching receipts with expenses
- receive those 2 webhooks and match them. 