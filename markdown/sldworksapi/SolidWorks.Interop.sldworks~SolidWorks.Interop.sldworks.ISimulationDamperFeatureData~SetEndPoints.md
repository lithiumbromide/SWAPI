---
title: "SetEndPoints Method (ISimulationDamperFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationDamperFeatureData"
member: "SetEndPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData~SetEndPoints.html"
---

# SetEndPoints Method (ISimulationDamperFeatureData)

Sets the end points for this damper feature.

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
Dim instance As ISimulationDamperFeatureData
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

- `PDirDisp1`: Damper end point
- `PDirDisp2`: Damper end point

### Return Value

True if the operation succeeds, false if it fails

## VBA Syntax

See [SimulationDamperFeatureData::SetEndPoints](ms-its:sldworksapivb6.chm::/sldworks~SimulationDamperFeatureData~SetEndPoints.html).

## Examples

See [ISimulationDamperFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationDamperFeatureData.html) examples.

## See Also

[ISimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.html)
[ISimulationDamperFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData_members.html)
[ISimulationDamperFeatureData::GetEndPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData~GetEndPoints.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
