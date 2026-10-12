---
title: "ModelDoc2::InsertObjectFromFile"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertObjectFromFile.htm"
---

# ModelDoc2::InsertObjectFromFile

This method is obsolete and has been superseded by [ModelDocExtension::InsertObjectFromFile](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__InsertObjectFromFile.htm).

Description

This method adds an OLE object from a specified file and inserts it at the location specified.

Syntax (OLE Automation)

retval = ModelDoc2.InsertObjectFromFile ( filePath, createLink, x, y, z )

| Input: | (BSTR) filePath | Full path name to the file to insert |
| --- | --- | --- |
| Input: | (BOOL) createLink | TRUE to create a link to the file, FALSE to embed the file |
| Input: | (double) x | X component of the location to insert the object |
| Input: | (double) y | Y component of the location to insert the object |
| Input: | (double) z | Z component of the location to insert the object |
| Return: | (BOOL) retval | TRUE if the operation was successful, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->InsertObjectFromFile ( filePath, createLink, x, y, z, &retval )

| Input: | (BSTR) filePath | Full path name to the file to insert |
| --- | --- | --- |
| Input: | (BOOL) createLink | TRUE to create a link to the file, FALSE to embed the file |
| Input: | (double) x | X component of the location to insert the object |
| Input: | (double) y | Y component of the location to insert the object |
| Input: | (double) z | Z component of the location to insert the object |
| Output: | (VARIANT_BOOL) retval | TRUE if the operation was successful, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Currently, only the drawing documents use the x,y,z coordinate position. Part and assembly documents l place the inserted object at the upper-right corner of the model view.
