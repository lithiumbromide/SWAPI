---
title: "ICWMultipleComponentContactsEditManager Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html"
---

# ICWMultipleComponentContactsEditManager Interface Members

The following tables list the members exposed by [ICWMultipleComponentContactsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddContactComponent | Adds the specified contact component to the set of contact components to edit. |
| Method | GetContactComponentsCount | Gets the number of contact components in the set of contact components to edit. |
| Method | IncludeClearance | Obsolete. Superseded by ICWMultipleComponentContactsEditManager::IncludeClearance2 . |
| Method | IncludeClearance2 | Sets whether to include clearance for non-touching faces. |
| Method | IncludeShellEdgeSolidOrShellFace | Obsolete. Superseded by ICWMultipleComponentContactsEditManager::IncludeShellEdgeSolidOrShellFace2 . |
| Method | IncludeShellEdgeSolidOrShellFace2 | Sets whether to create edge-to-edge bonded contact sets. |
| Method | MultipleComponentContactsBeginEdit | Starts editing multiple contact components. |
| Method | MultipleComponentContactsEndEdit | Finishes editing multiple contact components. |
| Method | RemoveContactComponent | Removes the specified contact component from the set of contact components to edit. |
| Method | SetAsDefaultComponentContact | Applies the properties of the specified component contact to the set of all component contacts to edit. |
| Method | SetBondingFormulation | Sets the specified bonding formulation for all component contacts. |
| Method | SetClearanceUnit | Sets the units of clearance distance. |
| Method | SetClearanceValue | Sets the maximum clearance between non-touching faces or shell edges. |
| Method | SetContactType | Sets the type of the component contacts to edit. |
| Method | SetFrictionValue | Sets the friction coefficient. |
| Method | SetIncludeFriction | Obsolete. Superseded by ICWMultipleComponentContactsEditManager::SetIncludeFriction2 . |
| Method | SetIncludeFriction2 | Sets whether to include friction. |
| Method | SetMeshOption | Sets the mesh compatibility option. |

[Top](#topBookmark)

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
