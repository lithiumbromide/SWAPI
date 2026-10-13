---
title: "DocumentLoadNotify - SldWorks Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorksEvents/SldWorksEvents__DocumentLoadNotify.htm"
---

# DocumentLoadNotify - SldWorks Event

## D ocumentLoadNotify - SldWorks Event

This event is obsolete and has been superseded by [SldWorksEvent::DocumentLoadNotify2](sldworksAPI.chm::/SldWorksEvents/SldWorksEvents__DocumentLoadNotify2.htm).

Description

Post-notifies the user program when a SolidWorks document is loaded.

NOTE: If developing a C++ application, use swAppDocumentLoadNotify to register for this notification.

status = DocumentLoadNotify ( docTitle , docPath )

| Input: | (BSTR) docTitle | Document title |
| --- | --- | --- |
| Input: | (BSTR) docPath | Document path |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This event is fired for documents referenced by assemblies and drawings. Client code should expect multiple calls to this event handler when an assembly or drawing is loaded.
