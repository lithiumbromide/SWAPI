---
title: "ModelDoc::SaveBMP"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SaveBMP.htm"
---

# ModelDoc::SaveBMP

This method is obsolete and has been superseded by [ModelDoc2::SaveBMP](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SaveBMP.htm).

Description

This method saves the current view as bitmap file.

Syntax (OLE Automation)

retval = ModelDoc.SaveBMP ( filenameIn, widthIn, heightIn )

| Input: | ( BSTR) filenameIn | Complete filename and path of the new bitmap file |
| --- | --- | --- |
| Input: | ( long) widthIn | Width of the bitmap |
| Input: | ( long) heightIn | Height of the bitmap |
| Return: | ( BOOL) retval | TRUE if file was created successfully |

Syntax (COM)

status = ModelDoc->SaveBMP (filenameIn, widthIn, heightIn, &retval )

| Input: | ( BSTR) filenameIn | Complete filename and Path of the new bitmap file |
| --- | --- | --- |
| Input: | ( long) widthIn | Width of the bitmap |
| Input: | ( long) heightIn | Height of the bitmap |
| Output: | (VARIANT_ BOOL) retval | TRUE if file was created successfully |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The filenameIn argument should include the full path to the file to be created. The extension should be .bmp.

If the widthIn or the heightIn argument is less than or equal to 0, the view size is based on the current window size.
