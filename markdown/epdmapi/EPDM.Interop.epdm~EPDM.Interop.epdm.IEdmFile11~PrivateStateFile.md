---
title: "PrivateStateFile Property (IEdmFile11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile11"
member: "PrivateStateFile"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile11~PrivateStateFile.html"
---

# PrivateStateFile Property (IEdmFile11)

Gets whether this file is in a private state.

## Syntax

### Visual Basic

```vb
ReadOnly Property PrivateStateFile As System.Boolean
```

### C#

```csharp
System.bool PrivateStateFile {get;}
```

### C++/CLI

```cpp
property System.bool PrivateStateFile {
   System.bool get();
}
```

### Property Value

True if this file is in a private state, false if not

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## Remarks

Files in a private state:

- are accessible only to the user adding them and the SOLIDWORKS PDM Professional Admin user.
- have no assigned workflow or category.

## See Also

[IEdmFile11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile11.html)
[IEdmFile11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile11_members.html)

## Availability

SOLIDWORKS PDM Professional 2015 SP02
