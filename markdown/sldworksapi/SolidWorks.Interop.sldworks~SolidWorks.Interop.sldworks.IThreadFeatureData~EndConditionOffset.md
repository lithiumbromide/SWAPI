---
title: "EndConditionOffset Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "EndConditionOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffset.html"
---

# EndConditionOffset Property (IThreadFeatureData)

Gets or sets whether to offset the end condition of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndConditionOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Boolean

instance.EndConditionOffset = value

value = instance.EndConditionOffset
```

### C#

```csharp
System.bool EndConditionOffset {get; set;}
```

### C++/CLI

```cpp
property System.bool EndConditionOffset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to offset the end condition, false to not (default)

## VBA Syntax

See [ThreadFeatureData::EndConditionOffset](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~EndConditionOffset.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

This property is valid only if [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.html) is set to [swThreadEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadEndCondition_e.html).swThreadEndCondition_UpToSelection.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)
[IThreadFeatureData::EndConditionOffsetDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffsetDistance.html)
[IThreadFeatureData::EndConditionOffsetReverse Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffsetReverse.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
