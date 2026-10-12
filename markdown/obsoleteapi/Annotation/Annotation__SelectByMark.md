---
title: "Annotation::SelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__SelectByMark.htm"
---

# Annotation::SelectByMark

This method is obsolete and has been superseded by [Annotation::Select2](sldworksAPI.chm::/Annotation/Annotation__Select2.htm).

Description

This method selects the annotation and either appends it to the selections or replaces the entire selection list. The selection is also marked with the value specified. This mark is used by certain API functions that require multiple selections.

Syntax (OLE Automation)

retval = Annotation.SelectByMark ( appendFlag, mark )

| Input: | (BOOL) appendFlag | TRUE if the annotation is to be appended to the selection list, FALSE if the annotation replaces the current selection list |
| --- | --- | --- |
| Input: | (long) mark | Value you want to use as a mark; this value is used by other functions that require ordered selection |
| Return: | (BOOL) retval | TRUE if the annotation was selected |

Syntax (COM)

status = Annotation->SelectByMark ( appendFlag, mark, &retval )

| Input: | (VARIANT_BOOL) appendFlag | TRUE if the annotation is to be appended to the selection list, FALSE if the annotation replaces the current selection list |
| --- | --- | --- |
| Input: | (long) mark | Value you want to use as a mark; this value is used by other functions that require ordered selection |
| Output: | (VARIANT_BOOL) retval | TRUE if the annotation was selected |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDoc2::SelectByMark instead of using this method. This method does not work well when a PropertyManager page is open or a command is running. ModelDoc2::SelectByMark handles selection correctly whether or not a command is running.
