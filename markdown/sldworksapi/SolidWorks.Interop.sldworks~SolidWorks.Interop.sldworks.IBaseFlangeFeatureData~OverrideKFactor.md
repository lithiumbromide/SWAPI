---
title: "OverrideKFactor Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "OverrideKFactor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideKFactor.html"
---

# OverrideKFactor Property (IBaseFlangeFeatureData)

Gets or sets whether to override the K-factor value specified in the gauge table for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideKFactor As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

instance.OverrideKFactor = value

value = instance.OverrideKFactor
```

### C#

```csharp
System.bool OverrideKFactor {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideKFactor {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the K-factor value, false to not

## VBA Syntax

See [BaseFlangeFeatureData::OverrideKFactor](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~OverrideKFactor.html).

## Examples

[Create Base-Flange Feature Using Gauge Table (VBA)](Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm)

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::KFactor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~KFactor.html)
[IBaseFlangeFeatureData::TableKFactor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableKFactor.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
