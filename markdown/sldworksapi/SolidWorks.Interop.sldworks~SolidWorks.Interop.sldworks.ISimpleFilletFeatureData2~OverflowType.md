---
title: "OverflowType Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "OverflowType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~OverflowType.html"
---

# OverflowType Property (ISimpleFilletFeatureData2)

Gets or sets the overflow type of the simple fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverflowType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer

instance.OverflowType = value

value = instance.OverflowType
```

### C#

```csharp
System.int OverflowType {get; set;}
```

### C++/CLI

```cpp
property System.int OverflowType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Overflow type as defined in [swFilletOverFlowType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFilletOverFlowType_e.html)

## VBA Syntax

See [SimpleFilletFeatureData2::OverflowType](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~OverflowType.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
