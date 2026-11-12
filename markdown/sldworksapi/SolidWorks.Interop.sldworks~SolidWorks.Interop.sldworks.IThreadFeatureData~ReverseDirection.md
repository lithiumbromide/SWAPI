---
title: "ReverseDirection Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ReverseDirection.html"
---

# ReverseDirection Property (IThreadFeatureData)

Gets or sets whether to reverse the direction of the Blind or Revolutions end condition of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Boolean

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.bool ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of the Blind or Revolutions end condition, false to not (default)

## VBA Syntax

See [ThreadFeatureData::ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~ReverseDirection.html).

## Remarks

This property is valid only if [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.html) is set to [swThreadEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadEndCondition_e.html):

- swThreadEndCondition_Blind

- or -

- swThreadEndCondition_Revolutions.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
