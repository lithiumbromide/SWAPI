---
title: "IMassProperty Interface Members"
project: "SOLIDWORKS API Help"
interface: "IMassProperty_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html"
---

# IMassProperty Interface Members

The following tables list the members exposed by [IMassProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CenterOfMass | Gets the center of mass. |
| Property | Density | Gets the density for this model. |
| Property | Mass | Gets the mass of this model. |
| Property | OverrideCenterOfMass | Gets or sets whether to override the calculated center of mass value for the model. |
| Property | OverrideMass | Gets or sets whether to override the calculated mass value for the model. |
| Property | OverrideMomentsOfInertia | Gets or sets whether to override the calculated moments of inertia for the model. |
| Property | PrincipleAxesOfInertia | Gets the principal axes of inertia for this model. |
| Property | PrincipleMomentsOfInertia | Gets the principal moments of inertia for this model. |
| Property | SurfaceArea | Gets the surface area for this model. |
| Property | UserAssigned | Gets whether the mass property values are user-defined or calculated for this document, regardless of which model is being edited. |
| Property | UseSystemUnits | Gets and sets whether to use system units or document units when calculating mass properties for this model. |
| Property | Volume | Gets the volume of this model. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddBodies | Uses only the specified bodies when calculating the mass properties for this model. |
| Method | GetMomentOfInertia | Gets the moment of inertia at the specified coordinate system for this model. |
| Method | IAddBodies | Uses only the specified bodies when calculating the mass properties for this model. |
| Method | IGetCenterOfMass | Gets the center of mass for this model. |
| Method | IGetMomentOfInertia | Gets the moment of inertia at the specified coordinate system for this model. |
| Method | IGetPrincipleAxesOfInertia | Gets the principal axes of inertia for this model. |
| Method | IGetPrincipleMomentsOfInertia | Gets the principal moments of inertia for this model. |
| Method | ISetAssignedMassProp | Sets the mass and center of gravity for the specified configurations for this model being edited in this part or assembly document. |
| Method | ISetOverrideCenterOfMassValue | Overrides the center of mass of the model currently being edited in this part or assembly document. |
| Method | ISetOverrideMassValue | Overrides the mass of the model currently being edited in this part or assembly document. |
| Method | ISetOverrideMomentsOfInertiaValue | Overrides the moments of inertia of the model currently being edited in this part or assembly document. |
| Method | ISetOverridePrincipleAxesOrientation | Overrides the orientation of the specified principal axis of inertia for the model currently being edited in this part or assembly document. |
| Method | ISetOverridePrincipleMomentsOfInertia | Overrides the principal moments of inertia of the model currently being edited in this part or assembly document. |
| Method | SetAssignedMassProp | Sets the mass and center of gravity for the specified configurations for this model being edited in this part or assembly document. |
| Method | SetCoordinateSystem | Sets the coordinate system to use when calculating mass properties for this model. |
| Method | SetOverrideCenterOfMassValue | Overrides the center of mass of the model currently being edited in this part or assembly document. |
| Method | SetOverrideMassValue | Overrides the mass of the model currently being edited in this part or assembly document. |
| Method | SetOverrideMomentsOfInertiaValue | Overrides the moments of inertia of the model currently being edited in this part or assembly document. |
| Method | SetOverridePrincipleAxesOrientation | Overrides the orientation of the specified principal axis of inertia for the model currently being edited in this part or assembly document. |
| Method | SetOverridePrincipleMomentsOfInertia | Overrides the principal moments of inertia of the model currently being edited in this part or assembly document. |

[Top](#topBookmark)

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDocExtension::GetMassProperties2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMassProperties2.html)
