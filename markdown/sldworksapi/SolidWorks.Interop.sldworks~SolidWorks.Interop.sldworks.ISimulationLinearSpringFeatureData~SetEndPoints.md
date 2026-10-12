---
title: "SetEndPoints Method (ISimulationLinearSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationLinearSpringFeatureData"
member: "SetEndPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData~SetEndPoints.html"
---

# SetEndPoints Method (ISimulationLinearSpringFeatureData)

Obsolete. Superseded by [ISimulationSpringFeatureData::SetEndPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationSpringFeatureData~SetEndPoints.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEndPoints( _
   ByVal PDirDisp1 As System.Object, _
   ByVal PDirDisp2 As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationLinearSpringFeatureData
Dim PDirDisp1 As System.Object
Dim PDirDisp2 As System.Object

instance.SetEndPoints(PDirDisp1, PDirDisp2)
```

### C#

```csharp
void SetEndPoints(
   System.object PDirDisp1,
   System.object PDirDisp2
)
```

### C++/CLI

```cpp
void SetEndPoints(
   System.Object^ PDirDisp1,
   System.Object^ PDirDisp2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PDirDisp1`: Linear edge, vertex, or sketch point
- `PDirDisp2`: Linear edge, vertex, or sketch point

## VBA Syntax

See [SimulationLinearSpringFeatureData::SetEndPoints](ms-its:sldworksapivb6.chm::/sldworks~SimulationLinearSpringFeatureData~SetEndPoints.html).

## See Also

[ISimulationLinearSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData.html)
[ISimulationLinearSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData_members.html)
[ISimulationLinearspringFeatureData::GetEndPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData~GetEndPoints.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
