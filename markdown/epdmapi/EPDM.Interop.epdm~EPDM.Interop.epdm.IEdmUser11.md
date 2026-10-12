---
title: "IEdmUser11 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUser11"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser11.html"
---

# IEdmUser11 Interface

Allows you to access a user in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmUser11
   Inherits IEdmObject5, IEdmUser10, IEdmUser5, IEdmUser6, IEdmUser7, IEdmUser8, IEdmUser9
```

### C#

```csharp
public interface IEdmUser11 : IEdmObject5, IEdmUser10, IEdmUser5, IEdmUser6, IEdmUser7, IEdmUser8, IEdmUser9
```

### C++/CLI

```cpp
public interface class IEdmUser11 : public IEdmObject5, IEdmUser10, IEdmUser5, IEdmUser6, IEdmUser7, IEdmUser8, IEdmUser9
```

## Remarks

This interface extends [IEdmUser10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10.html) by providing the ability to specify these user settings:

- Automatically delete local read-only files in File Explorer that are not part of the file vault.
- Always work with the latest version of files.
- Auto-select reference files to get latest when checking out.

## Accessors

See the [IEdmUser5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5.html) accessors.

## See Also

[IEdmUser11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser11_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
