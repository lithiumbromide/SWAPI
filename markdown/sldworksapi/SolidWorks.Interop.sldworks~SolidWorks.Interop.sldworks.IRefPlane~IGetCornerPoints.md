---
title: "IGetCornerPoints Method (IRefPlane)"
project: "SOLIDWORKS API Help"
interface: "IRefPlane"
member: "IGetCornerPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~IGetCornerPoints.html"
---

# IGetCornerPoints Method (IRefPlane)

Gets the corner points of this reference plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCornerPoints() As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlane
Dim value As MathPoint

value = instance.IGetCornerPoints()
```

### C#

```csharp
MathPoint IGetCornerPoints()
```

### C++/CLI

```cpp
MathPoint^ IGetCornerPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of four (4) [IMathpoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) objects

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)
[IRefPlane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane_members.html)
[IRefPlane::CornerPoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~CornerPoints.html)

## Availability

SOLIDWORKS 2009 SP5, Revision Number 17.5
