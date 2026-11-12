---
title: "IEdmVault19 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault19"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19.html"
---

# IEdmVault19 Interface

Allows you to access a file vault.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmVault19
   Inherits IEdmVault10, IEdmVault11, IEdmVault12, IEdmVault13, IEdmVault14, IEdmVault15, IEdmVault16, IEdmVault17, IEdmVault18, IEdmVault5, IEdmVault6, IEdmVault7, IEdmVault8, IEdmVault9
```

### C#

```csharp
public interface IEdmVault19 : IEdmVault10, IEdmVault11, IEdmVault12, IEdmVault13, IEdmVault14, IEdmVault15, IEdmVault16, IEdmVault17, IEdmVault18, IEdmVault5, IEdmVault6, IEdmVault7, IEdmVault8, IEdmVault9
```

### C++/CLI

```cpp
public interface class IEdmVault19 : public IEdmVault10, IEdmVault11, IEdmVault12, IEdmVault13, IEdmVault14, IEdmVault15, IEdmVault16, IEdmVault17, IEdmVault18, IEdmVault5, IEdmVault6, IEdmVault7, IEdmVault8, IEdmVault9
```

## Examples

[Copy Assembly Tree of Files (VB.NET)](Copy_Assembly_Tree_Example_VBNET.htm)
[Copy Assembly Tree of Files (C#)](Copy_Assembly_Tree_Example_CSharp.htm)

## Remarks

This interface:

- extends [IEdmVault18](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault18.html) by providing the ability to:

  - Call the Set Revision command to update a revision table in a SOLIDWORKS drawing in this vault.
  - Copy an assembly tree of referenced parts and drawings to a destination folder.

- is extended by [IEdmVault20](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20.html).

## See Also

[IEdmVault19 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
