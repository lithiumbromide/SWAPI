---
title: "IGetBoundingBox Method (IRefPlane)"
project: "SOLIDWORKS API Help"
interface: "IRefPlane"
member: "IGetBoundingBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~IGetBoundingBox.html"
---

# IGetBoundingBox Method (IRefPlane)

Gets the bounding box of the reference plane, the top-left and bottom-right points.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBoundingBox() As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlane
Dim value As MathPoint

value = instance.IGetBoundingBox()
```

### C#

```csharp
MathPoint IGetBoundingBox()
```

### C++/CLI

```cpp
MathPoint^ IGetBoundingBox();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array containing the bounding box, always two (2) [IMathpoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) objects

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)
[IRefPlane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane_members.html)
[IRefPlane::BoundingBox Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~BoundingBox.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
