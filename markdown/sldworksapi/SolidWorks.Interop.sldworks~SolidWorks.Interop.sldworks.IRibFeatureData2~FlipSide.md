---
title: "FlipSide Property (IRibFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2"
member: "FlipSide"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~FlipSide.html"
---

# FlipSide Property (IRibFeatureData2)

Gets or sets whether material is added to the reverse side of the rib.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipSide As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData2
Dim value As System.Boolean

instance.FlipSide = value

value = instance.FlipSide
```

### C#

```csharp
System.bool FlipSide {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipSide {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the material is added to the reverse side of the rib, false if not

## VBA Syntax

See [RibFeatureData2::FlipSide](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData2~FlipSide.html).

## Examples

See the [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html) examples.

## Remarks

Changing the value of this property does not affect geometry until [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) is called.

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
