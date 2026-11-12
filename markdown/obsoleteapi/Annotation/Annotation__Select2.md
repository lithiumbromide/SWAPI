---
title: "Annotation::Select2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__Select2.htm"
---

# Annotation::Select2

This method is obsolete and has been superseded by [Annotation::Select3](sldworksAPI.chm::/Annotation/Annotation__Select3.htm).

Description

This method selects and marks this annotation.

Syntax (OLE Automation)

retval = Annotation.Select2 ( Append, Mark )

| Input: | (BOOL) Append | TRUE appends the selections to the current selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this value is used by other functions that require ordered selection |
| Output: | (BOOL) retval | TRUE if the annotation was selected, FALSE if not |

Syntax (COM)

status = Annotation->Select2 ( Append, Mark, &retval )

| Input: | (VARIANT_BOOL) Append | TRUE appends the selections to the current selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this value is used by other functions that require ordered selection |
| Output: | (VARIANT_BOOL) retval | TRUE if the annotation was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDoc2::SelectByID instead of using this method. This method does not work well when a PropertyManager page is open or a command is running. ModelDoc2::SelectByID handles selection correctly whether or not a command is running.
