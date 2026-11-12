---
title: "DraftAngle Property (IRibFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2"
member: "DraftAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftAngle.html"
---

# DraftAngle Property (IRibFeatureData2)

Gets or sets the draft angle for the rib.

## Syntax

### Visual Basic (Declaration)

```vb
Property DraftAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData2
Dim value As System.Double

instance.DraftAngle = value

value = instance.DraftAngle
```

### C#

```csharp
System.double DraftAngle {get; set;}
```

### C++/CLI

```cpp
property System.double DraftAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle for the draft

## VBA Syntax

See [RibFeatureData2::DraftAngle](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData2~DraftAngle.html).

## Examples

See the [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html) examples.

## Remarks

Changing the value of this property does not affect geometry until [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) is called.

This property is valid only when [IRibFeatureData2::EnableDraft](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRibFeatureData2~EnableDraft.html) is set to true.

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html)
[IRibFeatureData2::RefSketchIndex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~RefSketchIndex.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
