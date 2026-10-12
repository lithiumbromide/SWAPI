---
title: "Z Property (ISplineHandle)"
project: "SOLIDWORKS API Help"
interface: "ISplineHandle"
member: "Z"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Z.html"
---

# Z Property (ISplineHandle)

Gets or sets the z coordinate of the spline point.

## Syntax

### Visual Basic (Declaration)

```vb
Property Z As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineHandle
Dim value As System.Double

instance.Z = value

value = instance.Z
```

### C#

```csharp
System.double Z {get; set;}
```

### C++/CLI

```cpp
property System.double Z {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

z coordinate of the spline point

## VBA Syntax

See [SplineHandle::Z](ms-its:sldworksapivb6.chm::/sldworks~SplineHandle~Z.html).

## Examples

See the [ISplineHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html) examples.

## See Also

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html)
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html)
[ISplineHandle::X Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~X.html)
[ISplineHandle::Y Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Y.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
