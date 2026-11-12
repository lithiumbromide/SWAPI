---
title: "TableKFactor Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "TableKFactor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableKFactor.html"
---

# TableKFactor Property (IBaseFlangeFeatureData)

Gets the K-factor to use, if it is not [overridden](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBaseFlangeFeatureData~OverrideKFactor.html), from the gauge table for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TableKFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Double

value = instance.TableKFactor
```

### C#

```csharp
System.double TableKFactor {get;}
```

### C++/CLI

```cpp
property System.double TableKFactor {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

K-factor value

## VBA Syntax

See [BaseFlangeFeatureData::TableKFactor](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~TableKFactor.html).

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::GaugeTablePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.html)
[IBaseFlangeFeatureData::KFactor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~KFactor.html)
[IBaseFlangeFeatureData::UseGaugeTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
