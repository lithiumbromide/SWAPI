---
title: "IComponent2 Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IComponent2_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_properties.html"
---

# IComponent2 Interface Properties

For a list of all members of this type, see [IComponent2 members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ComponentReference | Gets or sets a component reference for this component. |
| Property | CustomPropertyManager | Gets the configuration-specific custom property manager for this assembly component. |
| Property | DisplayTitle | Gets this component's title as displayed in the FeatureManager design tree. |
| Property | ExcludeFromBOM | Obsolete. Superseded by IComponent2::GetExcludeFromBOM2 and IComponent2::SetExcludeFromBOM2 . |
| Property | IMaterialPropertyValues | Gets or sets the material properties for the selected component in the active configuration. |
| Property | IsGraphicsOnly | Gets whether this component is graphics only. |
| Property | IsSpeedPak | Gets whether the active configuration for this component is SpeedPak. |
| Property | IsVirtual | Gets whether this component is a virtual component. NOTE: This property is a get-only property. Set is not implemented . |
| Property | MaterialPropertyValues | Gets or sets the material properties for the selected component in the active configuration. |
| Property | Name | Obsolete. Superseded by IComponent2::Name2 . |
| Property | Name2 | Gets or sets the name of the selected component. |
| Property | PresentationTransform | Gets or sets the component transform. |
| Property | ReferencedConfiguration | Gets or sets the active configuration used by this component. |
| Property | ReferencedDisplayState | Obsolete. Superseded by IComponent2::ReferencedDisplayState2 . |
| Property | ReferencedDisplayState2 | Gets or sets the active display state of this component. |
| Property | Solving | Gets the Solve as option (rigid or flexible) of this component. |
| Property | Transform | Obsolete. Superseded by IComponent2::Transform2 . |
| Property | Transform2 | Gets or sets the component transform. |
| Property | UseNamedConfiguration | Gets whether a specified configuration or the in-use/last active configuration is used. |
| Property | Visible | Gets or sets the visibility state of this component. |

[Top](#topBookmark)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDoc2::GetPathName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName.html)
