---
title: "GetEndPoints Method (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "GetEndPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~GetEndPoints.html"
---

# GetEndPoints Method (ISimulationSpringFeatureData)

Gets the end points for this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndPoints( _
   ByRef PDirDisp1 As System.Object, _
   ByRef PDirDisp2 As System.Object, _
   ByRef Type1 As System.Integer, _
   ByRef Type2 As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim PDirDisp1 As System.Object
Dim PDirDisp2 As System.Object
Dim Type1 As System.Integer
Dim Type2 As System.Integer
Dim value As System.Boolean

value = instance.GetEndPoints(PDirDisp1, PDirDisp2, Type1, Type2)
```

### C#

```csharp
System.bool GetEndPoints(
   out System.object PDirDisp1,
   out System.object PDirDisp2,
   out System.int Type1,
   out System.int Type2
)
```

### C++/CLI

```cpp
System.bool GetEndPoints(
   [Out] System.Object^ PDirDisp1,
   [Out] System.Object^ PDirDisp2,
   [Out] System.int Type1,
   [Out] System.int Type2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PDirDisp1`: Feature
- `PDirDisp2`: Feature
- `Type1`: Type of end point as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `Type2`: Type of end point as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [SimulationSpringFeatureData::GetEndPoints](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~GetEndPoints.html).

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::SetEndPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~SetEndPoints.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
