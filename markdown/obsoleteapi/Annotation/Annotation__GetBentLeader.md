---
title: "Annotation::GetBentLeader"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__GetBentLeader.htm"
---

# Annotation::GetBentLeader

This method is obsolete and has been superseded by [Annotation::GetLeaderStyle](sldworksAPI.chm::/Annotation/Annotation__GetLeaderStyle.htm).

Description

This method gets the bent leader display setting for this annotation.

Syntax (OLE Automation)

retval = Annotation.GetBentLeader ( )

| Return: | (BOOL) retval | TRUE if bent leader display is enabled for this annotation, FALSE if bent leader display is disabled for this annotation |
| --- | --- | --- |

Syntax (COM)

status = Annotation->GetBentLeader ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if bent leader display is enabled for this annotation, FALSE if bent leader display is disabled for this annotation |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The bent leader display flag is a characteristic of the annotation, not of individual leaders. Therefore, you can get or set it whether or not leaders are currently displayed.
