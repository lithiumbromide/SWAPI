---
title: "LockedByUserID Property (IEdmSearchResult5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearchResult5"
member: "LockedByUserID"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5~LockedByUserID.html"
---

# LockedByUserID Property (IEdmSearchResult5)

Gets the ID of the user who has the file checked out.

## Syntax

### Visual Basic

```vb
ReadOnly Property LockedByUserID As System.Integer
```

### C#

```csharp
System.int LockedByUserID {get;}
```

### C++/CLI

```cpp
property System.int LockedByUserID {
   System.int get();
}
```

### Property Value

ID of user who has file checked out; 1 if the file is not checked out

## See Also

[IEdmSearchResult5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5.html)
[IEdmSearchResult5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5_members.html)
