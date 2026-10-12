---
title: "ISketch Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISketch_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html"
---

# ISketch Interface Members

The following tables list the members exposed by [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | IModelToSketchXform | Obsolete. Superseded by ISketch::ModelToSketchTransform . NOTE: This property is a get-only property. Set is not implemented . |
| Property | ModelToSketchTransform | Gets the model-to-sketch transform for this sketch. NOTE: This property is a get-only property. Set is not implemented . |
| Property | ModelToSketchXform | Obsolete. Superseded by ISketch::ModelToSketchTransform . NOTE: This property is a get-only property. Set is not implemented . |
| Property | RelationManager | Gets the sketch relation manager. NOTE: This property is a get-only property. Set is not implemented . |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AutoDimension | Obsolete. Superseded by ISketch::AutoDimension2 . |
| Method | AutoDimension2 | Obsolete. Superseded by ISketchManager::FullyDefineSketch . |
| Method | CheckFeatureUse | Checks to see if this sketch is valid for use in creating a specified feature. |
| Method | ConstrainAll | Attempts to solve all of the apparent relations in the sketch and returns the number of constraints that were added to the sketch. |
| Method | GetArcCount | Gets the number of arcs in the sketch. |
| Method | GetArcs | Obsolete. Superseded by ISketch::GetArcs2 and ISketch::IGetArcs2 . |
| Method | GetArcs2 | Gets all of the arcs in the sketch. |
| Method | GetAutomaticSolve | Checks whether the computation to solve the sketch geometry of the part as modifications are automatically performed. |
| Method | GetConstrainedStatus | Gets the current constrained status of the sketch. |
| Method | GetContourEdgeCount | Gets the number of edges for this sketch contour. |
| Method | GetContourEdges | Gets the edges for a sketch that has one contour. |
| Method | GetDetachSegmentOnDrag | Gets the Detach Segment on Drag setting. |
| Method | GetEllipseCount | Gets the number of ellipses in the sketch. |
| Method | GetEllipses | Obsolete. Superseded by ISketch::GetEllipses3 and ISketch::IGetEllipses3 . |
| Method | GetEllipses2 | Obsolete. Superseded by ISketch::GetEllipses3 and ISketch::IGetEllipses3 . |
| Method | GetEllipses3 | Gets all of the ellipses in the sketch. |
| Method | GetLineCount | Obsolete. Superseded by ISketch::GetLineCount2 . |
| Method | GetLineCount2 | Gets the number of lines in the sketch with an option to exclude or include crosshatch lines. |
| Method | GetLines | Obsolete. Superseded by ISketch::GetLines2 and ISketch::IGetLines2 . |
| Method | GetLines2 | Gets all of the lines in the sketch with an option to include or exclude crosshatch lines. |
| Method | GetParabolaCount | Gets the number of parabolas in the sketch. |
| Method | GetParabolas | Obsolete. Superseded by ISketch::GetParabolas2 and ISketch::IGetParabolas2 . |
| Method | GetParabolas2 | Gets all of the parabolas in the sketch. |
| Method | GetPolyLineCount | Not implemented. |
| Method | GetPolylines | Not implemented. |
| Method | GetReferenceEntity | Gets the entity on which this sketch was created. |
| Method | GetSketchBlockInstanceCount | Gets the number of block instances in this sketch (i.e., the sketch under which the block instances are displayed in the FeatureManager design tree). |
| Method | GetSketchBlockInstances | Gets the block instances in this sketch (i.e., the sketch under which the block instances are displayed in the FeatureManager design tree). |
| Method | GetSketchContourCount | Gets the number of sketch contours in this sketch. |
| Method | GetSketchContours | Gets the sketch contours in this sketch. |
| Method | GetSketchHatches | Gets an array of sketch hatches that exist in this sketch. |
| Method | GetSketchPathCount | Gets the number of sketch paths in this sketch. |
| Method | GetSketchPaths | Gets the sketch paths in this sketch. |
| Method | GetSketchPictureCount | Gets the number of pictures on this sketch. |
| Method | GetSketchPictures | Gets the pictures on this sketch. |
| Method | GetSketchPoints | Obsolete. Superseded by ISketch::GetSketchPoints2 , ISketch::IGetSketchPoints2 , and ISketch::IEnumSketchPoints . |
| Method | GetSketchPoints2 | Gets the sketch points in this sketch. |
| Method | GetSketchPointsCount | Obsolete. Superseded by ISketch::GetSketchPointsCount2 . |
| Method | GetSketchPointsCount2 | Gets the number of sketch points in this sketch. |
| Method | GetSketchRegionCount | Gets the number of sketch regions in this sketch. |
| Method | GetSketchRegions | Gets the sketch regions in this sketch. |
| Method | GetSketchSegments | Gets the sketch segments in this sketch, which include line, arc, spline, parabola, and ellipse entities. |
| Method | GetSketchSlotCount | Gets the number of sketch slots in this sketch. |
| Method | GetSketchSlots | Gets the sketch slots in this sketch. |
| Method | GetSketchTextSegments | Gets the sketch segments that represent the selected text in the sketch. |
| Method | GetSplineCount | Gets the number of splines in this sketch. |
| Method | GetSplineInterpolateCount | Gets the number of points in the spline and number of splines in the sketch. |
| Method | GetSplineParams | Obsolete. Superseded by ISketch::GetSplineParams2 and ISketch::IGetSplineParams2 . |
| Method | GetSplineParams2 | Obsolete. Superseded by ISketch::GetSplineParams3 . |
| Method | GetSplineParams3 | Obsolete. Superseded by ISketch::GetSplineParams4 . |
| Method | GetSplineParams4 | Obsolete. Superseded by ISketch::GetSplineParams5 . |
| Method | GetSplineParams5 | Gets the parameterization data of the specified spline in this sketch. |
| Method | GetSplineParamsCount | Obsolete. Superseded by ISketch::GetSplineParamsCount2 . |
| Method | GetSplineParamsCount2 | Obsolete. Superseded by ISketch::GetSplineParamsCount3 . |
| Method | GetSplineParamsCount3 | Gets the number of splines in the sketch and the size of array required to hold the data for them. |
| Method | GetSplines | Gets information for each spline by tessellation instead of by interpolation as is done by ISketch::GetSplinesInterpolate and ISketch::IGetSplinesInterpolate . |
| Method | GetSplinesInterpolate | Gets the spline points by interpolation instead of by tessellation as is done by ISketch::GetSplines and ISketch::IGetSplines . |
| Method | GetUserPoints | Obsolete. Superseded by ISketch::GetUserPoints2 and ISketch::IGetUserPoints2 . |
| Method | GetUserPoints2 | Gets all of the user points in this sketch. |
| Method | GetUserPointsCount | Gets the number of user points in the sketch. |
| Method | IEnumSketchHatches | Gets the sketch hatches enumeration in this sketch. |
| Method | IEnumSketchPoints | Gets the sketch points enumeration in this sketch. |
| Method | IEnumSketchSegments | Gets the sketch segments enumeration in this sketch. |
| Method | IEnumSketchTextSegments | Gets the sketch segments enumeration for the selected text in this sketch. |
| Method | IGetArcs | Obsolete. Superseded by ISketch::GetArcs2 and ISketch::IGetArcs2 . |
| Method | IGetArcs2 | Gets all of the arcs in the sketch. |
| Method | IGetContourEdges | Gets the edges for a sketch that has one contour. |
| Method | IGetEllipses | Obsolete. Superseded by ISketch::GetEllipses3 and ISketch::IGetEllipses3 . |
| Method | IGetEllipses2 | Obsolete. Superseded by ISketch::GetEllipses3 and ISketch::IGetEllipses3 . |
| Method | IGetEllipses3 | Gets all of the ellipses in the sketch. |
| Method | IGetLines | Obsolete. Superseded by ISketch::GetLines2 and ISketch::IGetLines2 . |
| Method | IGetLines2 | Gets all of the lines in the sketch with an option to include or exclude crosshatch lines. |
| Method | IGetParabolas | Obsolete. Superseded by ISketch::GetParabolas2 and ISketch::IGetParabolas2 . |
| Method | IGetParabolas2 | Gets all of the parabolas in the sketch. |
| Method | IGetPolylines | Not implemented. |
| Method | IGetSketchBlockInstances | Gets the block instances in this sketch (i.e., the sketch under which the block instances are displayed in the FeatureManager design tree). |
| Method | IGetSketchContours | Gets the sketch contours in this sketch. |
| Method | IGetSketchPaths | Gets the sketch paths in this sketch. |
| Method | IGetSketchPictures | Gets the pictures on this sketch. |
| Method | IGetSketchPoints2 | Gets the sketch points in this sketch. |
| Method | IGetSketchRegions | Gets the sketch regions in this sketch. |
| Method | IGetSketchSlots | Gets the sketch slots in this sketch. |
| Method | IGetSplineParams | Obsolete. Superseded by ISketch::GetSplineParams2 and ISketch::IGetSplineParams2 . |
| Method | IGetSplineParams2 | Obsolete. Superseded by ISketch::IGetSplineParameters3 . |
| Method | IGetSplineParams3 | Obsolete. Superseded by ISketch::GetSplineParams4 . |
| Method | IGetSplines | Gets information for each spline by tessellation instead of by interpolation as is done by ISketch::GetSplinesInterpolate and ISketch::IGetSplinesInterpolate . |
| Method | IGetSplinesInterpolate | Gets the spline points by interpolation instead of by tessellation as is done by ISketch::GetSplines and ISketch::IGetSplines . |
| Method | IGetUserPoints | Obsolete. Superseded by ISketch::GetUserPoints2 and ISketch::IGetUserPoints2 . |
| Method | IGetUserPoints2 | Gets all of the user points in this sketch. |
| Method | InsertRouteLine | Inserts a route line in an explode line sketch or a 3D sketch to indicate component relationships. |
| Method | Is3D | Gets whether this sketch is 2D or 3D. |
| Method | IsBoundaryBoxSketch | Determines whether the sketch is a boundary box. |
| Method | IsDerived | Gets whether a sketch is derived. |
| Method | IsShared | Gets whether this sketch is used by more than one feature. |
| Method | IsSketchEditable | Gets whether this sketch is editable. |
| Method | MergePoints | Merges sketch points within a specified distance. |
| Method | SetAutomaticSolve | Controls whether the computation to solve the sketch geometry of the part as modifications are automatically performed. |
| Method | SetDetachSegmentOnDrag | Sets the Detach Segment on Drag setting. |
| Method | SetSketchEditable | Sets whether this sketch is editable. |
| Method | SetWorkingPlaneOrientation | Sets the orientation for sketching geometry in a 3D sketch. It sets the planar location for new 2D and 3D geometry in a 3D sketch. |

[Top](#topBookmark)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)
[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchParabola Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.html)
[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.html)
[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
