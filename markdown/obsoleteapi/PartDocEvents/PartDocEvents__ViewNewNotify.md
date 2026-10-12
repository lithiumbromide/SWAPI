---
title: "ViewNewNotify - PartDoc Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDocEvents/PartDocEvents__ViewNewNotify.htm"
---

# ViewNewNotify - PartDoc Event

This event is obsolete and has been superseded by the PartDoc event [ViewNewNotify2](sldworksAPI.chm::/PartDocEvents/PartDocEvents__ViewNewNotify2.htm).

Description

Post-notifies the user program when a new view window has been activated for the first time. This can occur by selecting Window, New Window or by using the split bar and then clicking in the newly created view.

status = ViewNewNotify ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

After you receive notification that a new view has been activated for the first time, you can get its handle using ModelDoc::ActiveView and ModelDoc::GetViewHWnd.
