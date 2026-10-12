---
title: "GetTargetAreaSize Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "GetTargetAreaSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTargetAreaSize.html"
---

# GetTargetAreaSize Method (IDatumTargetSym)

Gets the size of the datum target symbol area.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTargetAreaSize( _
   ByVal WhichOne As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim WhichOne As System.Integer
Dim value As System.String

value = instance.GetTargetAreaSize(WhichOne)
```

### C#

```csharp
System.string GetTargetAreaSize(
   System.int WhichOne
)
```

### C++/CLI

```cpp
System.String^ GetTargetAreaSize(
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: 0-based index indicating which size value to get (see [Remarks](#Remarks))

### Return Value

Target area size (see Remarks)

## VBA Syntax

See [DatumTargetSym::GetTargetAreaSize](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~GetTargetAreaSize.html).

## Remarks

Use [IDatumTargetSym::GetTargetShape](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~GetTargetShape.html) to get the style for the target area.

| If the target area style for this symbol is a ... | Then... |
| --- | --- |
| Point | There is one size value, which might be empty. Retrieve the text using an index value of 0. SOLIDWORKS displays the text in the upper half of the symbol, preceded by a diameter character. |
| Circle | There is one size value. Retrieve the text using an index value of 0. SOLIDWORKS displays the text in the upper half of the symbol, preceded by a diameter character. |
| Rectangle | There are two size values. Retrieve the text using an index value of 0 and 1. SOLIDWORKS displays the texts in the upper half of the symbol, separated by an x character. |

Use [IDatumTargetSym::SetTargetArea](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~SetTargetArea.html) to set the target area size.

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::GetDisplayTargetArea Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplayTargetArea.html)
[IDatumTargetSym::SetTargetArea Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetTargetArea.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
