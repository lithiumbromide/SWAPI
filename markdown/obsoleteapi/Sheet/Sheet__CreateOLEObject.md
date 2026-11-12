---
title: "Sheet::CreateOLEObject"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sheet/Sheet__CreateOLEObject.htm"
---

# Sheet::CreateOLEObject

This method is obsolete and has been superseded by [ModelDocExtension::CreateOLEObject](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__CreateOLEObject.htm).

Description

This method creates an OLE object from data. This method is primarily intended to allow the translation of a drawing that contains embedded objects.

Syntax (OLE Automation)

retval = Sheet.CreateOLEObject ( aspect, position, buffer )

| Input: | (long) aspect | Viewing aspect of the object ( uses DVASPECT enumeration) |
| --- | --- | --- |
| Input: | (VARIANT) position | Box corner top-left and bottom-right positions in sheet coordinates |
| Input: | (VARIANT) buffer | Data for the OLE object |
| Return: | (BOOL) retval | TRUE if the object is successfully created, FALSE if not |

Syntax (COM)

status = Sheet->CreateOLEObject ( aspect, &position, byteCount, &buffer, &retval )

| Input: | (long) aspect | Viewing aspect of the object ( uses DVASPECT enumeration) |
| --- | --- | --- |
| Input: | (double) position[6] | Box corner top-left and bottom-right positions in sheet coordinates |
| Input: | (long) byteCount | Size of the byte array for the data object |
| Input: | (BYTE)* buffer | Data for the OLE object |
| Output: | (VARIANT_BOOL) retval | TRUE if the object is successfully created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

See the MSDN documentation for details about the DVASPECT enumeration.

The aspect argument uses the DVASPECT enumeration, which has the following values:

- DVASPECT_CONTENT = 1
- DVASPECT_THUMBNAIL = 2
- DVASPECT_ICON = 4
- DVASPECT_DOCPRINT = 8

The buffer data is in the format obtained from the Microsoft MFC object COleClientItem using the GetHGlobalFromILockBytes.
