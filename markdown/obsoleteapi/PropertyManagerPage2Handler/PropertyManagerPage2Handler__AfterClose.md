---
title: "PropertyManagerPage2Handler::AfterClose"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler/PropertyManagerPage2Handler__AfterClose.htm"
---

# PropertyManagerPage2Handler::AfterClose

This method is obsolete and has been superseded by [PropertyManagerPage2Handler2::AfterClose](../PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__AfterClose.htm).

Description

This method is called after the page has been closed.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler.AfterClose ( )

Syntax (COM)

status = PropertyManagerPage2Handler->AfterClose ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method is meant to be a post-notification of when the page is gone. At this point, it is safer to take action, including executing other methods.

When you run other methods from any handler other than this method, you risk causing your PropertyManager page to close during handling, which will likely result in a SolidWorks crash. To avoid this risk, create your PropertyManager page as locked (see the Options argument of SldWorks::CreatePropertyManagerPage) and design your code to do as much work as possible in this method.
