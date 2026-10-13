---
title: "FileNewNotify - SldWorks Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorksEvents/SldWorksEvents__FileNewNotify.htm"
---

# FileNewNotify - SldWorks Event

This event is obsolete and has been superseded by SldWorks event [FileNewNotify2](sldworksAPI.chm::/SldWorksEvents/SldWorksEvents__FileNewNotify2.htm).

Description

Post-notifies the user program when a new file has been created.

status = FileNewNotify ( newDoc , docType )

| Input: | (LPDISPATCH) newDoc | Pointer to the new document |
| --- | --- | --- |
| Input: | (long) docType | Type of the new document |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The dispatch item returned has a reference count of 1. Your program is responsible for releasing this item. For more information on releasing, see Interface Pointers.
