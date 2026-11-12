---
title: "Component::SelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__SelectByMark.htm"
---

# Component::SelectByMark

This method is obsolete and has been superseded by [Component2::SelectByMark](../Component2/Component2__SelectByMark.htm).

Description

This method selects the component and either appends it to the selection list or replaces the entire selection list. The selection is also marked with the value specified. This mark is used by certain API functions that require multiple selections.

Syntax (OLE Automation)

retval = Component.SelectByMark ( appendFlag, mark )

| Input: | (BOOL) appendFlag | TRUE appends the current selection list, FALSE replaces the selection list |
| --- | --- | --- |
| Input: | (long) mark | Number you want to use as a mark |
| Return: | (BOOL) retval | TRUE if the feature was selected, FALSE if not |

Syntax (COM)

status = Component->SelectByMark ( appendFlag, mark, &retval )

| Input: | (VARIANT_BOOL) appendFlag | TRUE appends the current selection list, FALSE replaces the selection list |
| --- | --- | --- |
| Input: | (long) mark | Number you want to use as a mark |
| Output: | (VARIANT_BOOL) retval | TRUE if the feature was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The mark value is used by certain API functions that require ordered entity selection.

Use ModelDoc2::SelectByMark instead of using this method. This method does not work well when a PropertyManager page is open or a command is running. ModelDoc2::SelectByMark handles selection correctly whether or not a command is running.
