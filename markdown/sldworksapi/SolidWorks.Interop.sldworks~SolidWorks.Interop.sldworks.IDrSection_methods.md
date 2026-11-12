---
title: "IDrSection Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IDrSection_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_methods.html"
---

# IDrSection Interface Methods

For a list of all members of this type, see [IDrSection members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | EnumExcludedComponents | Obsolete. Superseded by IDrSection::EnumExcludedComponent2 . |
| Method | EnumExcludedComponents2 | Gets all of the assembly components that are excluded from this section view. |
| Method | GetArrowInfo | Gets the position of the arrows for the section line. |
| Method | GetAutoHatch | Gets whether auto hatching is enabled for the section view resulting from this section cut. |
| Method | GetDisplayOnlySpeedPakBodies | Gets whether to display in this section view only the bodies included in the SpeedPak configuration. |
| Method | GetDisplayOnlySurfaceCut | Gets whether to display only the surface cut by the section line. |
| Method | GetDontCutAllInstances | Gets whether all instances of the specified component are uncut in this section view or only in the specified component. |
| Method | GetExcludedComponents | Gets all of the assembly components that are excluded from this section view. |
| Method | GetLabel | Gets the label for this section view. |
| Method | GetLineInfo | Gets the vertices of the section line. |
| Method | GetName | Gets the name of the section line. |
| Method | GetPartialSection | Gets whether this is a partial section cut. |
| Method | GetReversedCutDirection | Gets whether the section cut direction is reversed from the default direction. |
| Method | GetScaleWithModelChanges | Gets whether the section line scales with changes to the model. |
| Method | GetSectionView | Gets the section view of this section cut. |
| Method | GetTextFormat | Gets the text format for the text for this section line. |
| Method | GetTextInfo | Gets the location of the section line text. |
| Method | GetUseDocTextFormat | Gets whether SOLIDWORKS is currently using the document default setting for text format. |
| Method | GetView | Gets the drawing view where the section line appears. |
| Method | IGetArrowInfo | Gets the position of the arrows for this section line. |
| Method | IGetLineInfo | Gets the vertices of the section line. |
| Method | IGetLineSegmentCount | Gets the number of line segments making up this section line. |
| Method | IGetSectionView | Gets the section view of this section cut. |
| Method | IGetTextFormat | Gets the text format for the text for this section line. |
| Method | IGetTextInfo | Gets the location of the section line text. |
| Method | IGetView | Gets the drawing view where the section line appears. |
| Method | IsAligned | Gets whether this is an aligned section view. |
| Method | ISetExcludedComponents | Excludes the specified components from this section view. |
| Method | ISetLineInfo | Sets the location (both position and arrow heads) of the section line. |
| Method | ISetTextFormat | Sets the text format for the text for this section line. |
| Method | SetAutoHatch | Sets whether auto hatching is enabled for the section view resulting from this section cut. |
| Method | SetDisplayOnlySpeedPakBodies | Sets whether to display in this section view only the bodies included in the SpeedPak configuration. |
| Method | SetDisplayOnlySurfaceCut | Sets whether to display only the surface cut by the section line. |
| Method | SetDontCutAllInstances | Sets whether all instances of the specified component are uncut in this section view or only in the specified component. |
| Method | SetExcludedComponents | Excludes the specified components from this section view. |
| Method | SetLabel | Obsolete. Superseded by IDrSection::ISetLabel2 . |
| Method | SetLabel2 | Sets the label for this section view. |
| Method | SetLineInfo | Sets the location (both position and arrow heads) of the section line. |
| Method | SetPartialSection | Sets whether this is a partial section cut. |
| Method | SetReversedCutDirection | Sets whether the section cut direction is reversed from the default. |
| Method | SetScaleWithModelChanges | Sets whether the section line scales with changes to the model. |
| Method | SetTextFormat | Sets the text format for the text for this section line. |

[Top](#topBookmark)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IEnumDrSections Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections.html)
[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
