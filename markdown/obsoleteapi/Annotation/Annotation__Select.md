---
title: "Annotation::Select"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__Select.htm"
---

# Annotation::Select

This method is obsolete and has been superseded by [Annotation::Select2](Annotation__Select2.htm).

Description

This method selects the annotation, and appends it to the selections or replaces the entire selection list.

Syntax (OLE Automation)

retval = Annotation.Select ( appendFlag )

| Input: | (BOOL) appendFlag | TRUE if the annotation is to be appended to the selection list, FALSE if the annotation replaces the selection list |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the annotation was selected |

Syntax (COM)

status = Annotation->Select ( appendFlag, &retval )

| Input: | (VARIANT_BOOL) appendFlag | TRUE if the annotation is to be appended to the selection list, FALSE if the annotation replaces the selection list |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the annotation was selected |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

Use ModelDoc2::SelectByID instead of using this method. This method does not work well when a PropertyManager page is open or a command is running. ModelDoc2::SelectByID handles selection correctly whether or not a command is running.
