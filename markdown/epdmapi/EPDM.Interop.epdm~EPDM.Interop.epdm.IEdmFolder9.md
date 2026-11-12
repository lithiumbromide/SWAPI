---
title: "IEdmFolder9 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder9"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder9.html"
---

# IEdmFolder9 Interface

Allows you to access the contents of a file system folder in the vault.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFolder9
   Inherits IEdmFolder5, IEdmFolder6, IEdmFolder7, IEdmFolder8, IEdmObject5
```

### C#

```csharp
public interface IEdmFolder9 : IEdmFolder5, IEdmFolder6, IEdmFolder7, IEdmFolder8, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFolder9 : public IEdmFolder5, IEdmFolder6, IEdmFolder7, IEdmFolder8, IEdmObject5
```

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## Remarks

This interface:

- extends [IEdmFolder8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8.html) by providing the ability to query whether the user has permission to rename a file in this folder.
- is extended by [IEdmFolder10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder10.html).

## See Also

[IEdmFolder9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder9_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
