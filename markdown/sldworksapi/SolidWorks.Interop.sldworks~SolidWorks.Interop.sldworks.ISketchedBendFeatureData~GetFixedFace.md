---
title: "GetFixedFace Method (ISketchedBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchedBendFeatureData"
member: "GetFixedFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~GetFixedFace.html"
---

# GetFixedFace Method (ISketchedBendFeatureData)

Gets the fixed face from this sketched bend.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFixedFace( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchedBendFeatureData
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.GetFixedFace(X, Y, Z)
```

### C#

```csharp
System.object GetFixedFace(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### C++/CLI

```cpp
System.Object^ GetFixedFace(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X location
- `Y`: Y location
- `Z`: Z location

### Return Value

Fixed [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) that does not move as a result of the bend

## VBA Syntax

See [SketchedBendFeatureData::GetFixedFace](ms-its:sldworksapivb6.chm::/sldworks~SketchedBendFeatureData~GetFixedFace.html).

## Examples

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

## Remarks

The location is a point on the fixed face, but in the space of the sketch used to define the sketched-bend feature. Thus, the z location is always 0.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.html)
[ISketchedBendFeatureData::SetFixedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~SetFixedFace.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
