---
title: "AutoPropagation Property (ISMNormalCutFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData2"
member: "AutoPropagation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~AutoPropagation.html"
---

# AutoPropagation Property (ISMNormalCutFeatureData2)

Gets or sets whether to automatically add tangent faces to the cut-extrude face group.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoPropagation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData2
Dim value As System.Boolean

instance.AutoPropagation = value

value = instance.AutoPropagation
```

### C#

```csharp
System.bool AutoPropagation {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoPropagation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to add tangent faces, false to not

## VBA Syntax

See [SMNormalCutFeatureData2::AutoPropagation](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData2~AutoPropagation.html).

## Examples

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html) example.

## See Also

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html)
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
