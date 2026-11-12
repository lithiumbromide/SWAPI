---
title: "IImportDxfDwgData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html"
---

# IImportDxfDwgData Interface Members

The following tables list the members exposed by [IImportDxfDwgData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AddSketchConstraints | Gets or sets whether constraints are added to the geometry in the part sketch after importing the entities. |
| Property | DocumentTemplate | Gets or sets the filename of the document template. |
| Property | IgnorePolylineWidth | Gets or sets whether to convert width polylines to solid fill hatches when importing to the part sketch. |
| Property | ImportDimensions | Gets or sets whether to import dimension into the part sketch. |
| Property | ImportHatch | Gets or sets whether to import hatch into this part sketch. |
| Property | ImportMethod | Gets or sets whether to import this sheet (layout). |
| Property | LengthUnit | Gets or sets the length units for the drawing. |
| Property | SheetName | Gets or sets the name of the sheet for the drawing. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetImportLayerToSheetFormat | Gets whether the specified visible layer is imported to the drawing sheet or sheet format. |
| Method | GetImportLayerVisibility | Gets whether the specified layer is imported hidden or visible. |
| Method | GetMergeDistance | Gets whether points that are within the specified distance are merged in the part sketch after entities are imported. |
| Method | GetMergePoints | Gets whether near-identical points are merged in the part sketch after entities are imported. |
| Method | GetPaperSize | Gets the size of the paper for the drawing. |
| Method | GetPosition | Gets the position of the entities created in the drawing. |
| Method | GetSheetScale | Gets the sheet scale for the drawing. |
| Method | SetImportLayerToSheetFormat | Sets whether the specified visible layers are imported to the sheet format or drawing sheet. |
| Method | SetImportLayerVisibility | Sets whether the specified layers are imported hidden or visible. |
| Method | SetMergePoints | Sets whether near-identical points within the specified distance are merged in the part sketch after entities are imported. |
| Method | SetPaperSize | Sets the size of the paper in the drawing. |
| Method | SetPosition | Sets the position of the entities created in the drawing. |
| Method | SetSheetScale | Sets the sheet scale for the drawing. |

[Top](#topBookmark)

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.html)
