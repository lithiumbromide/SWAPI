---
title: "IEdmFile15 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile15"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile15.html"
---

# IEdmFile15 Interface

Allows you to access a file in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFile15
   Inherits IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile14, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C#

```csharp
public interface IEdmFile15 : IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile14, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFile15 : public IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile14, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

## Remarks

This interface:

- Extends [IEdmFile14](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile14.html) by getting a file's thumbnail by file version.
- Is extended by [IEdmFile16](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile16.html).

To access an item in the vault, cast this interface's object to an [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html).

## See Also

[IEdmFile15 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile15_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
