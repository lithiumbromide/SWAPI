---
title: "FileSaveAsNotify - PartDoc Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDocEvents/PartDocEvents__FileSaveAsNotify.htm"
---

# FileSaveAsNotify - PartDoc Event

This event is obsolete and has been superseded by PartDoc event [FileSaveAsNotify2](sldworksAPI.chm::/PartDocEvents/PartDocEvents__FileSaveAsNotify2.htm).

Description

Pre-notifies the user program when a file is about to be saved with a new name and passes the new document name.

status = FileSaveAsNotify ( FileName )

| Input: | (BSTR) FileName | Name of the saved file |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You should check the filename extension of the FileName value passed to your application because the user may be saving this document as IGES, DSF, and so on.

When a user selects File, Save on a document that has never been saved, you receive a FileSaveAsNotify instead of FileSaveNotify.

Return S_FALSE to stop from proceeding with the action that caused the notification.
