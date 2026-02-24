Slash Live DB Challenge
For a batch processing job that runs once a day, you must delete all cards marked as “canceled” from the production database. The card may be referenced by other rows in the database and these references may be circular. For purposes of the question, you may not use CASCADE.

Prompt: Write a method called deleteCanceledCards that will remove all canceled cards from the database.

Assume you have access to all the schemas. Suppose a function getSchemas will return a list of schemas that each contain:

A list of columns
A list of foreign key references

Assume you also have access to an ORM which lets you fetch data (you can choose how you’d like to mock the ORM).

In Typescript, the type definition for the schema would look like:
interface Schema {
  /**
   * The name of the table being referenced
   */
  tableName: string;
  columns: Array<{
    name: string;
    type: string;
    nullable: boolean;
  }>;
  foreignKeys: Array<{
    /**
     * The column on this table being referenced
     */
    columnName: string;
    /**
     * The name of the table being that the foreign key is on (can be the same table)
     */
    foreignTableName: string; 
    /**
     * The name of the column on the table being referenced.
     */
    foreignKeyColumnName: string;
  }>
  // the table may have other properties like indexes but they are not relevant for this
}

New tables may be added/removed from the database over time. However, you must come up with a solution that can effectively delete all relevant tables without needing to manually maintain the code as new tables are added.

Example database
CREATE TABLE "card" (
  "id" VARCHAR PRIMARY KEY,
  "name" VARCHAR NOT NULL,
  "last4" VARCHAR NOT NULL,
  "expiry" VARCHAR NOT NULL,
  "status" VARCHAR NOT NULL, -- this is the status that might be "canceled"
  "timestamp" TIMESTAMP NOT NULL,
  "latestTransactionId" VARCHAR
);

ALTER TABLE "card" ADD CONSTRAINT "FK_1" FOREIGN KEY ("latestTransactionId") REFERENCES "transaction"("id");

CREATE TABLE "card_event_history" (
  "id" VARCHAR PRIMARY KEY,
  "cardId" VARCHAR NOT NULL,
  "metadata" JSONB NOT NULL,
  "timestamp" TIMESTAMP NOT NULL
);
ALTER TABLE "card_event_history" ADD CONSTRAINT "FK_2" FOREIGN KEY ("cardId") REFERENCES "card"("id");

CREATE TABLE "card_notification" (
  "id" VARCHAR PRIMARY KEY,
  "cardId" VARCHAR NOT NULL,
  "previousNotificationId" VARCHAR,
  "timestamp" TIMESTAMP
)
ALTER TABLE "card_notification" ADD CONSTRAINT "FK_3" FOREIGN KEY ("cardId") REFERENCES "card"("id")
ALTER TABLE "card_notification" ADD CONSTRAINT "FK_4" FOREIGN KEY ("previousNotificationId") REFERENCES "card_notification"("id")

CREATE TABLE "transaction" (
  "id" VARCHAR PRIMARY KEY,
  "cardId" VARCHAR NOT NULL,
  "description" VARCHAR NOT NULL,
  "amount" INT VARCHAR NOT NULL,
  "timestamp" TIMESTAMP NOT NULL
)
ALTER TABLE "transaction" ADD CONSTRAINT "FK_5" FOREIGN KEY ("cardId") REFERENCES "card"("id")

CREATE TABLE "transaction_notification" (
  "id" VARCHAR PRIMARY KEY,
  "transactionId" VARCHAR NOT NULL,
  "previousTransactionNotificationId" VARCHAR,
  "timestamp" TIMESTAMP
)

ALTER TABLE "transaction_notification" ADD CONSTRAINT "FK_6" FOREIGN KEY ("transactionId") REFERENCES "transaction"("id")
ALTER TABLE "transaction_notification" ADD CONSTRAINT "FK_7" FOREIGN KEY ("previousTransactionNotificationId") REFERENCES "transaction_notification" ("id")

