---
title: "GetBetweenTwoPointsText Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetBetweenTwoPointsText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPointsText.html"
---

# GetBetweenTwoPointsText Method (IGtol)

Gets the text used in the between two points symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBetweenTwoPointsText( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Index As System.Integer
Dim value As System.String

value = instance.GetBetweenTwoPointsText(Index)
```

### C#

```csharp
System.string GetBetweenTwoPointsText(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetBetweenTwoPointsText(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0 for the text on the left end of the symbol, 1 for the text on the right end of the symbol

### Return Value

Symbol text

## VBA Syntax

See [Gtol::GetBetweenTwoPointsText](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetBetweenTwoPointsText.html).

## Remarks

This method returns the requested text whether the between two points symbol is currently enabled. Use [IGtol::GetBetweenTwoPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetBetweenTwoPoints.html) to determine if this symbol is enabled.

Use [IGtol::SetBetweenTwoPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~SetBetweenTwoPoints.html) to enable this symbol and its texts.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::SetBetweenTwoPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBetweenTwoPoints.html)
[IGtol::GetBetweenTwoPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPoints.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
