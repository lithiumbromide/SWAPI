---
title: "Sheet::GetOLEObjectSettings"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sheet/Sheet__GetOLEObjectSettings.htm"
---

# Sheet::GetOLEObjectSettings

This method is obsolete and has been superseded by [SwOLEObject::Aspect](sldworksAPI.chm::/SwOLEObject/SwOLEObject__Aspect.htm), [SwOLEObject::Boundaries](sldworksAPI.chm::/SwOLEObject/SwOLEObject__Boundaries.htm), and [SwOLEObject::Buffer](sldworksAPI.chm::/SwOLEObject/SwOLEObject__Buffer.htm).

Description

This method gets settings for an OLE object.

Syntax (OLE Automation)

retval = Sheet.GetOLEObjectSettings ( index, &byteCount, &aspect )

| Input: | (long) index | Index of the OLE object |
| --- | --- | --- |
| Output: | (long) byteCount | Size of the byte array for the data object |
| Output: | (long) aspect | Viewing aspect of the object ( uses DVASPECT enumeration) |
| Return: | (VARIANT) retval | Box corner: top-left and bottom-right positions in sheet coordinates |

Syntax (COM)

status = Sheet->IGetOLEObjectSettings ( index, &byteCount, &aspect, &position, &retval )

| Input: | (long) index | Index of the OLE object |
| --- | --- | --- |
| Output: | (long) byteCount | Size of the byte array for the data object |
| Output: | (long) aspect | Viewing aspect of the object ( uses DVASPECT enumeration) |
| Output: | (double) position | Box corner: top-left and bottom-right positions in sheet coordinates |
| Output: | (VARIANT_BOOL) retval | TRUE if the settings are successfully returned, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See the MSDN documentation for details about the DVASPECT enumeration.

The aspect argument uses the DVASPECT enumeration, which has the following values:

- DVASPECT_CONTENT = 1
- DVASPECT_THUMBNAIL = 2
- DVASPECT_ICON = 4
- DVASPECT_DOCPRINT = 8

The buffer data is in the format obtained from the Microsoft MFC object COleClientItem using the GetHGlobalFromILockBytes.
