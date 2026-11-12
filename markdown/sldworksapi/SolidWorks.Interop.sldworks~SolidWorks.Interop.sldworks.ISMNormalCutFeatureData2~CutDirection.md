---
title: "CutDirection Property (ISMNormalCutFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData2"
member: "CutDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~CutDirection.html"
---

# CutDirection Property (ISMNormalCutFeatureData2)

Gets or sets the edge, linear curve, or planar face that defines the direction of the Normal Cut.

## Syntax

### Visual Basic (Declaration)

```vb
Property CutDirection As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData2
Dim value As System.Object

instance.CutDirection = value

value = instance.CutDirection
```

### C#

```csharp
System.object CutDirection {get; set;}
```

### C++/CLI

```cpp
property System.Object^ CutDirection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html), or [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) that defines the direction of the Normal Cut

## VBA Syntax

See [SMNormalCutFeatureData2::CutDirection](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData2~CutDirection.html).

## Examples

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html) example.

## See Also

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html)
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
