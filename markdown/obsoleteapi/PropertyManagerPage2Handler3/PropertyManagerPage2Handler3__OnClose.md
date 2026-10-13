---
title: "PropertyManagerPage2Handler3::OnClose"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnClose.htm"
---

# PropertyManagerPage2Handler3::OnClose

This method is obsolete and has been superseded by [PropertyManagerPage2Handler4::OnClose](../PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnClose.htm).

Description

This method is called when this PropertyManager page is closing.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler3.OnClose ( Reason )

| Input: | (long) Reason | Reason this method is called as defined in swPropertyManagerPageCloseReasons_e |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler3->OnClose ( Reason )

| Input: | (long) Reason | Reason this method is called as defined in swPropertyManagerPageCloseReasons_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This handler method is called when the PropertyManager page is about to close.

SolidWorks controls when add-ins can do work. An add-in is unable to do any real work within the PropertyManager2Handler::OnClose handler because the PropertyManager page and command are closing. So, typically the PropertyPage2Handler3::AfterClose handler is called after PropertyManager2Handler3::OnClose to allow an add-in to do work. However:

| If PropertyManager page is... | And you implemented the handler in... | Then you... |
| --- | --- | --- |
| Not pinned | C++ | Can prevent the PropertyManager page from closing by setting the HRESULT return value to S_FALSE. |
|  | Visual Basic | Should use the Err.Raise method with a value of 1 to prevent the PropertyManager page from closing. |
|  | NOTE: When control returns to SolidWorks: The PropertyManager page remains displayed on the screen. The PropertyManagerPage2Handler3::AfterClose handler is not called. |  |
| Pinned | C++ or Visual Basic | Set HRESULT to S_FALSE to close the PropertyManager page (i.e., ignore the fact that the page is pinned). This allows your add-in to call the PropertyManagerPage2Handler3::AfterClose handler and do its work. To avoid aggravating your user, who expected the PropertyManager page to remain pinned, you should re-display and re-pin the PropertyManager page after the add-in finishes its work. |
