---
title: "SetEndPoints Method (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "SetEndPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetEndPoints.html"
---

# SetEndPoints Method (ISimulationForceFeatureData)

Sets the end points for this Force feature.

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
Dim instance As ISimulationForceFeatureData
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

- `PDirDisp1`: Force end point
- `PDirDisp2`: Force end point

### Return Value

True if the operation succeeds, false if it fails

## VBA Syntax

See [SimulationForceFeatureData::SetEndPoints](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~SetEndPoints.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::GetEndPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetEndPoints.html)

## Availability

lidWorks 2009 FCS, Revision Number 17.0
