---
title: "ISelectionMgr Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html"
---

# ISelectionMgr Interface Members

The following tables list the members exposed by[ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | EnableContourSelection | Enables and disables contour selection. |
| Property | EnableSelection | Enables or disables selection. |
| Property | SelectionColor | Gets or sets the selection color. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddSelectionListObject | Adds the specified object to the selection list. |
| Method | AddSelectionListObjects | Adds the specified objects to the selection list. |
| Method | ClearSelectionColors | Clears all of selection color settings. |
| Method | CreateCallout | Obsolete. Superseded by ISelectionMgr::CreateCallout2 . |
| Method | CreateCallout2 | Creates a callout for the selection. |
| Method | CreateSelectData | Creates a ISelectData object to use as argument with Select methods. |
| Method | DeSelect | Obsolete . Superseded by ISelectionMgr::DeSelect2 . |
| Method | DeSelect2 | Deselects the specified entity. |
| Method | GetPreSelectedObject | Gets the preselected object when the preselection notify event is fired. |
| Method | GetSelectByIdSpecification | Gets the selection specification for the specified object. |
| Method | GetSelectedCoordSysElement | Gets the selected coordinate system element. |
| Method | GetSelectedObject | Obsolete. Superseded by ISelectionMgr::GetSelectedObject6 . |
| Method | GetSelectedObject2 | Obsolete. Superseded by ISelectionMgr::GetSelectedObject6 . |
| Method | GetSelectedObject3 | Obsolete. Superseded by ISelectionMgr::GetSelectedObject6 . |
| Method | GetSelectedObject4 | Obsolete. Superseded by ISelectionMgr::GetSelectedObject6 . |
| Method | GetSelectedObject5 | Obsolete. Superseded by ISelectionMgr::GetSelectedObject6 . |
| Method | GetSelectedObject6 | Gets the selected object. |
| Method | GetSelectedObjectCount | Obsolete. Superseded by ISelectionMgr::GetSelectedObjectCount2 . |
| Method | GetSelectedObjectCount2 | Gets the number of selected objects. |
| Method | GetSelectedObjectLoop | Obsolete. Superseded by ISelectionMgr::GetSelectedObjectLoop2 . |
| Method | GetSelectedObjectLoop2 | Gets the loop, if selected, for the selected edge. |
| Method | GetSelectedObjectMark | Gets the value of the mark for the specified selection. |
| Method | GetSelectedObjectsComponent | Obsolete. Superseded by ISelectionMgr::GetSelectedObjectsComponent3 . |
| Method | GetSelectedObjectsComponent2 | Obsolete. Superseded by ISelectionMgr::GetSelectedObjectsComponent3 . |
| Method | GetSelectedObjectsComponent3 | Obsolete. Superseded by ISelectionMgr::GetSelectedObjectsComponent4 . |
| Method | GetSelectedObjectsComponent4 | Gets the selected component in an assembly or drawing. |
| Method | GetSelectedObjectsDrawingView | Obsolete. Superseded by ISelectionMgr::GetSelectedObjectsDrawingView2 . |
| Method | GetSelectedObjectsDrawingView2 | Gets the drawing view for the selected object. |
| Method | GetSelectedObjectsFace | Gets the face of the specified selection if the specified selection is a silhouette edge . |
| Method | GetSelectedObjectType | Obsolete. Superseded by ISelectionMgr::GetSelectedObjectType3 . |
| Method | GetSelectedObjectType2 | Obsolete. Superseded by ISelectionMgr::GetSelectedObjectType3 . |
| Method | GetSelectedObjectType3 | Gets the type of object selected. |
| Method | GetSelectionPoint | Obsolete. Superseded by ISelectionMgr::GetSelectionPoint2 . |
| Method | GetSelectionPoint2 | Gets the selected point in model space coordinates from the currently selected object. |
| Method | GetSelectionPointInSketchSpace | Obsolete. Superseded by ISelectionMgr::GetSelectionPointInSketchSpace2 . |
| Method | GetSelectionPointInSketchSpace2 | Gets the selection point projected on to the active sketch and returned in sketch space. |
| Method | GetSelectionSpecification | Gets the selection specification at the specified index of the current selection list. |
| Method | IDeSelect | Obsolete. Superseded by ISelectionMgr::IDeSelect2 . |
| Method | IDeSelect2 | Deselects the specified entity. |
| Method | IGetSelectedObject | Obsolete. Superseded by ISelectionMgr::GetSelectedObject6 . |
| Method | IGetSelectedObject2 | Obsolete. Superseded by ISelectionMgr::GetSelectedObject6 . |
| Method | IGetSelectedObject3 | Obsolete. Superseded by ISelectionMgr::GetSelectedObject6 . |
| Method | IGetSelectedObject4 | Obsolete. Superseded by ISelectionMgr::GetSelectedObject6 . |
| Method | IGetSelectedObjectsComponent | Obsolete. Superseded by ISelectionMgr::GetSelectedObjectsComponent3 . |
| Method | IGetSelectedObjectsComponent2 | Obsolete. Superseded by ISelectionMgr::GetSelectedObjectsComponent3 . |
| Method | IGetSelectionPoint | Obsolete. Superseded by ISelectionMgr::IGetSelectionPoint2 . |
| Method | IGetSelectionPoint2 | Gets the selected point in model space coordinates from the currently selected object. |
| Method | IGetSelectionPointInSketchSpace | Obsolete. Superseded by ISelectionMgr::IGetSelectionPointInSketchSpace2 . |
| Method | IGetSelectionPointInSketchSpace2 | Gets the selection point projected on to the active sketch and returned in sketch space. |
| Method | IsCoordSysElementSelected | Gets whether the selection is a coordinate system element. |
| Method | IsInEditTarget | Obsolete. Superseded by ISelectionMgr::IsInEditTarget2 . |
| Method | IsInEditTarget2 | Gets whether the selected object is in the edit target. |
| Method | ResumeSelectionList | Obsolete. Superseded by ISelectionMgr::ResumeSelectionList2 . |
| Method | ResumeSelectionList2 | Reinstates the previously suspended selection list. |
| Method | SetCallout | Adds a callout to the currently selected object. |
| Method | SetSelectedObjectMark | Sets the mark value for the specified selection. |
| Method | SetSelectionPoint | Obsolete. Superseded by ISelectionMgr::SetSelectionPoint2 . |
| Method | SetSelectionPoint2 | Sets the selection point in model space. |
| Method | SuspendSelectionList | Suspends the current selection list. |

[Top](#topBookmark)

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html)
