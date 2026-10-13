---
title: "EnumEdges Method (ISketchText)"
project: "SOLIDWORKS API Help"
interface: "ISketchText"
member: "EnumEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~EnumEdges.html"
---

# EnumEdges Method (ISketchText)

Gets the edges in this sketch text.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumEdges() As EnumEdges
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchText
Dim value As EnumEdges

value = instance.EnumEdges()
```

### C#

```csharp
EnumEdges EnumEdges()
```

### C++/CLI

```cpp
EnumEdges^ EnumEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Edges enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumEdges.html)

## VBA Syntax

See [SketchText::EnumEdges](ms-its:sldworksapivb6.chm::/sldworks~SketchText~EnumEdges.html).

## Remarks

The edges returned by this method are transient and should be regarded as read only. They can be used to obtain the underlying [ICurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) objects, but should not be used for manipulation or to obtain any other objects through them. These pointers should not be saved; if they are needed again, they should be obtained at that time.

## See Also

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.html)
[ISketchText::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetEdges.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
