---
title: "Programming Items"
project: ""
interface: ""
member: ""
kind: "topic"
source: "API_GB/Items.htm"
---

# Programming Items

A file in SOLIDWORKS PDM Professional consists of two parts:

- The file that is stored on the archive server.
- The metadata associated with the file, or an item, which is stored in the SQL database.

The metadata consists of card contents, file references, permissions, workflow states, revisions, etc. An item is all of the metadata associated with a file. Most of the existing functions that work for files have been adjusted so that they also work for items. Only a few functions are specific to items.

All items and item folders are placed under a folder named "<items>", which is located directly beneath the vault root. SOLIDWORKS PDM Professional does not show this folder in the user interface, but it is included in the paths returned by the SOLIDWORKS PDM Professional API.

All items have the file extension, ".<item>". This extension in also hidden in the user interface, but it is returned by the SOLIDWORKS PDM Professional API.

### Code Samples

- [Creating items from a file structure](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration.html)
- [Creating items without linking them to files](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration2~AddSelection2.html)
- [Retrieving the IEdmItem interface for an item with a certain database ID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html)
- [Displaying properties and references for an item with a certain database ID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html)
- [Obtaining an IEdmItem pointer from an item path](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html)
- [Obtaining an IEdmItem pointer from an item name (via searching)](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html)
- [Displaying a message with all references in an item](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem~GetReferences.html)
- [Updating an item's references](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem~UpdateReferences.html)
- [Adding a reference from an item to an item with IEdmBatchItemReferenceUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemReferenceUpdate~UpdateReferences.html)

### Interfaces

- [IEdmBatchItemGeneration](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration.html)
- [IEdmBatchItemGeneration2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration2.html)
- [IEdmBatchItemReferenceUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemReferenceUpdate.html)
- [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html)
