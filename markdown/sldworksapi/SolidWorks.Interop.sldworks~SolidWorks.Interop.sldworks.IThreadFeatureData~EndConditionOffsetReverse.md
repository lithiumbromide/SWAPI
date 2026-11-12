---
title: "EndConditionOffsetReverse Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "EndConditionOffsetReverse"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffsetReverse.html"
---

# EndConditionOffsetReverse Property (IThreadFeatureData)

Gets or sets whether to flip the offset of the end condition to the opposite side of the end condition reference in this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndConditionOffsetReverse As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Boolean

instance.EndConditionOffsetReverse = value

value = instance.EndConditionOffsetReverse
```

### C#

```csharp
System.bool EndConditionOffsetReverse {get; set;}
```

### C++/CLI

```cpp
property System.bool EndConditionOffsetReverse {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the offset, false to not (default)

## VBA Syntax

See [ThreadFeatureData::EndConditionOffsetReverse](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~EndConditionOffsetReverse.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

This property is valid only if:

- [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.html) is set to [swThreadEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadEndCondition_e.html).swThreadEndCondition_UpToSelection.

- and -

- [IThreadFeatureData::EndConditionOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffset.html) is set to true.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
