---
title: "Feature::SelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__SelectByMark.htm"
---

# Feature::SelectByMark

This method is obsolete and has been superseded by [Feature::Select2](sldworksAPI.chm::/Feature/Feature__Select2.htm).

Description

This method selects and marks this feature.

Syntax (OLE Automation)

retval = Feature.SelectByMark ( appendFlag, mark )

| Input: | (BOOL) appendFlag | TRUE appends the feature to the selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Input: | (long) mark | Number you want to use as a mark |
| Return: | (BOOL) retval | TRUE if the feature was selected, FALSE if not |

Syntax (COM)

status = Feature->SelectByMark ( appendFlag, mark, &retval )

| Input: | (VARIANT_BOOL) appendFlag | TRUE appends the feature to the selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Input: | (long) mark | Number you want to use as a mark |
| Output: | (VARIANT_BOOL) retval | TRUE if the entity was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The selection mark is used by other functions that require multiple selections, such as InsertMfDraft2, InsertSplitLineSil, and InsertSplitLineProject.

Use [ModelDoc2::SelectByMark](../ModelDoc2/ModelDoc2__SelectByMark.htm) instead of this method. This method does not work well when a PropertyManager page is open or a command is running. ModelDoc2::SelectByMark handles selection correctly whether or not a command is running.
