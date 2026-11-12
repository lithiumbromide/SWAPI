---
title: "ForceType Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "ForceType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ForceType.html"
---

# ForceType Property (ISimulationForceFeatureData)

Gets the type of force.

**NOTE: This property is a get-only property. Set is not implemented.**

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ForceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim value As System.Integer

value = instance.ForceType
```

### C#

```csharp
System.int ForceType {get;}
```

### C++/CLI

```cpp
property System.int ForceType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of force as defined in [swSimulationForceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationForceType_e.html)

## VBA Syntax

See [SimulationForceFeatureData::ForceType](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~ForceType.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
