---
title: "ReverseDirection Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ReverseDirection.html"
---

# ReverseDirection Property (ISimulationSpringFeatureData)

Gets or sets whether to reverse the direction of this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Boolean

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.bool ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of this simulation spring feature, false to not

## VBA Syntax

See [SimulationSpringFeatureData::ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~ReverseDirection.html).

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
