---
title: "IMBD3DPdfData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html"
---

# IMBD3DPdfData Interface Members

The following tables list the members exposed by [IMBD3DPdfData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Accuracy | Gets or sets the level of accuracy for lossy compression when publishing to SOLIDWORKS MBD 3D PDF. |
| Property | CompressLossyTessellation | Gets or sets whether to apply lossy compression to polygons in the model when publishing to SOLIDWORKS MBD 3D PDF. |
| Property | CreateAttachSTEP242 | Gets or sets whether to export SOLIDWORKS parts and assemblies to STEP 242 format and attach the STEP 242 file to the SOLIDWORKS MBD 3D PDF. |
| Property | ExcludeFromAnnotationView | Gets or sets whether to exclude BOM tables from annotation views for this SOLIDWORKS MBD 3D PDF. |
| Property | FilePath | Gets or sets the path and file name to which to save this SOLIDWORKS MBD 3D PDF. |
| Property | STEP242Edition | Gets or sets the STEP 242 edition to use. |
| Property | ThemeName | Gets or sets the path and file name of the theme for this SOLIDWORKS MBD 3D PDF. |
| Property | ViewPdfAfterSaving | Gets or sets whether to display this SOLIDWORKS MBD 3D PDF after publishing it . |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetAttachments | Gets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF. |
| Method | GetBomAreaCount | Gets the number of BOM Table Areas defined in the theme for this SOLIDWORKS MBD 3D PDF. |
| Method | GetImportedNotes | Gets the imported note names from the theme of this MBD3DPdfData. |
| Method | GetMoreViews | Gets the names of the custom views (i.e., named views and 3D views ) in the model for this SOLIDWORKS MBD 3D PDF. |
| Method | GetStandardViews | Gets the types of standard views in the model for this SOLIDWORKS MBD 3D PDF. |
| Method | GetTextAndCustomProperties | Gets the text and custom properties in the theme for this SOLIDWORKS MBD 3D PDF. |
| Method | SetAttachments | Sets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF. |
| Method | SetBomTable | Maps a BOM Table Area in the theme with a BOM table in the model and sets the columns in the BOM table to export to the BOM Table Area in a SOLIDWORKS MBD 3D PDF. |
| Method | SetImportedNote | Sets the specified imported note. |
| Method | SetIndependentViewPort | Sets the specified view for an independent viewport for the SOLIDWORKS MBD 3D PDF. |
| Method | SetMoreViews | Sets the names of the custom views (i.e., named views and 3D views ) in the model for this SOLIDWORKS MBD 3D PDF. |
| Method | SetStandardViews | Sets the types of standard views in the model for this SOLIDWORKS MBD 3D PDF. |

[Top](#topBookmark)

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDocExtension::PublishTo3DPDF Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.html)
[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
