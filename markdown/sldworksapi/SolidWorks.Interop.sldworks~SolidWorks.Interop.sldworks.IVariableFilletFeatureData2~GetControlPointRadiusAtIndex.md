---
title: "GetControlPointRadiusAtIndex Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetControlPointRadiusAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointRadiusAtIndex.html"
---

# GetControlPointRadiusAtIndex Method (IVariableFilletFeatureData2)

Gets the radius at the specified control point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetControlPointRadiusAtIndex( _
   ByVal Index As System.Integer, _
   ByRef Location As System.Double, _
   ByRef PEdge As Edge _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim Location As System.Double
Dim PEdge As Edge
Dim value As System.Double

value = instance.GetControlPointRadiusAtIndex(Index, Location, PEdge)
```

### C#

```csharp
System.double GetControlPointRadiusAtIndex(
   System.int Index,
   out System.double Location,
   out Edge PEdge
)
```

### C++/CLI

```cpp
System.double GetControlPointRadiusAtIndex(
   System.int Index,
   [Out] System.double Location,
   [Out] Edge^ PEdge
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of the control point
- `Location`: Location of the control point
- `PEdge`: [Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

### Return Value

Value of the radius at the specified control point for the symmetric fillet; value of the Distance 1 radius at the specified control point for the asymmetric fillet (see **Remarks**)

## VBA Syntax

See [VariableFilletFeatureData2::GetControlPointRadiusAtIndex](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetControlPointRadiusAtIndex.html).

## Remarks

Call [IVariableFilletFeatureData2::GetControlPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointsCount.html) before calling this method.

Call [IVariableFilletFeatureData2::GetControlPointDistanceAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointDistanceAtIndex.html) to get the Distance 2 radius for the control point of the asymmetric fillet.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::SetControlPointRadiusAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointRadiusAtIndex.html)
[IVariableFilletFeatureData2::GetControlPointConicRhoOrRadiusAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointConicRhoOrRadiusAtIndex.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
