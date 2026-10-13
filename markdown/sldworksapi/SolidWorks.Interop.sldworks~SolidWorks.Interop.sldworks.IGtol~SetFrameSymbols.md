---
title: "SetFrameSymbols Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetFrameSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols.html"
---

# SetFrameSymbols Method (IGtol)

Obsolete. Superseded by [IGtol::SetFrameSymbols2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~SetFrameSymbols2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFrameSymbols( _
   ByVal FrameNumber As System.Short, _
   ByVal GCS As System.Short, _
   ByVal TolDia1 As System.Boolean, _
   ByVal TolMC1 As System.Short, _
   ByVal TolDia2 As System.Boolean, _
   ByVal TolMC2 As System.Short, _
   ByVal DatumMC1 As System.Short, _
   ByVal DatumMC2 As System.Short, _
   ByVal DatumMC3 As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNumber As System.Short
Dim GCS As System.Short
Dim TolDia1 As System.Boolean
Dim TolMC1 As System.Short
Dim TolDia2 As System.Boolean
Dim TolMC2 As System.Short
Dim DatumMC1 As System.Short
Dim DatumMC2 As System.Short
Dim DatumMC3 As System.Short

instance.SetFrameSymbols(FrameNumber, GCS, TolDia1, TolMC1, TolDia2, TolMC2, DatumMC1, DatumMC2, DatumMC3)
```

### C#

```csharp
void SetFrameSymbols(
   System.short FrameNumber,
   System.short GCS,
   System.bool TolDia1,
   System.short TolMC1,
   System.bool TolDia2,
   System.short TolMC2,
   System.short DatumMC1,
   System.short DatumMC2,
   System.short DatumMC3
)
```

### C++/CLI

```cpp
void SetFrameSymbols(
   System.short FrameNumber,
   System.short GCS,
   System.bool TolDia1,
   System.short TolMC1,
   System.bool TolDia2,
   System.short TolMC2,
   System.short DatumMC1,
   System.short DatumMC2,
   System.short DatumMC3
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNumber`:
- `GCS`:
- `TolDia1`:
- `TolMC1`:
- `TolDia2`:
- `TolMC2`:
- `DatumMC1`:
- `DatumMC2`:
- `DatumMC3`:

## VBA Syntax

See [Gtol::SetFrameSymbols](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetFrameSymbols.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
