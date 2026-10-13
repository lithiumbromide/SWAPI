---
title: "Annotation::GetLeader"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__GetLeader.htm"
---

# Annotation::GetLeader

This method is obsolete and has been superseded by [Annotation::GetLeaderStyle](sldworksAPI.chm::/Annotation/Annotation__GetLeaderStyle.htm).

Description

This method gets the leader display setting for this annotation.

Syntax (OLE Automation)

retval = Annotation.GetLeader ( )

| Return: | (BOOL) retval | TRUE if leader display is enabled for this annotation, FALSE if leader display is disabled for this annotation |
| --- | --- | --- |

Syntax (COM)

status = Annotation->GetLeader ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if leader display is enabled for this annotation, FALSE if leader display is disabled for this annotation |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use Annotation::SetLeader2 to enable or disable leader display.

NOTE: Dimension annotations do not have leaders. Therefore, this method always returns FALSE for dimension annotations.
