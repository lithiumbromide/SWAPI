---
title: "SldWorks::NewDrawing2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__NewDrawing2.htm"
---

# SldWorks::NewDrawing2

This method is obsolete and has been superseded by [SldWorks::NewDocument](sldworksAPI.chm::/SldWorks/SldWorks__NewDocument.htm) or [SldWorks::INewDocument2](sldworksAPI.chm::/SldWorks/SldWorks__INewDocument2.htm).

Description

This method creates a new drawing document with a template or custom size. The drawing document is named automatically.

Syntax (OLE Automation)

retval = SldWorks.NewDrawing2 ( templateToUse, templateName, paperSize, width, height)

| Input: | (long) templateToUse | Type of template to use as defined as swDwgTemplates_e |
| --- | --- | --- |
| Input: | (BSTR) templateName | Name of custom template with full directory path if using swDwgTemplateCustom |
| Input: | (long) paperSize | Size of paper if using swDwgTemplateNone as defined in swDwgPaperSizes_e |
| Input: | (double) width | Paper width if using swDwgTemplateNone and swDwgPapersUserDefined |
| Input: | (double) height | Paper height if using swDwgTemplateNone and swDwgPapersUserDefined |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created drawing or NULL if the operation fails |

Syntax (COM)

status = SldWorks->INewDrawing2 ( templateToUse, templateName, paperSize, width, height, &retval )

| Input: | (long) templateToUse | Type of template to use as defined as swDwgTemplates_e |
| --- | --- | --- |
| Input: | (BSTR) templateName | Name of custom template with full directory path if using swDwgTemplateCustom |
| Input: | (long) paperSize | Size of paper if using swDwgTemplateNone as defined in swDwgPaperSizes_e |
| Input: | (double) width | Paper width if using swDwgTemplateNone and swDwgPapersUserDefined |
| Input: | (double) height | Paper height if using swDwgTemplateNone and swDwgPapersUserDefined |
| Output: | (LPDRAWINGDOC) retval | Pointer to a newly created drawing or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Calling this method erases any settings made with the SldWorks::PreSelectDwgTemplateSize.

If the custom template or standard template file is not found, then the drawing is created without a template, as if swDwgTemplateNone was specified. If that happens, the paperSize argument is used to determine the size of the drawing. If the paper size is swDwgPapersUserDefined, then the width and height values are used to determine the size of the drawing. If the paperSize, width, or height is invalid, the paper size defaults to swDwgPaperAsize.

To set the document title without saving the file, see ModelDoc2::SetTitle2.
