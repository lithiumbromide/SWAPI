---
title: "ModelDoc2::EditBalloonProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__EditBalloonProperties.htm"
---

# ModelDoc2::EditBalloonProperties

This method is obsolete and has been superseded by [Note::SetBalloon](sldworksAPI.chm::/Note/Note__SetBalloon.htm) and [Note::SetBomBalloonText](sldworksAPI.chm::/Note/Note__SetBomBalloonText.htm).

Description

This method edits the selected balloon's properties

Syntax (OLE Automation)

retval = ModelDoc2.EditBalloonProperties ( style, size, upperTextStyle, upperText, lowerTextStyle, lowerText )

| Input: | (long) style | Style of balloon as defined in swBalloonStyle_e |
| --- | --- | --- |
| Input: | (long) size | Balloon size as defined in swBalloonFit_e |
| Input: | (long) upperTextStyle | Upper-text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) upperText | Text for the upper-text in this balloon |
| Input: | (long) lowerTextStyle | Lower-text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) lowerText | Text for the lower-text in this balloon |
| Return: | (LPDISPATCH) retval | Pointer to the balloon being edited |

Syntax (COM)

status = ModelDoc2->EditBalloonProperties ( style, size, upperTextStyle, upperText, lowerTextStyle, lowerText, &retval )

| Input: | (long) style | Style of balloon as defined in swBalloonStyle_e |
| --- | --- | --- |
| Input: | (long) size | Balloon size as defined in swBalloonFit_e |
| Input: | (long) upperTextStyle | Upper-text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) upperText | Text for the upper-text in this balloon |
| Input: | (long) lowerTextStyle | Lower-text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) lowerText | Text for the lower-text in this balloon |
| Output: | (LPDISPATCH) retval | Pointer to the balloon being edited. |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
