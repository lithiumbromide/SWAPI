---
title: "TangentPropagation Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "TangentPropagation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~TangentPropagation.html"
---

# TangentPropagation Property (ICosmeticWeldBeadFeatureData)

Gets or sets whether to apply the weld bead to all edges that are tangent to the selected faces or edges.

## Syntax

### Visual Basic (Declaration)

```vb
Property TangentPropagation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Boolean

instance.TangentPropagation = value

value = instance.TangentPropagation
```

### C#

```csharp
System.bool TangentPropagation {get; set;}
```

### C++/CLI

```cpp
property System.bool TangentPropagation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to apply the weld bead to all edges that are tangent to the selected faces or edges, false to not (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::TangentPropagation](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~TangentPropagation.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## Remarks

| If this property is... | Then use... |
| --- | --- |
| True | ICosmeticWeldBeadFeatureData::FromToLength to enable the from/to length properties |
| False | ICosmeticWeldBeadFeatureData::Side to define how to apply the weld bead to the selected faces or edges |

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
