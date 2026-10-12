---
title: "Location Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "Location"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Location.html"
---

# Location Property (ISimulationMotorFeatureData)

Select a face, vertex, or edge on the assembly for the reference origin when setting motion relative to another part.

## Syntax

### Visual Basic (Declaration)

```vb
Property Location As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim value As System.Object

instance.Location = value

value = instance.Location
```

### C#

```csharp
System.object Location {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Location {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html), or [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [SimulationMotorFeatureData::Location](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~Location.html).

## Examples

[Create Linear Motor Feature (VBA)](Create_Linear_Motor_Feature_Example_VB.htm)

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::RelativeComponent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~RelativeComponent.html)
[ISimulationMotorFeatureData::LoadReferances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~LoadReferences.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
