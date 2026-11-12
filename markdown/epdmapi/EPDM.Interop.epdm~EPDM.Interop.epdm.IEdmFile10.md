---
title: "IEdmFile10 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile10"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile10.html"
---

# IEdmFile10 Interface

Allows you to access a file in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFile10
   Inherits IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C#

```csharp
public interface IEdmFile10 : IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFile10 : public IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

## Remarks

This interface:

- extends [IEdmFile9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile9.html) by supporting password-protected workflow transitions.
- is extended by [IEdmFile11](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile11.html).

To access an item in the vault, cast this interface's object to an [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html).

## See Also

[IEdmFile10 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile10_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
