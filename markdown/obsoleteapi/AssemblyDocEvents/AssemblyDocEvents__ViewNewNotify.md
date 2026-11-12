---
title: "ViewNewNotify - AssemblyDoc Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDocEvents/AssemblyDocEvents__ViewNewNotify.htm"
---

# ViewNewNotify - AssemblyDoc Event

This event is obsolete and has been superseded by Assembly Doc event [ViewNewNotify2](sldworksAPI.chm::/AssemblyDocEvents/AssemblyDocEvents__ViewNewNotify2.htm).

Description

This event post-notifies the user program when a new view window has been activated for the first time.

status = ViewNewNotify ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

SolidWorks generates this event when the user selects Window, New Window, or uses the splitter and moves focus to the new view. Once you receive notification that a new view has been activated for the first time, you can use ModelDoc2::ActiveView and ModelView::GetViewHWnd to get its handle.
