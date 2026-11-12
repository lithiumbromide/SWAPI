---
title: "IEdmFile14 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile14"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile14.html"
---

# IEdmFile14 Interface

Allows you to access a file in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFile14
   Inherits IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C#

```csharp
public interface IEdmFile14 : IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFile14 : public IEdmFile10, IEdmFile11, IEdmFile12, IEdmFile13, IEdmFile5, IEdmFile6, IEdmFile7, IEdmFile8, IEdmFile9, IEdmObject5
```

## Remarks

This interface

extends [IEdmFile13](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13.html) by:

- providing the ability to generate configuration values for drawings or files lacking properties at the configuration level.
- getting the ID of the vault view in which a file is checked out.

is extended by [IEdmFile15](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile15.html).

To access an item in the vault, cast this interface's object to an [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html).

## See Also

[IEdmFile14 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile14_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
