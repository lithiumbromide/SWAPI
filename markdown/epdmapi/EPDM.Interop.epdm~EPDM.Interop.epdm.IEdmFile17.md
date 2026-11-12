---
title: "IEdmFile17 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile17"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile17.html"
---

# IEdmFile17 Interface

Allows you to access a file in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFile17
   Inherits IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile14, IEdmFile15, IEdmFile16, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C#

```csharp
public interface IEdmFile17 : IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile14, IEdmFile15, IEdmFile16, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFile17 : public IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile14, IEdmFile15, IEdmFile16, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

## Remarks

This interface:

- extends [IEdmFile16](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile16.html) by allowing you to determine whether a file has cut list items.
- is extended by [IEdmFile18](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile18.html).

To access an item in the vault, cast this interface's object to an [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html).

## See Also

[IEdmFile17 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile17_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
