---
title: "IEdmFolder8 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder8"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8.html"
---

# IEdmFolder8 Interface

Allows you to access the contents of a file system folder in the vault.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFolder8
   Inherits IEdmFolder5, IEdmFolder6, IEdmFolder7, IEdmObject5
```

### C#

```csharp
public interface IEdmFolder8 : IEdmFolder5, IEdmFolder6, IEdmFolder7, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFolder8 : public IEdmFolder5, IEdmFolder6, IEdmFolder7, IEdmObject5
```

## Examples

[Add File (C#)](Add_File_Example_CSharp.htm)
[Add File (VB.NET)](Add_File_Example_VBNET.htm)
[Copy File (VB.NET)](Copy_File_Example_VBNET.htm)
[Copy File (C#)](Copy_File_Example_CSharp.htm)

## Remarks

This interface:

- extends [IEdmFolder7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder7.html) by adding the ability to add or copy a file, which already exists in the vault, to a different folder in the vault.
- is extended by [IEdmFolder9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder9.html).

## See Also

[IEdmFolder8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
