---
title: "BaseComponent Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "BaseComponent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~BaseComponent.html"
---

# BaseComponent Property (ISimulationSpringFeatureData)

Gets or sets the base component for this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BaseComponent As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As Component2

instance.BaseComponent = value

value = instance.BaseComponent
```

### C#

```csharp
Component2 BaseComponent {get; set;}
```

### C++/CLI

```cpp
property Component2^ BaseComponent {
   Component2^ get();
   void set (    Component2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Base component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [SimulationSpringFeatureData::BaseComponent](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~BaseComponent.html).

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
