---
title: "LockPath Property (IEdmSearchResult5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearchResult5"
member: "LockPath"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5~LockPath.html"
---

# LockPath Property (IEdmSearchResult5)

Gets the full path where the file is checked out.

## Syntax

### Visual Basic

```vb
ReadOnly Property LockPath As System.String
```

### C#

```csharp
System.string LockPath {get;}
```

### C++/CLI

```cpp
property System.String^ LockPath {
   System.String^ get();
}
```

### Property Value

Full path where the file is checked out; "" for folders or if the file is not checked out

## See Also

[IEdmSearchResult5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5.html)
[IEdmSearchResult5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5_members.html)
