---
title: "IEdmVault22 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault22"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22.html"
---

# IEdmVault22 Interface

Allows you to access a file vault.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmVault22
   Inherits IEdmVault10, IEdmVault11, IEdmVault12, IEdmVault13, IEdmVault14, IEdmVault15, IEdmVault16, IEdmVault17, IEdmVault18, IEdmVault19, IEdmVault20, IEdmVault21, IEdmVault5, IEdmVault6, IEdmVault7, IEdmVault8, IEdmVault9
```

### C#

```csharp
public interface IEdmVault22 : IEdmVault10, IEdmVault11, IEdmVault12, IEdmVault13, IEdmVault14, IEdmVault15, IEdmVault16, IEdmVault17, IEdmVault18, IEdmVault19, IEdmVault20, IEdmVault21, IEdmVault5, IEdmVault6, IEdmVault7, IEdmVault8, IEdmVault9
```

### C++/CLI

```cpp
public interface class IEdmVault22 : public IEdmVault10, IEdmVault11, IEdmVault12, IEdmVault13, IEdmVault14, IEdmVault15, IEdmVault16, IEdmVault17, IEdmVault18, IEdmVault19, IEdmVault20, IEdmVault21, IEdmVault5, IEdmVault6, IEdmVault7, IEdmVault8, IEdmVault9
```

## Examples

[Assign Columnset to Folder before Browsing Add-in (VB.NET)](Assign_Columnset_To_Folder_Before_Browsing_Addin_Example_VBNET.htm)

## Remarks

This interface extends [IEdmVault21](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21.html) by providing the ability to [clear the Archive Server Get logs](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~ClearLogs.html), [synchronize the vault's archive servers with the active directory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~ADRunSync.html), get all column sets assigned to the logged-in user, [get the current column set for the logged-in user](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~GetCurrentColumnSet.html), and set a column set ID in the user's registry.

With IEdmVault22, add-ins can assign customized column sets to vault folders before they are browsed by:

1. Triggering a pre-browse-folder event ([EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_PreBrowseFolder) when the logged-in user browses a folder.
2. Handling the event by:

  1. [Getting all the column set IDs assigned to the logged-in user](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~GetColumnSets.html).
  2. [Specifying a column set ID for the folder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~SetColumnSetID.html) to be browsed.
3. Triggering and handling a post-browse-folder event (EdmCmdType.EdmCmd_PostBrowseFolder).

For more information about customized column sets, see the **SOLIDWORKS PDM Help > SOLIDWORKS PDM Administration Tool > Columns** topics.

## See Also

[IEdmVault22 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
