---
title: "SetControlPointDistanceAtIndex Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "SetControlPointDistanceAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointDistanceAtIndex.html"
---

# SetControlPointDistanceAtIndex Method (IVariableFilletFeatureData2)

Sets the Distance 2 radius at the specified control point for the asymmetric fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetControlPointDistanceAtIndex( _
   ByVal Index As System.Integer, _
   ByVal Dist2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim Dist2 As System.Double

instance.SetControlPointDistanceAtIndex(Index, Dist2)
```

### C#

```csharp
void SetControlPointDistanceAtIndex(
   System.int Index,
   System.double Dist2
)
```

### C++/CLI

```cpp
void SetControlPointDistanceAtIndex(
   System.int Index,
   System.double Dist2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of control point whose radius to set
- `Dist2`: Distance 2 radius for the control point of this asymmetric fillet

## VBA Syntax

See [VariableFilletFeatureData2::SetControlPointDistanceAtIndex](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~SetControlPointDistanceAtIndex.html).

## Remarks

Call [IVariableFilletFeatureData2::SetControlPointRadiusAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointRadiusAtIndex.html) to set the Distance 1 radius for the control point of this asymmetric fillet.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetControlPointDistanceAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointDistanceAtIndex.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
