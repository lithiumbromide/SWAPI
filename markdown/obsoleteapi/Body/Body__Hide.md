---
title: "Body::Hide"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__Hide.htm"
---

# Body::Hide

This method is obsolete and has been superseded by [Body2::Hide](sldworksAPI.chm::/Body2/Body2__Hide.htm).

Description

This method hides a temporary body object using the specified part's context.

Syntax (OLE Automation)

void Body.Hide ( part)

| Input: | (LPDISPATCH) part | Pointer to dispatch object, the part |
| --- | --- | --- |

Syntax (COM)

status = Body->IHide ( part )

| Input: | (LPPARTDOC) part | Pointer to the part |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

While SolidWorks is displaying your body object with [Body::Display](Body__Display.htm), do not release it explicitly or implicitly. Before releasing or allowing other applications to release the body object, you must stop it from being displayed using [Body::Hide](Body__Hide.htm).

COM applications should avoid explicitly releasing the body object by calling Body->Release() while it is displayed by SolidWorks. Dispatch applications should avoid allowing the body object to go out of scope while it is displayed by SolidWorks, and destroyed when ReleaseDispatch is automatically called. Dispatch applications should also avoid explicitly releasing the body object by calling ReleaseDispatch while it is displayed by SolidWorks.
