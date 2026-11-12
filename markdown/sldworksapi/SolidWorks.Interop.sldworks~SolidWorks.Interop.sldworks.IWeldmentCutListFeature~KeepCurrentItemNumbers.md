---
title: "KeepCurrentItemNumbers Property (IWeldmentCutListFeature)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListFeature"
member: "KeepCurrentItemNumbers"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepCurrentItemNumbers.html"
---

# KeepCurrentItemNumbers Property (IWeldmentCutListFeature)

Gets or sets whether item numbers are kept with their rows when columns are sorted or reordered in this weldment cut list table.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepCurrentItemNumbers As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListFeature
Dim value As System.Boolean

instance.KeepCurrentItemNumbers = value

value = instance.KeepCurrentItemNumbers
```

### C#

```csharp
System.bool KeepCurrentItemNumbers {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepCurrentItemNumbers {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to keep item numbers with their rows when columns are sorted or reordered, false to not

## VBA Syntax

See [WeldmentCutListFeature::KeepCurrentItemNumbers](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListFeature~KeepCurrentItemNumbers.html).

## Examples

See the [IWeldmentCutListFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html) examples.

## See Also

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.html)
[IWeldmentCutListFeature::KeepMissingItems Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepMissingItems.html)
[IWeldmentCutListFeature::SequenceStartNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~SequenceStartNumber.html)
[IWeldmentCutListFeature::StrikeoutMissingItems Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~StrikeoutMissingItems.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
