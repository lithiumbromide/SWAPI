---
title: "SelectionMgr::GetSelectedObject2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObject2.htm"
---

# SelectionMgr::GetSelectedObject2

This method is obsolete and has been superseded by [SelectionMgr::GetSelectedObject3](SelectionMgr_GetSelectedObject3.htm)

Description

This method gets an interface to the currently selected object.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectedObject2 ( AtIndex)

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the Dispatch object as specified in Remarks or return NULL if type is not supported |

Syntax (COM)

status = SelectionMgr->IGetSelectedObject2 ( AtIndex, &retval )

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPUNKNOWN) retval | Pointer to the Dispatch object as specified in Remarks or return NULL if type is not supported |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The list below shows the type selected and the object returned by this method. This method works for the following types:

| Type Selected | Object Returned |
| --- | --- |
| swSelCOMPONENTS | Component |
| swSelDIMENSIONS | Dimension |
| swSelEDGES | Edge |
| swSelREFEDGES | Edge |
| swSelFACES | Face |
| swSelGTOLS | Gtol |
| swSelNOTES | Note |
| swSelSHEETS | Sheet |
| swSelVERTICES | Vertex |
| swSelDRAWINGVIEWS | View |
| swSelATTRIBUTES | Feature (see NOTE ) |
| swSelBODYFEATURES | Feature (see NOTE ) |
| swSelDATUMAXES | Feature (see NOTE ) |
| swSelDATUMPLANES | Feature (see NOTE ) |
| swSelDATUMPOINTS | Feature (see NOTE ) |
| swSelMATES | Feature (see NOTE ) |
| swSelREFCURVES | Feature (see NOTE ) |
| swSelREFERENCECURVES | Feature (see NOTE ) |
| swSelREFSURFACES | Feature (see NOTE ) |
| swSelSKETCHES | Feature (see NOTE ) |
| NOTE: If Object Returned is a Feature object, then you must use Feature::GetSpecificFeature to get a more specific object interface. For example, if the selected object is a Sketch, then this method returns a Feature object. If you need the Sketch interface, then you must call the Feature::GetSpecificFeature method to return the Sketch object. |  |

Not Supported

- swSelOLEITEMS
- swSelSKETCHSEGS
- swSelSKETCHPOINTS
- swSelSECTIONLINES
- swSelDETAILCIRCLES
- swSelSECTIONTEXT
- swSelEXTSKETCHSEGS
- swSelEXTSKETCHPOINTS
- swSelCENTERMARKS
