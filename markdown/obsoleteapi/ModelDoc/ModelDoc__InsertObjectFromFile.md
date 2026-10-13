---
title: "ModelDoc::InsertObjectFromFile"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertObjectFromFile.htm"
---

# ModelDoc::InsertObjectFromFile

This method is obsolete and has been superseded by [ModelDoc2::InsertObjectFromFile](../ModelDoc2/ModelDoc2__InsertObjectFromFile.htm).

Description

This method adds an OLE object from a specified file and inserts it at the location specified.

Syntax (OLE Automation)

retval = ModelDoc.InsertObjectFromFile ( filePath, createLink, x, y, z )

| Input: | (BSTR) filePath | Full path name to the file being inserted |
| --- | --- | --- |
| Input: | (BOOL) createLink | TRUE to create a link to the file, FALSE to embed the file |
| Input: | (double) x | X component of the location to insert the object |
| Input: | (double) y | Y component of the location to insert the object |
| Input: | (double) z | Z component of the location to insert the object |
| Return: | (BOOL) retval | TRUE if the operation was successful, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertObjectFromFile ( filePath, createLink, x, y, z, &retval )

| Input: | (BSTR) filePath | Full path name to the file being inserted |
| --- | --- | --- |
| Input: | (BOOL) createLink | TRUE to create a link to the file, FALSE to embed the file |
| Input: | (double) x | X component of the location to insert the object |
| Input: | (double) y | Y component of the location to insert the object |
| Input: | (double) z | Z component of the location to insert the object |
| Output: | (VARIANT_BOOL) retval | TRUE if the operation was successful, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Currently, only the DrawingDoc object uses the x,y,z coordinate position. The PartDoc and AssemblyDoc objects place the inserted object at the upper-right hand corner of the ModelView object.
