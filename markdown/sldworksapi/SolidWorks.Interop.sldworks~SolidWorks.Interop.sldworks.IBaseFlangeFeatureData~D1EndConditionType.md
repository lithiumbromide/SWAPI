---
title: "D1EndConditionType Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "D1EndConditionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1EndConditionType.html"
---

# D1EndConditionType Property (IBaseFlangeFeatureData)

Gets or sets the Direction 1 end condition type for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1EndConditionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Integer

instance.D1EndConditionType = value

value = instance.D1EndConditionType
```

### C#

```csharp
System.int D1EndConditionType {get; set;}
```

### C++/CLI

```cpp
property System.int D1EndConditionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End condition type as defined in [swFlangeOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html)

## VBA Syntax

See [BaseFlangeFeatureData::D1EndConditionType](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~D1EndConditionType.html).

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
