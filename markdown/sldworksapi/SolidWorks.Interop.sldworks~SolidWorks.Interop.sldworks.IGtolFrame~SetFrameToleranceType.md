---
title: "SetFrameToleranceType Method (IGtolFrame)"
project: "SOLIDWORKS API Help"
interface: "IGtolFrame"
member: "SetFrameToleranceType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~SetFrameToleranceType.html"
---

# SetFrameToleranceType Method (IGtolFrame)

Sets the tolerance type for this Gtol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFrameToleranceType( _
   ByVal TolType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtolFrame
Dim TolType As System.Integer
Dim value As System.Boolean

value = instance.SetFrameToleranceType(TolType)
```

### C#

```csharp
System.bool SetFrameToleranceType(
   System.int TolType
)
```

### C++/CLI

```cpp
System.bool SetFrameToleranceType(
   System.int TolType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TolType`: Tolerance type as defined by [swGtolGeomCharSymbol_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolGeomCharSymbol_e.html) (see **Remarks**)

### Return Value

True if Gtol frame tolerance type successfully set, false if not

## VBA Syntax

See [GtolFrame::SetFrameToleranceType](ms-its:sldworksapivb6.chm::/sldworks~GtolFrame~SetFrameToleranceType.html).

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
