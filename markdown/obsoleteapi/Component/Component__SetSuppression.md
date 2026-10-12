---
title: "Component::SetSuppression"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__SetSuppression.htm"
---

# Component::SetSuppression

This method is obsolete and has been superseded by [Component2::SetSuppression](../Component2/Component2__SetSuppression.htm).

Description

This method controls the suppression state of this component.

Syntax (OLE Automation)

retval = Component.SetSuppression( Suppression )

| Input: | (long) Suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |
| Return: | (long) retval | Error code as defined in swSuppressionError_e |

Syntax (COM)

status = Component->SetSuppression( Suppression, &retval )

| Input: | (long) Suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |
| Output: | (long) retval | Error code as defined in swSuppressionError_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You cannot set a component to lightweight (for example, Suppression = swComponentLightweight is not valid).
