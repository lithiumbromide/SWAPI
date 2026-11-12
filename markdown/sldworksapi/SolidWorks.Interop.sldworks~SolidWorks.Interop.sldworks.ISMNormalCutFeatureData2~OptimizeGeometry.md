---
title: "OptimizeGeometry Property (ISMNormalCutFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData2"
member: "OptimizeGeometry"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~OptimizeGeometry.html"
---

# OptimizeGeometry Property (ISMNormalCutFeatureData2)

Gets or sets whether to optimize the geometry of the Normal Cut.

## Syntax

### Visual Basic (Declaration)

```vb
Property OptimizeGeometry As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData2
Dim value As System.Boolean

instance.OptimizeGeometry = value

value = instance.OptimizeGeometry
```

### C#

```csharp
System.bool OptimizeGeometry {get; set;}
```

### C++/CLI

```cpp
property System.bool OptimizeGeometry {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to optimize the geometry of the Normal Cut, false to not

## VBA Syntax

See [SMNormalCutFeatureData2::OptimizeGeometry](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData2~OptimizeGeometry.html).

## Examples

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html) example.

## See Also

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html)
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
