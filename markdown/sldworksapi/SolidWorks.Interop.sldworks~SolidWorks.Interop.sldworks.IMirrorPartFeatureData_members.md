---
title: "IMirrorPartFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html"
---

# IMirrorPartFeatureData Interface Members

The following tables list the members exposed by [IMirrorPartFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AbsorbedSketches | Gets or sets whether to import absorbed sketches. |
| Property | Axes | Gets or sets whether to import axes. |
| Property | CoordinateSystems | Gets or sets whether to import coordinate systems. |
| Property | CosmeticThreads | Gets or sets whether to import cosmetic threads. |
| Property | CustomProperties | Gets or sets whether to import custom properties. |
| Property | CutListProperties | Gets or sets whether to import cut-list properties. |
| Property | DimXpertAnnotations | Gets or sets whether to import DimXpert annotations. |
| Property | HoleWizardData | Gets or sets whether to import hole wizard data. |
| Property | ModelDimensions | Gets or sets whether to import model dimensions. |
| Property | PathName | Gets the path and file name of the derived mirror part feature. |
| Property | Planes | Gets or sets whether to import planes. |
| Property | SheetMetalInformation | Gets or sets whether to transfer the sheet-metal and flat-pattern information from the original sheet-metal part to the mirrored part. |
| Property | SolidBodies | Gets or sets whether to import solid bodies. |
| Property | SurfaceBodies | Gets or sets whether to import surface bodies. |
| Property | UnabsorbedSketches | Gets or sets whether to import unabsorbed sketches. |
| Property | UnlockedProperties | Gets or sets whether to enable editing of the sheet-metal definition in this mirrored sheet-metal part. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define the mirror part feature. |
| Method | GetMirrorPlane | Gets the plane about which this part is mirrored. |
| Method | GetMirrorPlaneType | Gets whether the mirror plane is a face or a reference plane. |
| Method | GetModelDoc | Gets the base model document of this mirror part feature. |
| Method | GetTransform | Gets the transform of this mirror part feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections used to define the mirror part feature. |

[Top](#topBookmark)

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IPartDoc::MirrorPart2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MirrorPart2.html)
[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
