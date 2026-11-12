---
title: "PropertyManagerPage2Handler::OnClose"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler/PropertyManagerPage2Handler__OnClose.htm"
---

# PropertyManagerPage2Handler::OnClose

This method is obsolete and has been superseded by [PropertyManagerPage2Handler2::OnClose](../PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnClose.htm).

Description

This method is called when the PropertyManager page is about to be closed.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler.OnClose ( Reason )

| Input: | (long) Reason | Reason this method is being called as defined in swPropertyManagerPageCloseReasons_e |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler->OnClose ( Reason )

| Input: | (long) Reason | Reason this method is being called as defined in swPropertyManagerPageCloseReasons_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful, S_FALSE to discontinue the Close operation and leave the PropertyManager page open |

Remarks

This method is meant to be a pre-notification of when a page is going close. At this point, before the page is gone, you can collect the information that is currently in the page and save it.
