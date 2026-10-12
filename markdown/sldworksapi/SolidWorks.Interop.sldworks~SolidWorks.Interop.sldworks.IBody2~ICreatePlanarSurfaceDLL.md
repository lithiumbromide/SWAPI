---
title: "ICreatePlanarSurfaceDLL Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreatePlanarSurfaceDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarSurfaceDLL.html"
---

# ICreatePlanarSurfaceDLL Method (IBody2)

Creates a planar surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePlanarSurfaceDLL( _
   ByRef RootPoint As System.Double, _
   ByRef Normal As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim RootPoint As System.Double
Dim Normal As System.Double
Dim value As Surface

value = instance.ICreatePlanarSurfaceDLL(RootPoint, Normal)
```

### C#

```csharp
Surface ICreatePlanarSurfaceDLL(
   ref System.double RootPoint,
   ref System.double Normal
)
```

### C++/CLI

```cpp
Surface^ ICreatePlanarSurfaceDLL(
   System.double% RootPoint,
   System.double% Normal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RootPoint`: Pointer to an array of 3 doubles (x,y,z)
- `Normal`: Pointer to an array of 3 doubles (x,y,z)

### Return Value

Pointer to the new planar surface

## VBA Syntax

See [Body2::ICreatePlanarSurfaceDLL](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreatePlanarSurfaceDLL.html).

## Remarks

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision number 10.0
