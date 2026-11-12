---
title: "GetEndPoints Method (ISimulationLinearSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationLinearSpringFeatureData"
member: "GetEndPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData~GetEndPoints.html"
---

# GetEndPoints Method (ISimulationLinearSpringFeatureData)

Obsolete. Superseded by [ISimulationSpringFeatureData::GetEndPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationSpringFeatureData~GetEndPoints.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetEndPoints( _
   ByRef PDirDisp1 As System.Object, _
   ByRef PDirDisp2 As System.Object, _
   ByRef Type1 As System.Integer, _
   ByRef Type2 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationLinearSpringFeatureData
Dim PDirDisp1 As System.Object
Dim PDirDisp2 As System.Object
Dim Type1 As System.Integer
Dim Type2 As System.Integer

instance.GetEndPoints(PDirDisp1, PDirDisp2, Type1, Type2)
```

### C#

```csharp
void GetEndPoints(
   out System.object PDirDisp1,
   out System.object PDirDisp2,
   out System.int Type1,
   out System.int Type2
)
```

### C++/CLI

```cpp
void GetEndPoints(
   [Out] System.Object^ PDirDisp1,
   [Out] System.Object^ PDirDisp2,
   [Out] System.int Type1,
   [Out] System.int Type2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PDirDisp1`: Linear edge, vertex, sketch segment, or sketch point
- `PDirDisp2`: Linear edge, vertex, sketch segment, or sketch point
- `Type1`: Type of end point as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `Type2`: Type of end point as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [SimulationLinearSpringFeatureData::GetEndPoints](ms-its:sldworksapivb6.chm::/sldworks~SimulationLinearSpringFeatureData~GetEndPoints.html).

## See Also

[ISimulationLinearSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData.html)
[ISimulationLinearSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData_members.html)
[ISimulationLinearSpringFeatureData::SetEndPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData~SetEndPoints.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
