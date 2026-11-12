---
title: "D2EndConditionType Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "D2EndConditionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D2EndConditionType.html"
---

# D2EndConditionType Property (IBaseFlangeFeatureData)

Gets or sets the Direction 2 end condition type for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2EndConditionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Integer

instance.D2EndConditionType = value

value = instance.D2EndConditionType
```

### C#

```csharp
System.int D2EndConditionType {get; set;}
```

### C++/CLI

```cpp
property System.int D2EndConditionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End condition type as defined in [swFlangeOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html)

## VBA Syntax

See [BaseFlangeFeatureData::D2EndConditionType](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~D2EndConditionType.html).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
