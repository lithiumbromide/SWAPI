---
title: "ClosestDistance Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ClosestDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClosestDistance.html"
---

# ClosestDistance Method (IModelDoc2)

Calculates the minimum distance between the specified geometric objects.

## Syntax

### Visual Basic (Declaration)

```vb
Function ClosestDistance( _
   ByVal Object1 As System.Object, _
   ByVal Object2 As System.Object, _
   ByRef Point1 As System.Object, _
   ByRef Point2 As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Object1 As System.Object
Dim Object2 As System.Object
Dim Point1 As System.Object
Dim Point2 As System.Object
Dim value As System.Double

value = instance.ClosestDistance(Object1, Object2, Point1, Point2)
```

### C#

```csharp
System.double ClosestDistance(
   System.object Object1,
   System.object Object2,
   out System.object Point1,
   out System.object Point2
)
```

### C++/CLI

```cpp
System.double ClosestDistance(
   System.Object^ Object1,
   System.Object^ Object2,
   [Out] System.Object^ Point1,
   [Out] System.Object^ Point2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Object1`: Pointer to first object (see **Remarks**)
- `Object2`: Pointer to second object (see **Remarks**)
- `Point1`: Array of x, y, z coordinates for the point on Object1 that is nearest to Point2
- `Point2`: Array of x, y, z coordinates for the point on Object2 that is nearest to Point1

### Return Value

Distance in meters between Point1 and Point2; -1.0 if no solution

## VBA Syntax

See [ModelDoc2::ClosestDistance](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ClosestDistance.html).

## Examples

[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)
[Calculate Closest Distance Between Model Components (VBA)](Calculate_Closest_Distance_Between_Model_Components_Example_VB.htm)

## Remarks

Supported types of Object1 and Object2 include [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

- swSelFACES (face)
- swSelEDGES (edge)
- swSelVERTICES (vertex)
- swSelSKETCHSEGS (sketch segment)
- swSelDATUMPLANES (reference plane)
- swSelEXTSKETCHPOINTS (point on origin)
- swSelDATUMAXES (reference axis)
- swSelCOMPONENTS (component; multi-body part supported, but not multi-part sub-assembly)
- swSelREFCURVES (reference curve)
- swSelSOLIDBODIES (solid bodies only; surface bodies not supported)

This method has these restrictions for drawings:

- Cannot measure between a sketch entity and a model entity
- Measured sketch entities have to belong to the same sheet
- Model entity measurements are based on the model origin
- Measured object cannot be a temporary geometric entity

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
