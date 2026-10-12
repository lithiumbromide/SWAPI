---
title: "ActionDirection Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "ActionDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionDirection.html"
---

# ActionDirection Property (ISimulationForceFeatureData)

Gets or sets the direction of the force.

## Syntax

### Visual Basic (Declaration)

```vb
Property ActionDirection As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim value As System.Object

instance.ActionDirection = value

value = instance.ActionDirection
```

### C#

```csharp
System.object ActionDirection {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ActionDirection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Along an axis defined by an edge or a plane

Along the line-of-sight between two points

## VBA Syntax

See [SimulationForceFeatureData::ActionDirection](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~ActionDirection.html).

## Remarks

The way you define the directions of your forces depends on which forces you are creating. If you are creating an action-only force, the force direction remains fixed with respect to some part in your model, either a moving part or the ground part. In this case, you can define the force direction using one vector defined by an edge or a plane.

If you are creating an action/reaction force, then the direction along which you want the force applied is defined by the line between two points in your model and is constantly changing throughout the simulation. In this case, you can define the force direction as the line between the two points.

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::ActionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionLocation.html)
[ISimulationForceFeatureData::ActionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionType.html)
[ISimulationForceFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReverseDirection.html)
[ISimulationForceFeatureData::ReactionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReactionLocation.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
