---
title: "Component::IsSuppressed"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__IsSuppressed.htm"
---

# Component::IsSuppressed

This method is obsolete and has been superseded by [Component2::IsSuppressed](sldworksAPI.chm::/Component2/Component2__IsSuppressed.htm).

Description

This method determines if this component is suppressed. The suppression state of this component may vary based on the active configuration.

Syntax (OLE Automation)

retval = Component.IsSuppressed ()

| Return: | (BOOL) retval | TRUE if this component is suppressed, FALSE if it was not |
| --- | --- | --- |

Syntax (COM)

status = Component->IsSuppressed ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if this component is suppressed, FALSE if it was not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You might want to use [Component::GetSuppression](Component__GetSuppression.htm), which returns the specific suppression state of the component.

NOTE: For lightweight components, Component::IsSuppressed returns TRUE.
