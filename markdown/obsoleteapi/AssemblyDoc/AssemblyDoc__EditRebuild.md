---
title: "AssemblyDoc::EditRebuild"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__EditRebuild.htm"
---

# AssemblyDoc::EditRebuild

This method is obsolete and has been superseded by [ModelDoc2::EditRebuild3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__EditRebuild3.htm).

Description

This method rebuilds the assembly.

Syntax (OLE Automation)

void AssemblyDoc.EditRebuild ()

Syntax (COM)

status = AssemblyDoc->EditRebuild ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

There are certain instances where SolidWorks prohibits this command. For example, if the user is interactively editing the properties of a face, then SolidWorks prohibits this method because calling it would invalidate all of the pointers in the document. If this method is not blocked, then closing the Face-Properties dialog might cause problems because the dialog box is looking for the original face pointer.
