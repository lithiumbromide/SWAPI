---
title: "UseGaugeTable Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "UseGaugeTable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseGaugeTable.html"
---

# UseGaugeTable Property (ISweptFlangeFeatureData)

Gets or sets whether to use an Excel gauge table for this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseGaugeTable As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean

instance.UseGaugeTable = value

value = instance.UseGaugeTable
```

### C#

```csharp
System.bool UseGaugeTable {get; set;}
```

### C++/CLI

```cpp
property System.bool UseGaugeTable {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use an Excel gauge table, false to not

## VBA Syntax

See [SweptFlangeFeatureData::UseGaugeTable](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~UseGaugeTable.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## Remarks

This property is valid only:

- if [ISweptFlangeFeatureData::UseMaterialSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseMaterialSheetMetalParameters.html) is false,

- and -

- when not creating the swept flange on an existing sheet metal feature.

If this property is true, then use [ISweptFlangeFeatureData::GetGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetGaugeTableParameters.html) and [ISweptFlangeFeatureData::SetGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~SetGaugeTableParameters.html) to get and set the gauge table.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
