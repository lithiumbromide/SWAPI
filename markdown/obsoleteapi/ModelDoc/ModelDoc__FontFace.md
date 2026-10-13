---
title: "ModelDoc::FontFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FontFace.htm"
---

# ModelDoc::FontFace

This method is obsolete and has been superseded by [ModelDoc2::FontFace](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FontFace.htm).

Description

This method changes font face in the selected notes, dimensions, and Gtols.

Syntax (OLE Automation)

(void) ModelDoc.FontFace ( face )

| Input: | (BSTR) face | Points to a null-terminated string that specifies the font face name (for example, Times New Roman) |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->FontFace ( face )

| Input: | (BSTR) face | Points to a null-terminated string that specifies the font face name (for example, Times New Roman) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

You can also refer to the TextFormat object for full control of text formatting. You obtain this object by using the GetTextFormat interfaces.
