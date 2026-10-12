---
title: "HasDamper Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "HasDamper"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~HasDamper.html"
---

# HasDamper Property (ISimulationSpringFeatureData)

Gets or sets whether this simulation spring feature has damper.

## Syntax

### Visual Basic (Declaration)

```vb
Property HasDamper As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Boolean

instance.HasDamper = value

value = instance.HasDamper
```

### C#

```csharp
System.bool HasDamper {get; set;}
```

### C++/CLI

```cpp
property System.bool HasDamper {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this simulation spring feature has damper, false if not

## VBA Syntax

See [SimulationSpringFeatureData::HasDamper](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~HasDamper.html).

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::DampingConstant Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~DampingConstant.html)
[ISimulationSpringFeatureData::ExponentOfDamperForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfDamperForceExpression.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
