---
title: "RelativeComponent Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "RelativeComponent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~RelativeComponent.html"
---

# RelativeComponent Property (ISimulationMotorFeatureData)

Gets or sets a part in the assembly to which to reference motion when setting motion relative to another part in this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RelativeComponent As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim value As Component2

instance.RelativeComponent = value

value = instance.RelativeComponent
```

### C#

```csharp
Component2 RelativeComponent {get; set;}
```

### C++/CLI

```cpp
property Component2^ RelativeComponent {
   Component2^ get();
   void set (    Component2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Relative [component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [SimulationMotorFeatureData::RelativeComponent](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~RelativeComponent.html).

## Examples

[Create Linear Motor Feature (VBA)](Create_Linear_Motor_Feature_Example_VB.htm)

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::Location Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Location.html)
[ISimulationMotorFeatureData::LoadReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~LoadReferences.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
