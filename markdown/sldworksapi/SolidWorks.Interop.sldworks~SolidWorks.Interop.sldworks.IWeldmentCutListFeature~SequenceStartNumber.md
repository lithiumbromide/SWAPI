---
title: "SequenceStartNumber Property (IWeldmentCutListFeature)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListFeature"
member: "SequenceStartNumber"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~SequenceStartNumber.html"
---

# SequenceStartNumber Property (IWeldmentCutListFeature)

Gets or sets the starting sequence number for this weldment cut list table.

## Syntax

### Visual Basic (Declaration)

```vb
Property SequenceStartNumber As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListFeature
Dim value As System.Integer

instance.SequenceStartNumber = value

value = instance.SequenceStartNumber
```

### C#

```csharp
System.int SequenceStartNumber {get; set;}
```

### C++/CLI

```cpp
property System.int SequenceStartNumber {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Starting sequence number for this weldment cut list table

## VBA Syntax

See [WeldmentCutListFeature::SequenceStartNumber](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListFeature~SequenceStartNumber.html).

## Examples

See the [IWeldmentCutListFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html) examples.

## See Also

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.html)
[IWeldmentCutListFeature::KeepCurrentItemNumbers Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepCurrentItemNumbers.html)
[IWeldmentCutListFeature::KeepMissingItems Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepMissingItems.html)
[IWeldmentCutListFeature::StrikeoutMissingItems Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~StrikeoutMissingItems.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
