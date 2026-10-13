---
title: "GetUseGaugeTable Method (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "GetUseGaugeTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetUseGaugeTable.html"
---

# GetUseGaugeTable Method (ISheetMetalFeatureData)

Gets whether to use a sheet metal feature gauge table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseGaugeTable( _
   ByRef UseGaugeTable As System.Boolean, _
   ByRef GaugeTableFile As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim UseGaugeTable As System.Boolean
Dim GaugeTableFile As System.String
Dim value As System.Integer

value = instance.GetUseGaugeTable(UseGaugeTable, GaugeTableFile)
```

### C#

```csharp
System.int GetUseGaugeTable(
   out System.bool UseGaugeTable,
   out System.string GaugeTableFile
)
```

### C++/CLI

```cpp
System.int GetUseGaugeTable(
   [Out] System.bool UseGaugeTable,
   [Out] System.String^ GaugeTableFile
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseGaugeTable`: True to use a gauge table, false to not
- `GaugeTableFile`: Gauge table file name; valid only if UseGaugeTable is true

### Return Value

Result code as defined in [swSheetMetalModifierError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalModifierError_e.html)

## VBA Syntax

See [SheetMetalFeatureData::GetUseGaugeTable](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~GetUseGaugeTable.html).

## Examples

See [ISheetMetalFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData.html) examples.

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[ISheetMetalFeatureData::SetUseGaugeTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetUseGaugeTable.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
