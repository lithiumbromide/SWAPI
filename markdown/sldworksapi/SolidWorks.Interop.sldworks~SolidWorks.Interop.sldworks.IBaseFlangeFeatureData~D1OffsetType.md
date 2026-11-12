---
title: "D1OffsetType Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "D1OffsetType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1OffsetType.html"
---

# D1OffsetType Property (IBaseFlangeFeatureData)

Obsolete. Superseded by [IBaseFlangeFeatureData::D1EndConditionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1EndConditionType.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property D1OffsetType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Integer

instance.D1OffsetType = value

value = instance.D1OffsetType
```

### C#

```csharp
System.int D1OffsetType {get; set;}
```

### C++/CLI

```cpp
property System.int D1OffsetType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset type as defined in [swFlangeOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html)

## VBA Syntax

See [BaseFlangeFeatureData::D1OffsetType](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~D1OffsetType.html).

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::D2OffsetType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D2OffsetType.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
