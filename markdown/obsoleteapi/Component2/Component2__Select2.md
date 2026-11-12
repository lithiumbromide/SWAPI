---
title: "Component2::Select2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__Select2.htm"
---

# Component2::Select2

This method is obsolete and has been superseded by [Component2::Select3](sldworksAPI.chm::/Component2/Component2__Select3.htm).

Description

This method selects this component and marks it.

Syntax (OLE Automation)

retval = Component2.Select2 ( Append, Mark )

| Input: | (BOOL) Append | TRUE appends the selection to the selection list, FALSE replaces the selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark |
| Output: | (BOOL) retval | TRUE if the component was selected, FALSE if not |

Syntax (COM)

status = Component2->Select2 ( Append, Mark, &retval )

| Input: | (VARIANT_BOOL) Append | TRUE appends the selection to the selection list, FALSE replaces the selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark |
| Output: | (VARIANT_BOOL) retval | TRUE if the component was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The Mark value is used by API functions that require ordered selection.

You cannot select the root component.
