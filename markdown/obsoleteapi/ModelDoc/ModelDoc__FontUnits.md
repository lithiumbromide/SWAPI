---
title: "ModelDoc::FontUnits"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FontUnits.htm"
---

# ModelDoc::FontUnits

This method is obsolete and has been superseded by [ModelDoc2::FontUnits](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FontUnits.htm).

Description

This method changes the height, specified in current system units, of the font in the selected notes, dimensions, and Gtols.

Syntax (OLE Automation)

(void) ModelDoc.FontUnits ( units )

| Input: | (double) units | Specifies the height, in current system units (for example, inches, millimeters, and so on) of the font |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->FontUnits ( units )

| Input: | (double) units | Specifies the height, in current system units (for example, inches, millimeters, and so on) of the font |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can also use the TextFormat object for full control of text formatting. You can obtain this object by using the GetTextFormat interfaces.
