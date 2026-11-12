---
title: "ParentFolder Property (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "ParentFolder"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~ParentFolder.html"
---

# ParentFolder Property (IEdmFolder5)

Gets the interface to the parent folder of this folder.

## Syntax

### Visual Basic

```vb
ReadOnly Property ParentFolder As IEdmFolder5
```

### C#

```csharp
IEdmFolder5 ParentFolder {get;}
```

### C++/CLI

```cpp
property IEdmFolder5^ ParentFolder {
   IEdmFolder5^ get();
}
```

### Property Value

[IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html); Null if this folder is the root folder

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
