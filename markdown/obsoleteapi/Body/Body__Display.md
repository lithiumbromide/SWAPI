---
title: "Body::Display"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__Display.htm"
---

# Body::Display

This method is obsolete and has been superseded by [Body2::Display](../Body2/Body2__Display2.htm).

Description

This method displays a temporary body object in the context of the specified part.

Syntax (OLE Automation)

void Body.Display ( part, color)

| Input: | (LPDISPATCH) part | Pointer to dispatch object, the part |
| --- | --- | --- |
| Input: | (long) color | Desired color |

Syntax (COM)

status = Body->IDisplay ( part, color )

| Input: | (LPPARTDOC) part | Pointer to the part |
| --- | --- | --- |
| Input: | (long) color | Desired color |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

While SolidWorks is using this method to display this Body object, it cannot be explicitly or implicitly released. Before releasing or allowing the Body object to be released, use Body::Hide to prevent SolidWorks from displaying the body.

COM applications can use Body->Release() to avoid explicitly releasing the body object while it is displayed. Dispatch applications should not allow the Body object to go out of scope while it is displayed, or be destroyed when the ReleaseDispatch method is called automatically. Dispatch applications should also avoid calling ReleaseDispatch to explicitly release the body object while it is displayed.
