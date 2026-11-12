---
title: "WeightFactor Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "WeightFactor"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~WeightFactor.html"
---

# WeightFactor Property (ICWMeshControl)

Gets or sets the component weight factor for the mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Property WeightFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Double

instance.WeightFactor = value

value = instance.WeightFactor
```

### C#

```csharp
System.double WeightFactor {get; set;}
```

### C++/CLI

```cpp
property System.double WeightFactor {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Component weight factor as defined in [swsMeshControlWeightFactor_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshControlWeightFactor_e.html)

## VBA Syntax

See [CWMeshControl::WeightFactor](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~WeightFactor.html).

## Remarks

The weight factor results in using a different element size for each selected component based on its significance.

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
