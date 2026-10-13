---
title: "IEdmFile13 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile13"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13.html"
---

# IEdmFile13 Interface

Allows you to access a file in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFile13
   Inherits IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C#

```csharp
public interface IEdmFile13 : IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFile13 : public IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## Remarks

This interface:

extends [IEdmFile12](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile12.html) by providing the ability to:

- select which transition to use when changing state.
- get a thumbnail, if available, of a file.

is extended by [IEdmFile14](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile14.html).

To access an item in the vault, cast this interface's object to an [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html).

## See Also

[IEdmFile13 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
