---
title: "IsTwoSided Property (IRibFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2"
member: "IsTwoSided"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~IsTwoSided.html"
---

# IsTwoSided Property (IRibFeatureData2)

Gets or sets whether the rib is created on two sides of the midplane or in a single direction (see [IRibFeatureData2::ReverseThicknessDir](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRibFeatureData2~ReverseThicknessDir.html)).

## Syntax

### Visual Basic (Declaration)

```vb
Property IsTwoSided As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData2
Dim value As System.Boolean

instance.IsTwoSided = value

value = instance.IsTwoSided
```

### C#

```csharp
System.bool IsTwoSided {get; set;}
```

### C++/CLI

```cpp
property System.bool IsTwoSided {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the rib is extruded either side of the midplane, false if it is single-sided

## VBA Syntax

See [RibFeatureData2::IsTwoSided](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData2~IsTwoSided.html).

## Examples

See the [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html) examples.

## Remarks

Changing the value of this property does not affect geometry until [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) is called.

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
