---
title: "IEdmVault20 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault20"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20.html"
---

# IEdmVault20 Interface

Allows you to access a file vault.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmVault20
   Inherits IEdmVault10, IEdmVault11, IEdmVault12, IEdmVault13, IEdmVault14, IEdmVault15, IEdmVault16, IEdmVault17, IEdmVault18, IEdmVault19, IEdmVault5, IEdmVault6, IEdmVault7, IEdmVault8, IEdmVault9
```

### C#

```csharp
public interface IEdmVault20 : IEdmVault10, IEdmVault11, IEdmVault12, IEdmVault13, IEdmVault14, IEdmVault15, IEdmVault16, IEdmVault17, IEdmVault18, IEdmVault19, IEdmVault5, IEdmVault6, IEdmVault7, IEdmVault8, IEdmVault9
```

### C++/CLI

```cpp
public interface class IEdmVault20 : public IEdmVault10, IEdmVault11, IEdmVault12, IEdmVault13, IEdmVault14, IEdmVault15, IEdmVault16, IEdmVault17, IEdmVault18, IEdmVault19, IEdmVault5, IEdmVault6, IEdmVault7, IEdmVault8, IEdmVault9
```

## Examples

[Get a File's State Transitions (VB.NET)](Get_Files_State_Transitions_Example_VBNET.htm)
[Get a File's State Transitions (C#)](Get_Files_State_Transitions_Example_CSharp.htm)

## Remarks

This interface:

- extends [IEdmVault19](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19.html) by providing the ability to get whether a specified user must add a comment when making specified workflow transitions for specified documents.
- is extended by [IEdmVault21](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21.html).

## See Also

[IEdmVault20 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
