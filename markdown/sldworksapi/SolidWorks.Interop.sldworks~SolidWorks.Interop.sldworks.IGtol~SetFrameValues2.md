---
title: "SetFrameValues2 Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetFrameValues2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues2.html"
---

# SetFrameValues2 Method (IGtol)

Sets the geometric tolerance values and datum references in the specified frame of this GTol symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFrameValues2( _
   ByVal FrameNumber As System.Short, _
   ByVal Tol1 As System.String, _
   ByVal Tol2 As System.String, _
   ByVal Datum1 As System.String, _
   ByVal Datum2 As System.String, _
   ByVal Datum3 As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNumber As System.Short
Dim Tol1 As System.String
Dim Tol2 As System.String
Dim Datum1 As System.String
Dim Datum2 As System.String
Dim Datum3 As System.String
Dim value As System.Boolean

value = instance.SetFrameValues2(FrameNumber, Tol1, Tol2, Datum1, Datum2, Datum3)
```

### C#

```csharp
System.bool SetFrameValues2(
   System.short FrameNumber,
   System.string Tol1,
   System.string Tol2,
   System.string Datum1,
   System.string Datum2,
   System.string Datum3
)
```

### C++/CLI

```cpp
System.bool SetFrameValues2(
   System.short FrameNumber,
   System.String^ Tol1,
   System.String^ Tol2,
   System.String^ Datum1,
   System.String^ Datum2,
   System.String^ Datum3
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNumber`: Symbol frame number; 1 for first frame (see **Remarks**)
- `Tol1`: Tolerance 1 value
- `Tol2`: Tolerance 2 value
- `Datum1`: Primary datum with material conditions (**see Remarks**)
- `Datum2`: Secondary datum with material conditions (**see Remarks**)
- `Datum3`: Tertiary datum with material conditions (**see Remarks**)

### Return Value

True if frame values are set, false if not

## VBA Syntax

See [Gtol::SetFrameValues2](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetFrameValues2.html).

## Examples

[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)
[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)
[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)

## Remarks

This method is valid only if this Gtol was created in a version of SOLIDWORKS earlier than 2022.

Before calling this method, call:

- [IGtol::SetFrameSymbols2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.html) to specify the GTol symbol for this frame.
- [IGtol::GetFrameCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameCount.html) to specify FrameNumber.

Geometric tolerance and material condition symbols are defined in **C:\ProgramData\SolidWorks\SolidWorks** **20**`nn`**\lang\english\**gtol.sym. Inspect this file as you specify Datum1, Datum2, and Datum3 in <`LibraryName-SymbolName`> format.

For example, for datum tags A, B, and C:

```
   bRet = aGTol.SetFrameValues2(1, "0.2", "", "B-A-C<MOD-MMC>", "B<MOD-MMC>-C<MOD-LMC>", "C<MOD-MMC>-A")
```

sets the first symbol frame of this GTol with:

- Tolerance 1 = 0.2
- Primary datum = B-A-C<MOD-MMC>
- Secondary datum = B<MOD-MMC>-C<MOD-LMC>
- Teritiary datum = C<MOD-MMC>-A

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetFrameDiameterSymbols Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameDiameterSymbols.html)
[IGtol::GetFrameSymbols2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols2.html)
[IGtol::GetFrameValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameValues.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
