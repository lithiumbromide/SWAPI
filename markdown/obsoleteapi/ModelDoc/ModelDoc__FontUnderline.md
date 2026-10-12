---
title: "ModelDoc::FontUnderline"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FontUnderline.htm"
---

# ModelDoc::FontUnderline

This method is obsolete and has been superseded by [ModelDoc2::FontUnderline](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FontUnderline.htm).

Description

This method enables or disables the underline font style in the selected notes, dimensions, and Gtols.

Syntax (OLE Automation)

(void) ModelDoc.FontUnderline ( underline )

| Input: | (Boolean) underline | TRUE for underline enabled, FALSE for disabled |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->FontUnderline ( underline )

| Input: | (VARIANT_BOOL)underline | TRUE for Underline enabled, FALSE for disabled |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can also use the TextFormat object for full control of text formatting. You can obtain this object by using the GetTextFormat interfaces.
