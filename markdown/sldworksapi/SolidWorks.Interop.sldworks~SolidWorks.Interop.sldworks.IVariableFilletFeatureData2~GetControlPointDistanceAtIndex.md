---
title: "GetControlPointDistanceAtIndex Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetControlPointDistanceAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointDistanceAtIndex.html"
---

# GetControlPointDistanceAtIndex Method (IVariableFilletFeatureData2)

Gets the Distance 2 radius at the specified control point for the asymmetric fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetControlPointDistanceAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetControlPointDistanceAtIndex(Index)
```

### C#

```csharp
System.double GetControlPointDistanceAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetControlPointDistanceAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of control point for which to get the radius

### Return Value

Value of the Distance 2 radius at the specified control point for the asymmetric fillet

## VBA Syntax

See [VariableFilletFeatureData2::GetControlPointDistanceAtIndex](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetControlPointDistanceAtIndex.html).

## Remarks

Call [IVariableFilletFeatureData2::GetControlPointRadiusAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointRadiusAtIndex.html) to get the Distance 1 radius of the control point for this asymmetric fillet.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::SetControlPointDistanceAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointDistanceAtIndex.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
