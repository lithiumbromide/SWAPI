---
title: "Component2::SetSuppression"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__SetSuppression.htm"
---

# Component2::SetSuppression

This method is obsolete and has been superseded by [Component2::SetSuppression2](sldworksAPI.chm::/Component2/Component2__SetSuppression2.htm).

Description

This method sets the suppression state of this component.

Syntax (OLE Automation)

retval = Component2.SetSuppression( Suppression )

| Input: | (long) Suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |
| Return: | (long) retval | One of the values defined in swSuppressionError_e |

Syntax (COM)

status = Component2->SetSuppression( Suppression, &retval )

| Input: | (long) Suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |
| Output: | (long) retval | One of the values defined in swSuppressionError_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
