---
title: "Shape Property (IRevisionCloud)"
project: "SOLIDWORKS API Help"
interface: "IRevisionCloud"
member: "Shape"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~Shape.html"
---

# Shape Property (IRevisionCloud)

Gets the shape of this revision cloud annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Shape As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionCloud
Dim value As System.Integer

value = instance.Shape
```

### C#

```csharp
System.int Shape {get;}
```

### C++/CLI

```cpp
property System.int Shape {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Revision cloud annotation shape as defined in [swRevisionCloudShape_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevisionCloudShape_e.html)

## VBA Syntax

See [RevisionCloud::Shape](ms-its:sldworksapivb6.chm::/sldworks~RevisionCloud~Shape.html).

## See Also

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.html)
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
