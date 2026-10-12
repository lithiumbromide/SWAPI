---
title: "EnableDraft Property (IRibFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2"
member: "EnableDraft"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~EnableDraft.html"
---

# EnableDraft Property (IRibFeatureData2)

Gets or sets whether the rib has an associated draft.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableDraft As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData2
Dim value As System.Boolean

instance.EnableDraft = value

value = instance.EnableDraft
```

### C#

```csharp
System.bool EnableDraft {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableDraft {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the rib has a draft, false if not

## VBA Syntax

See [RibFeatureData2::EnableDraft](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData2~EnableDraft.html).

## Examples

See the [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html) examples.

## Remarks

Changing the value of this property does not affect geometry until [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) is called.

Use [IRibFeatureData2::DraftOutward](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRibFeatureData2~DraftOutward.html) and [IRibFeatureData2::DraftAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRibFeatureData2~DraftAngle.html) for additional draft control.

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html)
[IRibFeatureData2::RefSketchIndex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~RefSketchIndex.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
