---
title: "IEdmUserGroup9 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserGroup9"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup9.html"
---

# IEdmUserGroup9 Interface

Allows you to access a user group in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmUserGroup9
   Inherits IEdmObject5, IEdmUserGroup5, IEdmUserGroup6, IEdmUserGroup7, IEdmUserGroup8
```

### C#

```csharp
public interface IEdmUserGroup9 : IEdmObject5, IEdmUserGroup5, IEdmUserGroup6, IEdmUserGroup7, IEdmUserGroup8
```

### C++/CLI

```cpp
public interface class IEdmUserGroup9 : public IEdmObject5, IEdmUserGroup5, IEdmUserGroup6, IEdmUserGroup7, IEdmUserGroup8
```

## Remarks

This interface extends [IEdmUserGroup8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup8.html) by providing the ability to specify these user group settings:

- Automatically delete local read-only files that are not part of the file vault.
- Always work with the latest version of files.
- Auto-select reference files to get latest when checking out.

## Accessors

See the [IEdmUserGroup5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5.html) accessors.

## See Also

[IEdmUserGroup9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup9_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
