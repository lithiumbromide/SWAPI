---
title: "Feature::Select"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__Select.htm"
---

# Feature::Select

This method is obsolete and has been superseded by [Feature::Select2](sldworksAPI.chm::/Feature/Feature__Select2.htm).

Description

This method selects the feature and either appends it to the selections or replaces the entire selection list.

Syntax (OLE Automation)

retval = Feature.Select ( appendFlag )

| Input: | (BOOL) appendFlag | TRUE appends the feature to the current selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the feature was selected, FALSE if not |

Syntax (COM)

status = Feature->Select ( appendFlag, &retval )

| Input: | (VARIANT_BOOL) appendFlag | TRUE appends the feature to the current selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the feature was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use [ModelDoc2::SelectByID](../ModelDoc2/ModelDoc2__SelectByID.htm) instead of this method. This method does not work well when a PropertyManager page is open or a command is running. ModelDoc2::SelectByID handles selection correctly whether or not a command is running.
