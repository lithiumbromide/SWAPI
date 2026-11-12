---
title: "ReverseDirection Property (ISimulationGravityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationGravityFeatureData"
member: "ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData~ReverseDirection.html"
---

# ReverseDirection Property (ISimulationGravityFeatureData)

Gets or sets whether to reverse the direction of gravity.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationGravityFeatureData
Dim value As System.Boolean

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.bool ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of gravity, false to not

## VBA Syntax

See [SimulationGravityFeatureData::ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~SimulationGravityFeatureData~ReverseDirection.html).

## Examples

See the [ISimulationGravityFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.html) examples.

## See Also

[ISimulationGravityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.html)
[ISimulationGravityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData_members.html)
[ISimulationGravityFeatureData::DirectionReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData~DirectionReference.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
