---
title: "IsLocked Property (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "IsLocked"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~IsLocked.html"
---

# IsLocked Property (IEdmFile5)

Gets whether the file is checked out.

## Syntax

### Visual Basic

```vb
ReadOnly Property IsLocked As System.Boolean
```

### C#

```csharp
System.bool IsLocked {get;}
```

### C++/CLI

```cpp
property System.bool IsLocked {
   System.bool get();
}
```

### Property Value

True if the file is checked out, false if not

## Examples

[Traverse Folders and Files in Vault (C#)](Traverse_Folders_and_Files_in_Vault_Example_CSharp.htm)
[Traverse Folders and Files in Vault (VB.NET)](Traverse_Folders_and_Files_in_Vault_Example_VBNET.htm)
[Add Custom File Reference (VB.NET)](Add_Custom_File_Reference_Example_VBNET.htm)
[Add Custom File Reference (C#)](Add_Custom_File_Reference_Example_CSharp.htm)

## Remarks

In a multi-user implementation, a file can be checked in and out by others while you are working on it. Before using this property, call [IEdmFile5::Refresh](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~Refresh.html) to ensure this property gets the correct checkout status.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
