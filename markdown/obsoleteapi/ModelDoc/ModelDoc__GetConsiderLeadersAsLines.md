---
title: "ModelDoc::GetConsiderLeadersAsLines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetConsiderLeadersAsLines.htm"
---

# ModelDoc::GetConsiderLeadersAsLines

This method is obsolete and has been superseded by ModelDoc2::GetConsiderLeadersAsLines.

Description

This method determines if the display data of a leader should be included as lines when the lines are retrieved from a view or annotation in this document.

Syntax (OLE Automation)

retval = ModelDoc.GetConsiderLeadersAsLines ( )

| Return: | (BOOL) retval | TRUE if leaders should be returned as line data, FALSE if leaders should not be returned as line data |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetConsiderLeadersAsLines ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if leaders should be returned as line data, FALSE if leaders should not be returned as line data |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

The GetLeaderCount and GetLeaderAtIndex APIs that are supported by several different annotations return the information about where the vertices of the leader are located. The GetLineCount and GetLinesAtIndex APIs also return the leader information as part of its line information. Depending on what your program is trying to accomplish and which APIs it is using, this duplication of information may not be desirable. ModelDoc::SetConsiderLeadersAsLines controls this behavior by setting a flag on the document that indicates whether or not the leader information should be returned as part of the line information or not.

This API gets the current behavior for this document.
