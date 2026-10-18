## schema
term: Schema
category: Data & Analytics
eli5: The agreed shape of data: which fields exist, what type each one is, and how tables relate.
analogy: Like the blank boxes on a registration form: a fixed place for name, date and phone number.
enables: etl, data_quality
related: json

## etl
term: ETL (Extract, Transform, Load)
category: Data & Analytics
eli5: Pulls data out of its sources, tidies and reshapes it, then loads it somewhere people can use it.
analogy: Like gathering supplies from several shops, sorting them at home, then putting everything on one shelf.
precursors: schema
enables: data_warehouse
related: data_pipeline

## data_pipeline
term: Data Pipeline
category: Data & Analytics
eli5: An automated route that moves data from one place to another, often cleaning it along the way.
analogy: Like a water network carrying water from the reservoir to every tap, with filters on the route.
enables: data_lineage
related: etl, message_queue

## data_warehouse
term: Data Warehouse
category: Data & Analytics
eli5: A central store of cleaned, organized data built for reporting and analysis.
analogy: Like an archive room where every box is labelled and sorted, ready for researchers.
precursors: etl
related: data_lake, data_catalog

## data_lake
term: Data Lake
category: Data & Analytics
eli5: A large store that keeps raw data in its original form until someone needs it.
analogy: Like a real lake that collects water from many streams before anyone decides how to use it.
related: data_warehouse

## data_quality
term: Data Quality
category: Data & Analytics
eli5: How accurate, complete, consistent and up to date a set of data is.
analogy: Like proofreading a document before sending it: mistakes are cheaper to catch early.
precursors: schema
related: data_lineage

## data_lineage
term: Data Lineage
category: Data & Analytics
eli5: A record of where data came from and every step that changed it on the way.
analogy: Like the paper trail behind an antique, listing each owner and repair.
precursors: data_pipeline
related: data_quality, data_catalog

## data_catalog
term: Data Catalog
category: Data & Analytics
eli5: A searchable index that says what data exists, what it means and who owns it.
analogy: Like a library catalogue that tells you which books exist and which shelf holds them.
related: data_warehouse, data_lineage
