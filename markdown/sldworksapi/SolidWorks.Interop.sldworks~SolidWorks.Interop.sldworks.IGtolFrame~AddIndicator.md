---
title: "AddIndicator Method (IGtolFrame)"
project: "SOLIDWORKS API Help"
interface: "IGtolFrame"
member: "AddIndicator"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~AddIndicator.html"
---

# AddIndicator Method (IGtolFrame)

Adds a tolerance indicator to the end of the list of indicators to the right of this Gtol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddIndicator( _
   ByVal BorderType As System.Integer, _
   ByVal TolType As System.Integer, _
   ByVal Datum As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtolFrame
Dim BorderType As System.Integer
Dim TolType As System.Integer
Dim Datum As System.String
Dim value As System.Boolean

value = instance.AddIndicator(BorderType, TolType, Datum)
```

### C#

```csharp
System.bool AddIndicator(
   System.int BorderType,
   System.int TolType,
   System.string Datum
)
```

### C++/CLI

```cpp
System.bool AddIndicator(
   System.int BorderType,
   System.int TolType,
   System.String^ Datum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BorderType`: Type of border as defined by [swGtolIndicatorBorderType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolIndicatorBorderType_e.html)
- `TolType`: Tolerance type as defined by [swGtolGeomCharSymbol_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolGeomCharSymbol_e.html) (see **Remarks**)
- `Datum`: Datum feature symbol that refers to the BorderType

### Return Value

True if tolerance indicator successfully added, false if not

## VBA Syntax

See [GtolFrame::AddIndicator](ms-its:sldworksapivb6.chm::/sldworks~GtolFrame~AddIndicator.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

Tolerance indicators:

- define a tolerance zone within which a Gtol value applies.
- are shown to the right of the main frame, but to the left of any text box for the first frame.

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
