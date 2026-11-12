---
title: "ICWShell Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html"
---

# ICWShell Interface Members

The following tables list the members exposed by [ICWShell](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CompositeOptions | Gets the options for this composite shell. |
| Property | EntityCount | Gets the number of entities in the shell. |
| Property | Formulation | Gets or sets the formulation type for the shell. |
| Property | Name | Gets the name of the shell. |
| Property | ShellOffsetOption | Gets or sets the shell offset option. |
| Property | ShellOffsetValue | Gets or sets the shell offset value. |
| Property | ShellThickness | Gets or sets the shell thickness. |
| Property | ShellUnit | Gets or sets the units for the shell thickness. |
| Property | State | Gets the state of suppression of the shell. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetDefaultMaterial | Gets the CAD material of the shell. |
| Method | GetDisplayName | Gets the name of this shell as displayed in the Simulation tree. |
| Method | GetEntityAt | Gets the entity at the specified index. |
| Method | GetShellMaterial | Gets the material applied to the shell for analysis. |
| Method | InsertEntity | Inserts an entity. |
| Method | RemoveEntity | Removes the entity at the specified index from the shell. |
| Method | SetFavMaterial | Obsolete. Superseded by ICWShell::SetFavMaterial2 . |
| Method | SetFavMaterial2 | Applies the specified material from the material favorites list. |
| Method | SetLibraryMaterial | Obsolete. Superseded by ICWShell::SetLibraryMaterial2 . |
| Method | SetLibraryMaterial2 | Sets the material library and material name for the shell. |
| Method | SetShellMaterial | Sets the material to apply to the shell for analysis. |
| Method | ShellBeginEdit | Starts editing the shell. |
| Method | ShellEndEdit | Ends editing a shell. |
| Method | SuppressUnSuppress | Suppresses or unsuppresses the shell depending on its state . |

[Top](#topBookmark)

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWShellManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager.html)
[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
