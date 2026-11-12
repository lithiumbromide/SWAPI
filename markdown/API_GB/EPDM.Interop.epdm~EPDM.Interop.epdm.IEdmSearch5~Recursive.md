---
title: "Recursive Property (IEdmSearch5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch5"
member: "Recursive"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~Recursive.html"
---

# Recursive Property (IEdmSearch5)

Gets or sets whether to search recursively in subfolders.

## Syntax

### Visual Basic

```vb
Property Recursive As System.Boolean
```

### C#

```csharp
System.bool Recursive {get; set;}
```

### C++/CLI

```cpp
property System.bool Recursive {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to search recursively in subfolders, false to search only in the folder specified by [IEdmSearch5::StartFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~StartFolderID.html)

## See Also

[IEdmSearch5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html)
[IEdmSearch5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
