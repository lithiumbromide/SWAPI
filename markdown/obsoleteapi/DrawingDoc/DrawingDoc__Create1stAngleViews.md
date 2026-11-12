---
title: "DrawingDoc::Create1stAngleViews"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__Create1stAngleViews.htm"
---

# DrawingDoc::Create1stAngleViews

This method is obsolete and has been superseded by [DrawingDoc](sldworksAPI.chm::/DrawingDoc/DrawingDoc__Create1stAngleViews2.htm)::Create1stAngleViews2.

Description

This method creates standard three orthographic views (first angle projection) for the specified model.

Syntax (OLE Automation)

retval = DrawingDoc.Create1stAngleViews ( modelName)

| Input: | (BSTR) modelName | Name of the document from which to create views |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = DrawingDoc->Create1stAngleViews ( modelName, &retval )

| Input: | (BSTR) modelName | Name of the document from which to create views |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
