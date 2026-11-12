---
title: "NormalCutParameters Property (ISMNormalCutFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData2"
member: "NormalCutParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~NormalCutParameters.html"
---

# NormalCutParameters Property (ISMNormalCutFeatureData2)

Gets or sets the Normal Cut parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Property NormalCutParameters As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData2
Dim value As System.Integer

instance.NormalCutParameters = value

value = instance.NormalCutParameters
```

### C#

```csharp
System.int NormalCutParameters {get; set;}
```

### C++/CLI

```cpp
property System.int NormalCutParameters {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Normal Cut parameters as defined in [swNormalCutParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutParameters_e.html)

## VBA Syntax

See [SMNormalCutFeatureData2::NormalCutParameters](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData2~NormalCutParameters.html).

## Examples

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html) example.

## See Also

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html)
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
