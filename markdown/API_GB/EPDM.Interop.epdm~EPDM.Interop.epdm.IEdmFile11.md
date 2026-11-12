---
title: "IEdmFile11 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile11"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile11.html"
---

# IEdmFile11 Interface

Allows you to access a file in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFile11
   Inherits IEdmFile10, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C#

```csharp
public interface IEdmFile11 : IEdmFile10, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFile11 : public IEdmFile10, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## Remarks

This interface extends:

- extends [IEdmFile10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile10.html) by providing the ability to get whether a file is in a private state.
- is extended by [IEdmFile12](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile12.html).EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile10.html

To access an item in the vault, cast this interface's object to an [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html).

## See Also

[IEdmFile11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile11_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
