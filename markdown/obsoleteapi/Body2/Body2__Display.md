---
title: "Body2::Display"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__Display.htm"
---

# Body2::Display

This method is obsolete and superseded by [Body2::Display2](Body2__Display2.htm).

Description

This method displays a temporary body object in the context of the specified part.

Syntax (OLE Automation)

void Body2.Display ( part, color)

| Input: | (LPDISPATCH) part | Pointer to Dispatch object, the part |
| --- | --- | --- |
| Input: | (long) color | Part color |

Syntax (COM)

status = Body2->IDisplay ( part, color )

| Input: | (LPPARTDOC) part | Pointer to the part |
| --- | --- | --- |
| Input: | (long) color | Part color |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

While SolidWorks is displaying your body object using Body2::Display, do not release it explicitly or implicitly. Before releasing or allowing the Body2 object to be released, call Body2::Hide to prevent it from being displayed.

COM applications can call Body2->Release() to avoid explicitly releasing the Body2 object while it is being displayed.

Dispatch applications should avoid:

- allowing the Body2 object to go out of scope while it is being displayed.
- explicitly releasing the Body2 object by calling ReleaseDispatch while it is being displayed by SolidWorks.
