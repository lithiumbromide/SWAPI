---
title: "Body::GetType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body_GetType.htm"
---

# Body::GetType

This method is obsolete and has been superseded by [Body2::GetType](sldworksAPI.chm::/Body2/Body2__GetType.htm).

Description

This method gets the body type.

Syntax (OLE Automation)

retval = Body.GetType ( )

| Return: | (long) retval | Body type as defined in swBodyType_e |
| --- | --- | --- |

Syntax (COM)

status = Body->GetType ( &retval )

| Output: | (long) retval | Body type as defined in swBodyType_e |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Empty is a special case that SolidWorks returns if the interface pointer or underlying body pointer is NULL, indicating the body is non-existent.
