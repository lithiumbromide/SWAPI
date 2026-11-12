---
title: "SetDistance Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "SetDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetDistance.html"
---

# SetDistance Method (IVariableFilletFeatureData2)

Sets the Distance 2 radius for this asymmetric fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDistance( _
   ByVal PFilletItem As System.Object, _
   ByVal Dist2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As System.Object
Dim Dist2 As System.Double

instance.SetDistance(PFilletItem, Dist2)
```

### C#

```csharp
void SetDistance(
   System.object PFilletItem,
   System.double Dist2
)
```

### C++/CLI

```cpp
void SetDistance(
   System.Object^ PFilletItem,
   System.double Dist2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: [Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) at which to set the Distance 2 radius
- `Dist2`: Distance 2 radius at the vertex specified by PFilletItem

## VBA Syntax

See [VariableFilletFeatureData2::SetDistance](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~SetDistance.html).

## Remarks

Call [IVariableFilletFeatureData2::SetRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.html) to set the Distance 1 radius at the vertex.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetDistance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetDistance.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
