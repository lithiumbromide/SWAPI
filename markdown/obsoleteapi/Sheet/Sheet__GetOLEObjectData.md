---
title: "Sheet::GetOLEObjectData"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sheet/Sheet__GetOLEObjectData.htm"
---

# Sheet::GetOLEObjectData

This method is obsolete and has been superseded by [SwOLEObject](sldworksAPI.chm::/SwOLEObject/SwOLEObject.htm).

Description

This method gets data for an OLE object.

Syntax (OLE Automation)

void Sheet.GetOLEObjectData ( index, &buffer, &retval )

| Input: | (long) index | Index of the OLE object |
| --- | --- | --- |
| Output: | (BYTE) buffer | Size of the byte array for the data object |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE otherwise |

Syntax (COM)

status = Sheet->IGetOLEObjectData ( index, &buffer, &retval )

| Input: | (long) index | Index of the OLE object |
| --- | --- | --- |
| Output: | (BYTE) buffer | Size of the byte array for the data object |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the buffer data in the required format. These embedded objects are then saved with the newly created drawing translation.

This method only works with an MFC DLL add-in because the buffer input parameter is assumed to point to a Microsoft MFC object COleClientItem.
