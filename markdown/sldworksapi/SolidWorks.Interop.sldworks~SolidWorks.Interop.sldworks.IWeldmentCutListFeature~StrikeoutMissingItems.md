---
title: "StrikeoutMissingItems Property (IWeldmentCutListFeature)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListFeature"
member: "StrikeoutMissingItems"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~StrikeoutMissingItems.html"
---

# StrikeoutMissingItems Property (IWeldmentCutListFeature)

Gets or sets whether to strike out missing items in the weldment cut list table.

## Syntax

### Visual Basic (Declaration)

```vb
Property StrikeoutMissingItems As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListFeature
Dim value As System.Boolean

instance.StrikeoutMissingItems = value

value = instance.StrikeoutMissingItems
```

### C#

```csharp
System.bool StrikeoutMissingItems {get; set;}
```

### C++/CLI

```cpp
property System.bool StrikeoutMissingItems {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to strike out missing items in the weldment cut list table, false to not

## VBA Syntax

See [WeldmentCutListFeature::StrikeoutMissingItems](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListFeature~StrikeoutMissingItems.html).

## Examples

See the [IWeldmentCutListFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html) examples.

## Remarks

Use [IWeldmentCutListFeature::KeepMissingItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListFeature~KeepMissingItems.html) to determine if missing cut list items are to be shown in the weldment cut list table.

## See Also

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.html)
[IWeldmentCutListFeature::KeepCurrentItemNumbers Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepCurrentItemNumbers.html)
[IWeldmentCutListFeature::SequenceStartNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~SequenceStartNumber.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
