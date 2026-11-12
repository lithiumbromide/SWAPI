---
title: "FileSaveAsNotify - AssemblyDoc Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDocEvents/AssemblyDocEvents__FileSaveAsNotify.htm"
---

# FileSaveAsNotify - AssemblyDoc Event

This event is obsolete and has been superseded by the AssemblyDoc event [FileSaveAsNotify2](sldworksAPI.chm::/AssemblyDocEvents/AssemblyDocEvents__FileSaveAsNotify2.htm).

Description

This event pre-notifies the user program when a file is about to be saved with a new name and passes the new document name.

status = FileSaveAsNotify ( FileName )

| Input: | (BSTR) FileName | New document name |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You might want to check the file extension on the filename passed to your application because the user may have saved this document as IGES, DXF, and so on. When a user saves a document for the first time, SolidWorks generates a FileSaveAsNotify event instead of a FileSaveNotify event.

You can return S_FALSE to stop SolidWorks from proceeding with the action that caused the notification.
