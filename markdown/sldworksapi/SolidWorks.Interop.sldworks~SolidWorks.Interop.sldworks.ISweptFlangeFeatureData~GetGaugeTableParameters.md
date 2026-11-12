---
title: "GetGaugeTableParameters Method (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "GetGaugeTableParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetGaugeTableParameters.html"
---

# GetGaugeTableParameters Method (ISweptFlangeFeatureData)

Gets the gauge table parameters object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGaugeTableParameters() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Object

value = instance.GetGaugeTableParameters()
```

### C#

```csharp
System.object GetGaugeTableParameters()
```

### C++/CLI

```cpp
System.Object^ GetGaugeTableParameters();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)

## VBA Syntax

See [SweptFlangeFeatureData::GetGaugeTableParameters](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~GetGaugeTableParameters.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## Remarks

This method is valid only if [ISweptFlangeFeatureData::UseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseGaugeTable.html) is true.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)
[ISweptFlangeFeatureData::SetGaugeTableParameters Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~SetGaugeTableParameters.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
