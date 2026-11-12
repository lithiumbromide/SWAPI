---
title: "UpdateToModelChanges Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "UpdateToModelChanges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~UpdateToModelChanges.html"
---

# UpdateToModelChanges Property (ISimulationSpringFeatureData)

Gets or sets whether to have the [free length](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationSpringFeatureData~FreeLength.html) dynamically update model changes while the PropertyManager page is open.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpdateToModelChanges As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Boolean

instance.UpdateToModelChanges = value

value = instance.UpdateToModelChanges
```

### C#

```csharp
System.bool UpdateToModelChanges {get; set;}
```

### C++/CLI

```cpp
property System.bool UpdateToModelChanges {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Ture to have the free length dynamically update model changes while the PropertyManager page is open, false to not

## VBA Syntax

See [SimulationSpringFeatureData::UpdateToModelChanges](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~UpdateToModelChanges.html).

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
