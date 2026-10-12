---
title: "LoadReferences Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "LoadReferences"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~LoadReferences.html"
---

# LoadReferences Property (ISimulationForceFeatureData)

Gets or sets the load references for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property LoadReferences As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
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

Load-bearing [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [SimulationForceFeatureData::LoadReferences](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~LoadReferences.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
