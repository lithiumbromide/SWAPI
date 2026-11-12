---
title: "ModelDoc::InsertGtol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertGtol.htm"
---

# ModelDoc::InsertGtol

This method is obsolete and has been superseded by [ModelDoc2::InsertGtol](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertGtol.htm).

Description

This method creates a new geometric tolerance symbol in this document.

Syntax (OLE Automation)

gtol = ModelDoc.InsertGtol ( )

| Return: | (LPDISPATCH) gtol | Dispatch pointer to the new Gtol object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IInsertGtol ( >ol )

| Output: | (LPGTOL) gtol | Pointer to the new Gtol object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The leader attachment points for the Gtol that is created come from the selections made before calling this method. The initial location of the symbol will also be near the selection location. If there are no selections, the Gtol will not have a leader, be free standing, and initially be at the origin of the model or drawing.

This method creates an empty symbol. To fill in the text and symbols of this Gtol, you should use the pointer that is returned by this method to access the various get and set methods of the Gtol interface, such as Gtol::SetFrameSymbols2 and Gtol::SetFrameValues. Use the Gtol::GetAnnotation method to retrieve the Annotation object, which has other useful methods, such as Annotation::SetLeader2 and Annotation::SetPosition.
