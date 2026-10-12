---
title: "PropertyManagerPage2Handler2::AfterClose"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__AfterClose.htm"
---

# PropertyManagerPage2Handler2::AfterClose

## P ropertyManagerPage2Handler2::AfterClose

This method is obsolete and has been superseded by [PropertyManagerPage2Handler3::AfterClose](../PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__AfterClose.htm).

Description

This method is called after the PropertyManager page is closed.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler2.AfterClose ( )

Syntax (COM)

status = PropertyManagerPage2Handler2->AfterClose ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method is meant to be a post-notification of when a page is closed. At this point, it is safer to take action, including executing other methods. The PropertyManagerPage2Handler2::OnClose method is intended to be a pre-notification of when a page is going to close. At this point, before the page is closed, you can collect the information that is currently on the page and save it.

When you run other methods from any handler other than PropertyManagerPage2Handler2::AfterClose, you risk causing your PropertyManager page to close during handling, which will most likely result in a SolidWorks crash. To avoid this risk, create your PropertyManager as locked (see the Options argument of SldWorks::CreatePropertyManagerPage) and design your code to do as much work as possible in the PropertyManagerPage2Handler2::AfterClose method.
