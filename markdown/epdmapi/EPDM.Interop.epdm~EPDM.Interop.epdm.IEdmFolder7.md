---
title: "IEdmFolder7 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder7"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder7.html"
---

# IEdmFolder7 Interface

Allows you to access the contents of a file system folder in the vault.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFolder7
   Inherits IEdmFolder5, IEdmFolder6, IEdmObject5
```

### C#

```csharp
public interface IEdmFolder7 : IEdmFolder5, IEdmFolder6, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFolder7 : public IEdmFolder5, IEdmFolder6, IEdmObject5
```

## Remarks

This interface:

- extends [IEdmFolder6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6.html) by adding the ability to destroy deleted items in this folder.
- is extended by [IEdmFolder8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8.html) by adding the ability to add or copy a file, which already exists in the vault, to a different folder in the vault.

## See Also

[IEdmFolder7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder7_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
