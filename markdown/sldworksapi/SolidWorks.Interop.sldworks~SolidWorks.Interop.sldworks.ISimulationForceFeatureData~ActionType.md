---
title: "ActionType Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "ActionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionType.html"
---

# ActionType Property (ISimulationForceFeatureData)

Gets or sets the type of action for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ActionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim value As System.Integer

instance.ActionType = value

value = instance.ActionType
```

### C#

```csharp
System.int ActionType {get; set;}
```

### C++/CLI

```cpp
property System.int ActionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of action as defined in [swSimulationForceActionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationForceActionType_e.html)

## VBA Syntax

See [SimulationForceFeatureData::ActionType](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~ActionType.html).

## Examples

[Create Force Feature (VBA)](Create_Force_Feature_Example_VB.htm)

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::ActionDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionDirection.html)
[ISimulationForceFeatureData::ActionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionLocation.html)
[ISimulationForceFeatureData::ReactionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReactionLocation.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
