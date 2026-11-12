---
title: "IEdmFile18 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile18"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile18.html"
---

# IEdmFile18 Interface

Allows you to access a file in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFile18
   Inherits IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile14, IEdmFile15, IEdmFile16, IEdmFile17, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C#

```csharp
public interface IEdmFile18 : IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile14, IEdmFile15, IEdmFile16, IEdmFile17, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFile18 : public IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile14, IEdmFile15, IEdmFile16, IEdmFile17, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

## Remarks

This interface extends [IEdmFile17](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile17.html) by allowing you to retrieve a file's thumbnail handle.

To access an item in the vault, cast this interface's object to an [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html).

## See Also

[IEdmFile18 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile18_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
