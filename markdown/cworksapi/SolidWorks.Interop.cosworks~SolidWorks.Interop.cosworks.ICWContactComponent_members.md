---
title: "ICWContactComponent Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html"
---

# ICWContactComponent Interface Members

The following tables list the members exposed by [ICWContactComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BondingFormulation | Sets the bonding formulation for this contact. |
| Property | ClearanceUnit | Gets or sets the units of clearance between non-touching faces. |
| Property | ClearanceValue | Gets or sets the maximum clearance (gap) between non-touching faces or shell edges. |
| Property | ContactComponentType | Gets or sets the type of contact. |
| Property | ContactName | Gets the name of the contact. |
| Property | FrictionValue | Gets or sets the friction coefficient for this contact. |
| Property | GlobalContact | Obsolete. Superseded by ICWContactComponent::GlobalContact2 . |
| Property | GlobalContact2 | Sets whether to apply a global contact condition. |
| Property | IncludeClearance | Obsolete. Superseded by ICWContactComponent::IncludeClearance2 . |
| Property | IncludeClearance2 | Sets whether to specify clearance for non-touching faces in this contact. |
| Property | IncludeFriction | Obsolete. Superseded by ICWContactComponent::IncludeFriction2 . |
| Property | IncludeFriction2 | Sets whether to specify a friction coefficient for this contact. |
| Property | IncludeShellEdgeSolidOrShellFace | Obsolete. Superseded by ICWContactComponent::IncludeShellEdgeSolidOrShellFace2 . |
| Property | IncludeShellEdgeSolidOrShellFace2 | Sets whether to create contact sets. |
| Property | Option | Gets or sets the mesh compatibility for this contact. |
| Property | State | Gets the suppression state of this contact. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ContactComponentBeginEdit | Start editing of this contact. |
| Method | ContactComponentEndEdit | Ends editing of this contact. |
| Method | InsertEntity | Inserts a component into this contact. |
| Method | RemoveEntity | Removes a component from this contact. |
| Method | ReplaceEntity | Replaces the entity of this contact. |
| Method | SuppressUnSuppress | Suppresses or unsuppresses this contact depending on its state . |

[Top](#topBookmark)

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
