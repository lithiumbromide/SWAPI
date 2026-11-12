---
title: "DrawingDoc::CreateFlatPatternViewFromModelView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateFlatPatternViewFromModelView.htm"
---

# DrawingDoc::CreateFlatPatternViewFromModelView

This method is obsolete and has been superseded by [DrawingDoc::CreateFlatPatternViewFromModelView2](DrawingDoc__CreateFlatPatternViewFromModelView2.htm).

Description

This method creates a flat pattern view from a model view at the specified location.

Syntax (OLE Automation)

retval = DrawingDoc.CreateFlatPatternViewFromModelView ( modelName, configName, locX, locY, locZ )

| Input: | (BSTR) modelName | Name of the model in the flat pattern view |
| --- | --- | --- |
| Input: | (BSTR) configName | Name of the configuration |
| Input: | (double) locX | X location of view |
| Input: | (double) locY | Y location of view |
| Input: | (double) locZ | Z location of view |
| Return: | (BOOL) retval | TRUE if the view was successfully created, FALSE if not |

Syntax (COM)

status = DrawingDoc->CreateFlatPatternViewFromModelView ( modelName, configName, locX, locY, locZ, &retval )

| Input: | (BSTR) modelName | Name of the model in the flat pattern view |
| --- | --- | --- |
| Input: | (BSTR) configName | Name of the configuration |
| Input: | (double) locX | X location of view |
| Input: | (double) locY | Y location of view |
| Input: | (double) locZ | Z location of view |
| Output: | (VARIANT_BOOL) retval | TRUE if the view was successfully created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
