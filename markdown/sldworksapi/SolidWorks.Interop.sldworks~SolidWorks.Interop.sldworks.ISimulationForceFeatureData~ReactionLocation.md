---
title: "ReactionLocation Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "ReactionLocation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReactionLocation.html"
---

# ReactionLocation Property (ISimulationForceFeatureData)

Gets or sets the location at which to apply the force for an action/reaction force.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReactionLocation As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim value As System.Object

instance.ReactionLocation = value

value = instance.ReactionLocation
```

### C#

```csharp
System.object ReactionLocation {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ReactionLocation {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Vertex, circle/sphere/torus center, or edge midpoint

## VBA Syntax

See [SimulationForceFeatureData::ReactionLocation](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~ReactionLocation.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::ActionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionType.html)
[ISimulationForceFeatureData::ActionDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionDirection.html)
[ISimulationForceFeatureData::ActionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionLocation.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
