---
title: "ModelDoc::EditBalloonProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditBalloonProperties.htm"
---

# ModelDoc::EditBalloonProperties

This method is obsolete and has been superseded by [ModelDoc2::EditBalloonProperties](../ModelDoc2/ModelDoc2__EditBalloonProperties.htm).

Description

This method edits the selected balloon's properties.

Syntax (OLE Automation)

retval = ModelDoc.EditBalloonProperties ( style, size, upperTextStyle, upperText, lowerTextStyle, lowerText )

| Input: | (long) style | Style of balloon you wish to use as defined in swBalloonStyle_e |
| --- | --- | --- |
| Input: | (long) size | Balloon size you wish to use as defined in swBalloonFit_e |
| Input: | (long) upperTextStyle | Upper text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) upperText | Text string for the upper text in this balloon |
| Input: | (long) lowerTextStyle | Lower text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) lowerText | Text string for the lower text in this balloon |
| Return: | (LPDISPATCH) retval | Pointer to the balloon that is being edited |

Syntax (COM)

status = ModelDoc->EditBalloonProperties ( style, size, upperTextStyle, upperText, lowerTextStyle, lowerText, &retval )

| Input: | (long) style | Style of balloon you wish to use as defined in swBalloonStyle_e |
| --- | --- | --- |
| Input: | (long) size | Balloon size you wish to use as defined in swBalloonFit_e |
| Input: | (long) upperTextStyle | Upper text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) upperText | Text string for the upper text in this balloon. |
| Input: | (long) lowerTextStyle | Lower text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) lowerText | Text string for the lower text in this balloon |
| Output: | (LPDISPATCH) retval | Pointer to the balloon that is being edited |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
