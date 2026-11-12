---
title: "Component::GetConstrainedStatus"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetConstrainedStatus.htm"
---

# Component::GetConstrainedStatus

This method is obsolete and has been superseded by [Component2::GetConstrainedStatus](sldworksAPI.chm::/Component2/Component2__GetConstrainedStatus.htm).

Description

This method gets the constrained status of this component.

Syntax (OLE Automation)

retval = Component.GetConstrainedStatus ( )

| Return: | (long) retval | Contrained status as defined in swConstrainedStatus_e |
| --- | --- | --- |

Syntax (COM)

status = Component->GetConstrainedStatus ( &retval )

| Output: | (long) retval | Contrained status as defined in swConstrainedStatus_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
