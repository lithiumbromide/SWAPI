---
title: "IMassProperty2 Interface Members"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html"
---

# IMassProperty2 Interface Members

The following tables list the members exposed by [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AccuracyLevel | Gets or sets the accuracy level used to calculate mass properties. |
| Property | CenterOfMass | Gets the center of mass of selected components/bodies. |
| Property | Density | Gets the density of selected components/bodies. |
| Property | IncludeHiddenBodiesOrComponents | Gets or sets whether to include the mass properties of hidden bodies/components. |
| Property | Mass | Gets the mass of selected components/bodies. |
| Property | PrincipalAxesOfInertia | Gets the principal axis of inertia for the specified axis. |
| Property | PrincipalMomentsOfInertia | Gets the principal moments of inertia. |
| Property | SelectedItems | Gets or sets the list of bodies/components for which to calculate mass properties. |
| Property | ShowWeldBeadMass | Gets or sets whether to calculate weld bead mass. |
| Property | SurfaceArea | Gets the surface area of selected components/bodies. |
| Property | UseSystemUnits | Gets or sets whether to use system units or document units when calculating mass properties. |
| Property | Volume | Gets the volume of selected components/bodies. |
| Property | WeldBeadMass | Gets the weld bead mass. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetMomentOfInertia | Gets the moment of inertia at the specified coordinate system for the selected bodies/components. |
| Method | GetOverrideOptions | Gets the mass property override options for the selected bodies/components. |
| Method | Recalculate | Recalculates the mass properties of the selectied bodies/components. |
| Method | SetCoordinateSystem | Sets the coordinate system to use when calculating mass properties for this model. |
| Method | SetOverrideOptions | Sets the mass property override options for the selected bodies/components. |

[Top](#topBookmark)

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
