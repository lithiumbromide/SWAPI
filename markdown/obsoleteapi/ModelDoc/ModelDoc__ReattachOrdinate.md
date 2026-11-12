---
title: "ModelDoc::ReattachOrdinate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ReattachOrdinate.htm"
---

# ModelDoc::ReattachOrdinate

This method is obsolete and has been superseded by [ModelDoc2::ReattachOrdinate](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ReattachOrdinate.htm).

Description

This method reattaches an ordinate dimension to a different entity.

Syntax (OLE Automation)

retval = ModelDoc.ReattachOrdinate ( )

| Return: | (BOOL) retval | TRUE if the reattachment was successful, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->ReattachOrdinate ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the reattachment was successful, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

To use this method, you must first select the dimension to be reattached and then call ModelDoc::AndSelecteByID to select the new entity to which to attach this dimension. For example:

```vb
Part.SelectByID "D6@Sketch2@Part1.SLDDRW", "DIMENSION", 0.0194564, 0.0695452, 0
Part.AndSelectByID "", "EDGE", 0.0310388, 0.05887719999651, -499.8885
Part.ReAttachOrdinate
```
