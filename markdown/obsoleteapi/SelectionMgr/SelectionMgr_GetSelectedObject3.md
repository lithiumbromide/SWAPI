---
title: "SelectionMgr::GetSelectedObject3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr_GetSelectedObject3.htm"
---

# SelectionMgr::GetSelectedObject3

This method is obsolete and has been superseded by [SelectionMgr::GetSelectedObject4](SelectionMgr__GetSelectedObject4.htm).

Description

This method gets an interface to the currently selected object.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectedObject3 ( AtIndex)

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the Dispatch object as specified in Remarks or return NULL if type is not supported or if nothing is selected |

Syntax (COM)

status = SelectionMgr->IGetSelectedObject3 ( AtIndex, &retval )

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPUNKNOWN) retval | Pointer to the selected object as specified in Remarks or return NULL if type is not supported or if nothing is selected. |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The following list includes all of the types supported by this method as well as the object it returns for each type. You can use SelectionMgr::GetSelectedObjectType2 to determine Type Selected.

| Type Selected | Object Returned | Notes |
| --- | --- | --- |
| swSelCOMPONENTS | Component |  |
| swSelDIMENSIONS | DisplayDimension | Use DisplayDimenion::GetDimension to get the Dimension object |
| swSelEDGES | Edge |  |
| swSelREFEDGES | Edge |  |
| swSelFACES | Face |  |
| swSelGTOLS | Gtol |  |
| swSelNOTES | Note |  |
| swSelSHEETS | Sheet |  |
| swSelSKETCHSEGS | SketchSegment |  |
| swSelEXTSKETCHSEGS | SketchSegment |  |
| swSelSKETCHPOINTS | SketchPoint |  |
| swSelEXTSKETCHPOINTS | SketchPoint |  |
| swSelVERTICES | Vertex |  |
| swSelDRAWINGVIEWS | View |  |
| swSelATTRIBUTES | Feature (see NOTE ) |  |
| swSelBODYFEATURES | Feature (see NOTE ) |  |
| swSelDATUMAXES | Feature (see NOTE ) |  |
| swSelDATUMPLANES | Feature (see NOTE ) |  |
| swSelDATUMPOINTS | Feature (see NOTE ) |  |
| swSelDETAILCIRCLES | Feature (see NOTE ) | Use Feature::GetSpecificFeature to get the IDetailCircle |
| swSelMATES | Feature (see NOTE ) |  |
| swSelREFCURVES | Feature (see NOTE ) |  |
| swSelREFERENCECURVES | Feature (see NOTE ) |  |
| swSelREFSURFACES | Feature (see NOTE ) | Returns Feature object only when selection was made in the FeatureManager design tree. Otherwise, a Face or Edge object is returned. |
| swSelSECTIONLINES | Feature (see NOTE ) |  |
| swSelSKETCHES | Feature (see NOTE ) |  |
| swSelBOMS | BOM |  |
| swSelCENTERLINES | Centerline |  |
| swSelCTHREAD | Feature (see NOTE ) |  |
| NOTE: If the Object Returned is a Feature object, then you must use Feature::GetSpecificFeature if you want a more specific object interface. For example, if the selected object is a Sketch, then SelectionMgr::GetSelectedObject3 returns a Feature object. If you need the Sketch interface, then you must call the Feature::GetSpecificFeature method to return the Sketch object. |  |  |

Not Supported

swSelOLEITEMS

swSelCENTERMARKS

NOTE: When reference surfaces are selected in the graphics view, this method returns reference surface faces instead of the entire reference surface feature. When dimensions are selected in the graphics view, this method returns the DisplayDimension object instead of the Dimension object.
