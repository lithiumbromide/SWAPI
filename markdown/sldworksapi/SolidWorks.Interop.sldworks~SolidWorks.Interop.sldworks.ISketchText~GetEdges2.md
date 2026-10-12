---
title: "GetEdges2 Method (ISketchText)"
project: "SOLIDWORKS API Help"
interface: "ISketchText"
member: "GetEdges2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetEdges2.html"
---

# GetEdges2 Method (ISketchText)

Gets the edges for this sketch text.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdges2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchText
Dim value As System.Object

value = instance.GetEdges2()
```

### C#

```csharp
System.object GetEdges2()
```

### C++/CLI

```cpp
System.Object^ GetEdges2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [SketchText::GetEdges2](ms-its:sldworksapivb6.chm::/sldworks~SketchText~GetEdges2.html).

## Remarks

The difference between this method and the now obsolete ISketchText::GetEdges is this method also gets the edges of sketch text rendered with "stick" or single line fonts such as OLF SimpleSansOC.

The edges returned by this method are transient and should be regarded as read only. They can be used to obtain the underlying [ICurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) objects, but should not be used for manipulation or to obtain any other objects. These pointers should not be saved; if they are needed again, they should be obtained at that time.

## See Also

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.html)
[ISketchText::EnumEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~EnumEdges.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
