---
title: "ActionLocation Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "ActionLocation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionLocation.html"
---

# ActionLocation Property (ISimulationForceFeatureData)

Gets or sets the location at which to apply the force for an action-only force.

## Syntax

### Visual Basic (Declaration)

```vb
Property ActionLocation As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim value As System.Object

instance.ActionLocation = value

value = instance.ActionLocation
```

### C#

```csharp
System.object ActionLocation {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ActionLocation {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Vertex, circular edge, or linear edge to define the points at which the moment is applied

## VBA Syntax

See [SimulationForceFeatureData::ActionLocation](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~ActionLocation.html).

## Examples

[Create Force Feature (VBA)](Create_Force_Feature_Example_VB.htm)

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::ActionDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionDirection.html)
[ISimulationForceFeatureData::ActionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionType.html)
[ISimulationForceFeatureData::ReactionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReactionLocation.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
