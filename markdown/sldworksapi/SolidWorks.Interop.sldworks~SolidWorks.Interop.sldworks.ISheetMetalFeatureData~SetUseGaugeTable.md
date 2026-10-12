---
title: "SetUseGaugeTable Method (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "SetUseGaugeTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetUseGaugeTable.html"
---

# SetUseGaugeTable Method (ISheetMetalFeatureData)

Sets whether to use a sheet metal feature gauge table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUseGaugeTable( _
   ByVal UseGaugeTable As System.Boolean, _
   ByVal GaugeTableFile As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim UseGaugeTable As System.Boolean
Dim GaugeTableFile As System.String
Dim value As System.Integer

value = instance.SetUseGaugeTable(UseGaugeTable, GaugeTableFile)
```

### C#

```csharp
System.int SetUseGaugeTable(
   System.bool UseGaugeTable,
   System.string GaugeTableFile
)
```

### C++/CLI

```cpp
System.int SetUseGaugeTable(
   System.bool UseGaugeTable,
   System.String^ GaugeTableFile
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseGaugeTable`: True to use a gauge table, false to not
- `GaugeTableFile`: Gauge table file name; valid only if UseGaugeTable is true

### Return Value

Result code as defined in [swSheetMetalModifierError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalModifierError_e.html)

## VBA Syntax

See [SheetMetalFeatureData::SetUseGaugeTable](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~SetUseGaugeTable.html).

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[ISheetMetalFeatureData::GetUseGaugeTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetUseGaugeTable.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
