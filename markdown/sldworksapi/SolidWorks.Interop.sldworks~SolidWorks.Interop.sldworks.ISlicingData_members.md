---
title: "ISlicingData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISlicingData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html"
---

# ISlicingData Interface Members

The following tables list the members exposed by [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AddSlicingPlanesAndSketchesToFolder | Gets or sets whether to add slicing planes and sketches to a folder in the FeatureManager design tree. |
| Property | NumberOfPlanes | Gets or sets the number of slicing planes. |
| Property | Offset | Gets or sets the linear or radial spacing between slicing planes. |
| Property | PlaneReferences | Sets the reference entities of the first slicing plane. |
| Property | ReverseDirection | Gets or sets whether to reverse the direction of slicing the model with respect to the initial reference plane. |
| Property | SlicesToGenerate | Gets or sets the slicing method. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetBoundingBoxDirection1 | Gets bounding box direction 1 (top manipulator for both linear and radial slicing). |
| Method | GetBoundingBoxDirection2 | Gets bounding box direction 2 (right manipulator for linear slicing, bottom manipulator for radial slicing). |
| Method | GetBoundingBoxDirection3 | Gets bounding box direction 3 (left manipulator for linear slicing, inner radius for radial slicing). |
| Method | GetBoundingBoxDirection4 | Gets bounding box direction 4 (bottom manipulator for linear slicing, outer radius for radial slicing). |
| Method | SetBoundingBoxDirection1 | Sets bounding box direction 1 (top manipulator for both linear and radial slicing). |
| Method | SetBoundingBoxDirection2 | Sets bounding box direction 2 (right manipulator for linear slicing, bottom manipulator for radial slicing). |
| Method | SetBoundingBoxDirection3 | Sets bounding box direction 3 (left manipulator for linear slicing, inner radius for radial slicing). |
| Method | SetBoundingBoxDirection4 | Sets bounding box direction 4 (bottom manipulator for linear slicing, outer radius for radial slicing). |

[Top](#topBookmark)

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
