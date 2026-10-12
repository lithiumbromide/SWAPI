---
title: "SetEndPoints Method (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "SetEndPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~SetEndPoints.html"
---

# SetEndPoints Method (ISimulationSpringFeatureData)

Sets the end points for this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEndPoints( _
   ByVal PDirDisp1 As System.Object, _
   ByVal PDirDisp2 As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim PDirDisp1 As System.Object
Dim PDirDisp2 As System.Object
Dim value As System.Boolean

value = instance.SetEndPoints(PDirDisp1, PDirDisp2)
```

### C#

```csharp
System.bool SetEndPoints(
   System.object PDirDisp1,
   System.object PDirDisp2
)
```

### C++/CLI

```cpp
System.bool SetEndPoints(
   System.Object^ PDirDisp1,
   System.Object^ PDirDisp2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PDirDisp1`: Feature
- `PDirDisp2`: Feature

## VBA Syntax

See [SimulationSpringFeatureData::SetEndPoints](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~SetEndPoints.html).

## Examples

[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::GetEndPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~GetEndPoints.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
