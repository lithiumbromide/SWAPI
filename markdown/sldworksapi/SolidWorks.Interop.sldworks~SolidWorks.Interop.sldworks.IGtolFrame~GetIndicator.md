---
title: "GetIndicator Method (IGtolFrame)"
project: "SOLIDWORKS API Help"
interface: "IGtolFrame"
member: "GetIndicator"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetIndicator.html"
---

# GetIndicator Method (IGtolFrame)

Gets the indicator border type, tolerance type, and datum at the specified indicator index for this Gtol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIndicator( _
   ByVal IndicatorIndex As System.Integer, _
   ByRef BorderType As System.Integer, _
   ByRef TolType As System.Integer, _
   ByRef Datum As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtolFrame
Dim IndicatorIndex As System.Integer
Dim BorderType As System.Integer
Dim TolType As System.Integer
Dim Datum As System.String
Dim value As System.Boolean

value = instance.GetIndicator(IndicatorIndex, BorderType, TolType, Datum)
```

### C#

```csharp
System.bool GetIndicator(
   System.int IndicatorIndex,
   out System.int BorderType,
   out System.int TolType,
   out System.string Datum
)
```

### C++/CLI

```cpp
System.bool GetIndicator(
   System.int IndicatorIndex,
   [Out] System.int BorderType,
   [Out] System.int TolType,
   [Out] System.String^ Datum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IndicatorIndex`: One-based index of tolerance indicator to retrieve
- `BorderType`: Type of border as defined by [swGtolIndicatorBorderType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolIndicatorBorderType_e.html)
- `TolType`: Tolerance type as defined by [swGtolGeomCharSymbol_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolGeomCharSymbol_e.html) (see **Remarks**)
- `Datum`: Datum feature symbol that refers to the BorderType

### Return Value

True if indicator successfully retrieved, false if not

## VBA Syntax

See [GtolFrame::GetIndicator](ms-its:sldworksapivb6.chm::/sldworks~GtolFrame~GetIndicator.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

Before calling this method, use [IGtolFrame:GetIndicatorCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetIndicatorCount.html) to determine IndicatorIndex.

TolType may be one of only swGtolGeomCharSymbol_e.:

- swGcsANG
- swGcsPARALLEL
- swGcsPERP
- swGcsCIRCRUNOUT
- swGcsSYMMETRY

## See Also

[IGtolFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html)
[IGtolFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
