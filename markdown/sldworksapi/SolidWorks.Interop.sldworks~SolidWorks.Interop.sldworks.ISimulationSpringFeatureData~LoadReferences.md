---
title: "LoadReferences Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "LoadReferences"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~LoadReferences.html"
---

# LoadReferences Property (ISimulationSpringFeatureData)

Gets or sets the load references for this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property LoadReferences As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Object

instance.LoadReferences = value

value = instance.LoadReferences
```

### C#

```csharp
System.object LoadReferences {get; set;}
```

### C++/CLI

```cpp
property System.Object^ LoadReferences {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Load-bearing [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SimulationSpringFeatureData::LoadReferences](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~LoadReferences.html).

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
