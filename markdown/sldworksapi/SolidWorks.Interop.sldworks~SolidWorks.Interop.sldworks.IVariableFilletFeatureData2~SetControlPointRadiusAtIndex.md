---
title: "SetControlPointRadiusAtIndex Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "SetControlPointRadiusAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointRadiusAtIndex.html"
---

# SetControlPointRadiusAtIndex Method (IVariableFilletFeatureData2)

Sets the radius at the specified control point.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetControlPointRadiusAtIndex( _
   ByVal Index As System.Integer, _
   ByVal Location As System.Double, _
   ByVal Radius As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim Location As System.Double
Dim Radius As System.Double

instance.SetControlPointRadiusAtIndex(Index, Location, Radius)
```

### C#

```csharp
void SetControlPointRadiusAtIndex(
   System.int Index,
   System.double Location,
   System.double Radius
)
```

### C++/CLI

```cpp
void SetControlPointRadiusAtIndex(
   System.int Index,
   System.double Location,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of control point whose radius to set
- `Location`: Percent distance between the edge start vertex and the edge end vertex
- `Radius`: Value of the radius for the control point of this symmetric fillet; Distance 1 radius for the control point of this asymmetric fillet

## VBA Syntax

See [VariableFilletFeatureData2::SetControlPointRadiusAtIndex](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~SetControlPointRadiusAtIndex.html).

## Remarks

Call [IVariableFilletFeatureData2::SetControlPointDistanceAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointDistanceAtIndex.html) to set the Distance 2 radius for the control point of this asymmetric fillet.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetControlPointRadiusAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointRadiusAtIndex.html)
[IVariableFilletFeatureData2::GetControlPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointsCount.html)
[IVariableFilletFeatureData2::SetControlPointConicRhoOrRadiusAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointConicRhoOrRadiusAtIndex.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
