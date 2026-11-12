---
title: "Axis Property (ISimulationGravityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationGravityFeatureData"
member: "Axis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData~Axis.html"
---

# Axis Property (ISimulationGravityFeatureData)

Gets or sets the axis for this Gravity feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Axis As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationGravityFeatureData
Dim value As System.Integer

instance.Axis = value

value = instance.Axis
```

### C#

```csharp
System.int Axis {get; set;}
```

### C++/CLI

```cpp
property System.int Axis {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Axis as defined in [swSimulationGravityAxisName_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationGravityAxisName_e.html)

## VBA Syntax

See [SimulationGravityFeatureData::Axis](ms-its:sldworksapivb6.chm::/sldworks~SimulationGravityFeatureData~Axis.html).

## Examples

See the [ISimulationGravityFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.html) examples.

## See Also

[ISimulationGravityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.html)
[ISimulationGravityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
