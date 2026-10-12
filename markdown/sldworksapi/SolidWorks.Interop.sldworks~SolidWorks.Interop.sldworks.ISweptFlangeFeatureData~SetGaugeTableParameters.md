---
title: "SetGaugeTableParameters Method (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "SetGaugeTableParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~SetGaugeTableParameters.html"
---

# SetGaugeTableParameters Method (ISweptFlangeFeatureData)

Sets the gauge table parameters object.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetGaugeTableParameters( _
   ByVal DispIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim DispIn As System.Object

instance.SetGaugeTableParameters(DispIn)
```

### C#

```csharp
void SetGaugeTableParameters(
   System.object DispIn
)
```

### C++/CLI

```cpp
void SetGaugeTableParameters(
   System.Object^ DispIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DispIn`: [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)

## VBA Syntax

See [SweptFlangeFeatureData::SetGaugeTableParameters](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~SetGaugeTableParameters.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## Remarks

This method is valid only if [ISweptFlangeFeatureData::UseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseGaugeTable.html) is true.

Use [ISweptFlangeFeatureData::GetGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetGaugeTableParameters.html) to specify DispIn.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
