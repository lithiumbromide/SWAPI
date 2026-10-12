---
title: "DirectionReference Property (ISimulationGravityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationGravityFeatureData"
member: "DirectionReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData~DirectionReference.html"
---

# DirectionReference Property (ISimulationGravityFeatureData)

Gets or sets the direction of in which gravity moves.

## Syntax

### Visual Basic (Declaration)

```vb
Property DirectionReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationGravityFeatureData
Dim value As System.Object

instance.DirectionReference = value

value = instance.DirectionReference
```

### C#

```csharp
System.object DirectionReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ DirectionReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Linear edge, planar face, axis, or plane indicating the direction of gravity

## VBA Syntax

See [SimulationGravityFeatureData::DirectionReference](ms-its:sldworksapivb6.chm::/sldworks~SimulationGravityFeatureData~DirectionReference.html).

## See Also

[ISimulationGravityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.html)
[ISimulationGravityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData_members.html)
[ISimulationGravityFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData~ReverseDirection.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
