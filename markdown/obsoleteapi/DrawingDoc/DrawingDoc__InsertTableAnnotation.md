---
title: "DrawingDoc::InsertTableAnnotation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertTableAnnotation.htm"
---

# DrawingDoc::InsertTableAnnotation

This method is obsolete and has been superseded by [DrawingDoc::InsertTableAnnotation2](sldworksAPI.chm::/DrawingDoc/DrawingDoc__InsertTableAnnotation2.htm).

Description

This method inserts a table annotation in this drawing.

Syntax (OLE Automation)

retval = DrawingDoc.InsertTableAnnotation ( X, Y, AnchorType, Rows, Columns)

| Input: | (double) X | X coordinate at which to insert this table annotation |
| --- | --- | --- |
| Input: | (double) Y | Y coordinate at which to insert this table annotation |
| Input: | (long) AnchorType | Type of anchor as defined by swBOMConfigurationAnchorType_e (see Remarks ) |
| Input: | (long) Rows | Number of rows in the table annotation |
| Input: | (long) Columns | Number of columns in the table annotation |
| Output: | (LPTABLEANNOTATION*) retval | Pointer to the newly created TableAnnotation object |

Syntax (COM)

status = DrawingDoc->InsertTableAnnotation ( X, Y, AnchorType, Rows, Columns, &retval)

| Input: | (double) X | X coordinate at which to insert this table annotation |
| --- | --- | --- |
| Input: | (double) Y | Y coordinate at which to insert this table annotation |
| Input: | (long) AnchorType | Type of anchor as defined by swBOMConfigurationAnchorType_e (see Remarks ) |
| Input: | (long) Rows | Number of rows in the table annotation |
| Input: | (long) Columns | Number of columns in the table annotation |
| Output: | (LPTABLEANNOTATION*) retval | Pointer to the newly created TableAnnotation object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The anchor helps to define which corner is represented by the X and Y values. After the table is inserted, the anchor does not mean anything in the context of the general table. Because this method is used for general, BOM, and revision tables, TableAnnotation::Anchored is only meaningful for the BOM and revision tables.
