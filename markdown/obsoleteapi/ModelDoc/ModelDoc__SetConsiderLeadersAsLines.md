---
title: "ModelDoc::SetConsiderLeadersAsLines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetConsiderLeadersAsLines.htm"
---

# ModelDoc::SetConsiderLeadersAsLines

This method is obsolete and has been superseded by [ModelDoc2::SetConsiderLeadersAsLines](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetConsiderLeadersAsLines.htm).

Description

This method sets a flag on the document that indicates whether or not the display data of a leader should be included as lines when the lines are retrieved from a view or annotation in this document.

Syntax (OLE Automation)

retval = ModelDoc.SetConsiderLeadersAsLines ( leadersAsLines )

| Input: | (BOOL) leadersAsLines | TRUE if leaders should be returned as line data, FALSE if leaders should not be returned as line data |
| --- | --- | --- |
| Return: | (BOOL) retval | Original value of the flag before this API was called |

Syntax (COM)

status = ModelDoc->SetConsiderLeadersAsLines ( leadersAsLines, &retval )

| Input: | (VARIANT_BOOL) leadersAsLines | TRUE if leaders should be returned as line data, FALSE if leaders should not be returned as line data |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | Original value of the flag before this API was called |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

Use [ModelDoc::GetConsiderLeadersAsLines](ModelDoc__GetConsiderLeadersAsLines.htm) to determine the current behavior.
