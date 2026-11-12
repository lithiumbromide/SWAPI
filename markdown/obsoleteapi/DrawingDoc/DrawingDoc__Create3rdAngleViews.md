---
title: "DrawingDoc::Create3rdAngleViews"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__Create3rdAngleViews.htm"
---

# DrawingDoc::Create3rdAngleViews

This method is obsolete and has been superseded by [DrawingDoc::](sldworksAPI.chm::/DrawingDoc/DrawingDoc__Create3rdAngleViews2.htm)Create3rdAngleViews2.

Description

This method creates standard three orthographic views (third angle projection) for the specified model.

Syntax (OLE Automation)

retval = DrawingDoc.Create3rdAngleViews ( modelName)

| Input: | (BSTR) modelName | Name of the document from which to create views |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = DrawingDoc->Create3rdAngleViews ( modelName, &retval )

| Input: | (BSTR) modelName | Name of the document from which to create views |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
