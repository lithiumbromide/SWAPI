---
title: "ReferenceComponent Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "ReferenceComponent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReferenceComponent.html"
---

# ReferenceComponent Property (ISimulationForceFeatureData)

Gets or sets the component to serve as a reference frame for the force.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferenceComponent As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim value As Component2

instance.ReferenceComponent = value

value = instance.ReferenceComponent
```

### C#

```csharp
Component2 ReferenceComponent {get; set;}
```

### C++/CLI

```cpp
property Component2^ ReferenceComponent {
   Component2^ get();
   void set (    Component2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) to serve as a reference frame

## VBA Syntax

See [SimulationForceFeatureData::ReferenceComponent](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~ReferenceComponent.html).

## Examples

[Create Force Feature (VBA)](Create_Force_Feature_Example_VB.htm)

## Remarks

Specifying a component to serve as a reference frame is optional. If a component is not specified, then the reference frame is the global ground.

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
