---
title: "GetDisplayDimension Method (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "GetDisplayDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetDisplayDimension.html"
---

# GetDisplayDimension Method (ISketchRelation)

Gets the display dimension object for this sketch relation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayDimension() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim value As System.Object

value = instance.GetDisplayDimension()
```

### C#

```csharp
System.object GetDisplayDimension()
```

### C++/CLI

```cpp
System.Object^ GetDisplayDimension();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [SketchRelation::GetDisplayDimension](ms-its:sldworksapivb6.chm::/sldworks~SketchRelation~GetDisplayDimension.html).

## Examples

[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
