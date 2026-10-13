---
title: "ISketchBlockDefinition Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html"
---

# ISketchBlockDefinition Interface Members

The following tables list the members exposed by [ISketchBlockDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | FileName | Gets or sets the name of the file to which the block definition is linked. |
| Property | InsertionPoint | Gets or sets the insertion point for the block definition. |
| Property | LinkToFile | Gets or sets whether the block definition file is linked to a file. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetArcCount | Gets the number of arcs in this block definition. |
| Method | GetArcs | Gets information about all of the arcs in the block definition. |
| Method | GetDisplayDimensionCount | Gets the number of display dimensions in this block definition. |
| Method | GetDisplayDimensions | Gets the display dimensions in this block definition. |
| Method | GetEllipseCount | Gets the number of ellipses in this block definition. |
| Method | GetEllipses | Gets the information about all of the ellipses in this block definition. |
| Method | GetFeature | Gets the feature for this block definition. |
| Method | GetInstanceCount | Gets the number of block instances of this block definition. |
| Method | GetInstances | Gets all of the block instances of this block definition. |
| Method | GetLineCount | Gets the number of lines in this block definition. |
| Method | GetLines | Gets information about all of the lines in this block definition. |
| Method | GetNoteCount | Gets the number of notes in this block definition. |
| Method | GetNotes | Gets the notes in this block definition. |
| Method | GetParabolaCount | Gets the number of parabolas in this block definition. |
| Method | GetParabolas | Gets information about all of the parabolas in this block definition. |
| Method | GetSketch | Gets the underlying sketch of this block definition. |
| Method | GetSplineCount | Gets the number of splines in this block definition. |
| Method | GetSplineInterpolateCount | Gets the number of splines in the sketch block definition and the size of array required to hold the data for the interpolation of these splines. |
| Method | GetSplineParams | Gets all the parameters of the splines in the sketch block definition. |
| Method | GetSplineParamsCount | Gets the number of splines in the sketch block definition and the size of array required to hold the data for the parameters of these splines. |
| Method | GetSplines | Obsolete. Superseded by ISketchBlockDefinition::GetSplines2 and ISketchBlockDefinition::IGetSplines2 . |
| Method | GetSplines2 | Gets the spline points by tessellation instead of by interpolation as is done by ISketchBlockDefinition::GetSplinesInterpolate and ISketchBlockDefinition::IGetSplinesInterpolate . |
| Method | GetSplinesInterpolate | Gets all of the parameers of the splines by interpolation instead of by tessellation as is done by ISketch::GetSplines2 and ISketch::IGetSplines2 . |
| Method | GetUserPoints | Gets information about all of the user points in this block definition. |
| Method | GetUserPointsCount | Gets the number of user points in this block definition. |
| Method | IGetArcs | Gets information about all of the arcs in the block definition. |
| Method | IGetDisplayDimensions | Gets the display dimensions in this block definition. |
| Method | IGetEllipses | Gets the information about all of the ellipses in this block definition. |
| Method | IGetInstances | Gets all of the block instances of this block definition. |
| Method | IGetLines | Gets information about all of the lines in this block definition. |
| Method | IGetNotes | Gets the notes in this block definition. |
| Method | IGetParabolas | Gets information about all of the parabolas in this block definition. |
| Method | IGetSplineParams | Gets all the parameters of the splines in the sketch block definition. |
| Method | IGetSplines | Obsolete. Superseded by ISketchBlockDefinition::GetSplines2 and ISketchBlockDefinition::IGetSplines2 . |
| Method | IGetSplines2 | Gets the spline points by tessellation instead of by interpolation as is done by ISketchBlockDefinition::GetSplinesInterpolate and ISketchBlockDefinition::IGetSplinesInterpolate . |
| Method | IGetSplinesInterpolate | Gets all of the parameers of the splines by interpolation instead of by tessellation as is done by ISketch::GetSplines2 and ISketch::IGetSplines2 . |
| Method | IGetUserPoints | Gets information about all of the user points in this block definition. |
| Method | Save | Saves the block definition. |

[Top](#topBookmark)

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
