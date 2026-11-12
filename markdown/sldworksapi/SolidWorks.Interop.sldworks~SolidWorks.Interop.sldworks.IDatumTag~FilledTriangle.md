---
title: "FilledTriangle Property (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "FilledTriangle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~FilledTriangle.html"
---

# FilledTriangle Property (IDatumTag)

Gets or sets whether a filled triangle or empty triangle attaches to the model on the leader for this datum feature symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Property FilledTriangle As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim value As System.Boolean

instance.FilledTriangle = value

value = instance.FilledTriangle
```

### C#

```csharp
System.bool FilledTriangle {get; set;}
```

### C++/CLI

```cpp
property System.bool FilledTriangle {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this datum tag has a filled triangle, false if an empty triangle

## VBA Syntax

See [DatumTag::FilledTriangle](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~FilledTriangle.html).

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTriangleAtIndex.html)
[IDatumTag::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTriangleCount.html)
[IDatumTag::IGetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetTriangleAtIndex.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
