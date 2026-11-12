---
title: "CheckFeatureUse Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "CheckFeatureUse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~CheckFeatureUse.html"
---

# CheckFeatureUse Method (ISketch)

Checks to see if this sketch is valid for use in creating a specified feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function CheckFeatureUse( _
   ByVal FeatureType As System.Integer, _
   ByRef OpenCount As System.Integer, _
   ByRef ClosedCount As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim FeatureType As System.Integer
Dim OpenCount As System.Integer
Dim ClosedCount As System.Integer
Dim value As System.Integer

value = instance.CheckFeatureUse(FeatureType, OpenCount, ClosedCount)
```

### C#

```csharp
System.int CheckFeatureUse(
   System.int FeatureType,
   out System.int OpenCount,
   out System.int ClosedCount
)
```

### C++/CLI

```cpp
System.int CheckFeatureUse(
   System.int FeatureType,
   [Out] System.int OpenCount,
   [Out] System.int ClosedCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatureType`: Determine if this type of feature can be created as defined in [swSketchCheckFeatureProfileUsage_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchCheckFeatureProfileUsage_e.html)
- `OpenCount`: Number of open contours found in this sketch
- `ClosedCount`: Number of closed contours found in this sketch

### Return Value

swSketchCheckFeatureStatus_OK if this sketch can be used to create the specified feature; see [swSketchCheckFeatureStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchCheckFeatureStatus_e.html) for possible failure values

## VBA Syntax

See [Sketch::CheckFeatureUse](ms-its:sldworksapivb6.chm::/sldworks~Sketch~CheckFeatureUse.html).

## Examples

[Determine If Sketch Suitable for Feature (VBA)](Determine_If_Sketch_Suitable_for_Feature_Example_VB.htm)

## Remarks

This method is equivalent to the SOLIDWORKS interactive tool Check Sketch for Feature Usage. See the SOLIDWORKS Help for details.

The OpenCount and ClosedCount arguments are output values. If this method returns swSketchCheckFeatureStatus_OK, meaning that the sketch can be used to create the specified feature, then these two arguments contain useful information. If this method returns something else, then OpenCount and ClosedCount both return 0.

If the featureType value is not valid, this method returns swSketchCheckFeatureStatus_UnknownError.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)

## Availability

SOLIDWORKS 2000 SP03, Revision Number 8.3
