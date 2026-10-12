---
title: "SetBetweenTwoPoints Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetBetweenTwoPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBetweenTwoPoints.html"
---

# SetBetweenTwoPoints Method (IGtol)

Enables or disables the between two points symbol and its texts.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetBetweenTwoPoints( _
   ByVal Between As System.Boolean, _
   ByVal TextFrom As System.String, _
   ByVal TextTo As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Between As System.Boolean
Dim TextFrom As System.String
Dim TextTo As System.String

instance.SetBetweenTwoPoints(Between, TextFrom, TextTo)
```

### C#

```csharp
void SetBetweenTwoPoints(
   System.bool Between,
   System.string TextFrom,
   System.string TextTo
)
```

### C++/CLI

```cpp
void SetBetweenTwoPoints(
   System.bool Between,
   System.String^ TextFrom,
   System.String^ TextTo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Between`: True to enable the between two points symbol, or false to disable it
- `TextFrom`: Text on the left end of the symbol
- `TextTo`: Text on the right end of the symbol

## VBA Syntax

See [Gtol::SetBetweenTwoPoints](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetBetweenTwoPoints.html).

## Examples

[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)
[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)
[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)

## Remarks

The TextFrom and TextTo values might be set to empty strings.

This method ignores TextFrom and TextTo if the between value is false (the symbol is being disabled).

Use:

- [IGtol::GetBetweenTwoPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetBetweenTwoPoints.html) to determine if this symbol is currently in use
- [IGtol::GetBetweenTwoPointsText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetBetweenTwoPointsText.html) to determine the texts that are part of this symbol

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
