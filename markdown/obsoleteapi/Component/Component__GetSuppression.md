---
title: "Component::GetSuppression"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetSuppression.htm"
---

# Component::GetSuppression

This method is obsolete and has been superseded by [Component2::GetSuppression](sldworksAPI.chm::/Component2/Component2__GetSuppression.htm).

Description

This method provides access to the suppression state of this component.

Syntax (OLE Automation)

Suppression= Component.GetSuppression

| Return: | (long) Suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |

Syntax (COM)

status = Component->GetSuppression( &Suppression )

| Output: | (long) Suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method to determine if the component is suppressed, lightweight, or fully resolved. Knowing the suppression state of the component is critical because lightweight and suppressed components contain only a small subset of data compared with a fully resolved component. For more information, see Working With Lightweight Components.
