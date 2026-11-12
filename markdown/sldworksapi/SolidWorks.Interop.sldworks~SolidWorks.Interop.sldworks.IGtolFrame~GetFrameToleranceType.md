---
title: "GetFrameToleranceType Method (IGtolFrame)"
project: "SOLIDWORKS API Help"
interface: "IGtolFrame"
member: "GetFrameToleranceType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetFrameToleranceType.html"
---

# GetFrameToleranceType Method (IGtolFrame)

Gets the tolerance type of this Gtol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFrameToleranceType( _
   ByRef TolType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtolFrame
Dim TolType As System.Integer
Dim value As System.Boolean

value = instance.GetFrameToleranceType(TolType)
```

### C#

```csharp
System.bool GetFrameToleranceType(
   out System.int TolType
)
```

### C++/CLI

```cpp
System.bool GetFrameToleranceType(
   [Out] System.int TolType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TolType`: Tolerance type as defined by [swGtolGeomCharSymbol_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolGeomCharSymbol_e.html) (see **Remarks**)

### Return Value

True if Gtol frame tolerance type successfully retrieved, false if not

## VBA Syntax

See [GtolFrame::GetFrameToleranceType](ms-its:sldworksapivb6.chm::/sldworks~GtolFrame~GetFrameToleranceType.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

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
