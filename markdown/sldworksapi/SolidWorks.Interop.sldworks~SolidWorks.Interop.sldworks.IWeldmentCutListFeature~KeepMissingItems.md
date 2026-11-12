---
title: "KeepMissingItems Property (IWeldmentCutListFeature)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListFeature"
member: "KeepMissingItems"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepMissingItems.html"
---

# KeepMissingItems Property (IWeldmentCutListFeature)

Gets or sets whether to continue to show cut list items that were deleted from the weldment in the weldment cut list table.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepMissingItems As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListFeature
Dim value As System.Boolean

instance.KeepMissingItems = value

value = instance.KeepMissingItems
```

### C#

```csharp
System.bool KeepMissingItems {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepMissingItems {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to keep missing cut list items, false to not

## VBA Syntax

See [WeldmentCutListFeature::KeepMissingItems](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListFeature~KeepMissingItems.html).

## Remarks

Use [IWeldmentCutListFeature::StrikeoutMissingItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListFeature~StrikeoutMissingItems.html) to determine if deleted items are to be shown with strikeout formatting in the weldment cut list table.

## See Also

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.html)
[IWeldmentCutListFeature::KeepCurrentItemNumbers Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepCurrentItemNumbers.html)
[IWeldmentCutListFeature::SequenceStartNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~SequenceStartNumber.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
