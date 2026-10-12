---
title: "IClosestDistance Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IClosestDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IClosestDistance.html"
---

# IClosestDistance Method (IModelDoc2)

Calculates the distance and closest points between two geometric objects.

## Syntax

### Visual Basic (Declaration)

```vb
Function IClosestDistance( _
   ByVal Object1 As System.Object, _
   ByVal Object2 As System.Object, _
   ByRef Point1 As System.Double, _
   ByRef Point2 As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Object1 As System.Object
Dim Object2 As System.Object
Dim Point1 As System.Double
Dim Point2 As System.Double
Dim value As System.Double

value = instance.IClosestDistance(Object1, Object2, Point1, Point2)
```

### C#

```csharp
System.double IClosestDistance(
   System.object Object1,
   System.object Object2,
   out System.double Point1,
   out System.double Point2
)
```

### C++/CLI

```cpp
System.double IClosestDistance(
   System.Object^ Object1,
   System.Object^ Object2,
   [Out] System.double Point1,
   [Out] System.double Point2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Object1`: Pointer to first object
- `Object2`: Pointer to second object
- `Point1`: Array of x, y, z coordinates for the first point
- `Point2`: Array of x, y, z coordinates for the second point

### Return Value

Minimum distance; -1.0 if no solution

## VBA Syntax

See [ModelDoc2::IClosestDistance](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IClosestDistance.html).

## Remarks

Supported input object types include:

- swSelFACES (face)
- swSelEDGES (edge)
- swSelVERTICES (vertex)
- swSelSKETCHSEGS (sketch segments)
- swSelDATUMPLANES (reference plane)
- swSelEXTSKETCHPOINTS (point on origin)
- swSelDATUMAXES (reference axis)
- swSelCOMPONENTS (component)
- swSelREFCURVES (reference curves)

This method includes these restrictions for drawings:

- Cannot measure between a sketch entity and a model entity
- Measured sketch entities have to belong to the same sheet
- Model entity measurements are based on the model origin
- Measured object cannot be a temporary geometric entity

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
