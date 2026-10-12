---
title: "BaseComponent Property (ISimulationDamperFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationDamperFeatureData"
member: "BaseComponent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData~BaseComponent.html"
---

# BaseComponent Property (ISimulationDamperFeatureData)

Gets or sets the base component for this damper feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BaseComponent As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationDamperFeatureData
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

Base [component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [SimulationDamperFeatureData::BaseComponent](ms-its:sldworksapivb6.chm::/sldworks~SimulationDamperFeatureData~BaseComponent.html).

## See Also

[ISimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.html)
[ISimulationDamperFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
