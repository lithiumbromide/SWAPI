---
title: "GetDisplaySymbol Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "GetDisplaySymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplaySymbol.html"
---

# GetDisplaySymbol Method (IDatumTargetSym)

Gets whether the datum target symbol is displayed.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplaySymbol() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim value As System.Boolean

value = instance.GetDisplaySymbol()
```

### C#

```csharp
System.bool GetDisplaySymbol()
```

### C++/CLI

```cpp
System.bool GetDisplaySymbol();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the datum target symbol is displayed, false if it is not

## VBA Syntax

See [DatumTargetSym::GetDisplaySymbol](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~GetDisplaySymbol.html).

## Remarks

Use:

- [IDatumTargetSym::GetDisplayTargetArea](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~GetDisplayTargetArea.html) to determine whether the datum target area part of this annotation is displayed.
- [IDatumTargetSym::SetDisplay](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~SetDisplay.html) to enable or disable the display of the target area or symbol.

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::GetDisplaySizeOutside Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplaySizeOutside.html)
[IDatumTargetSym::GetDisplaySizeOutside Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplaySizeOutside.html)
[IDatumTargetSym::SetDisplay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDisplay.html)
[IDatumTargetSym::SetDisplay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDisplay.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
