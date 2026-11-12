---
title: "GetDisplaySizeOutside Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "GetDisplaySizeOutside"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplaySizeOutside.html"
---

# GetDisplaySizeOutside Method (IDatumTargetSym)

Gets whether the datum target area size is displayed inside or outside of the symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplaySizeOutside() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim value As System.Boolean

value = instance.GetDisplaySizeOutside()
```

### C#

```csharp
System.bool GetDisplaySizeOutside()
```

### C++/CLI

```cpp
System.bool GetDisplaySizeOutside();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the datum target area size is displayed outside of the symbol, false if the datum target area size is displayed inside of the symbol

## VBA Syntax

See [DatumTargetSym::GetDisplaySizeOutside](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~GetDisplaySizeOutside.html).

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::SetDisplay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDisplay.html)
[IDatumTargetSym::GetDisplaySymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplaySymbol.html)
[IDatumTargetSym::GetDisplayTargetArea Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplayTargetArea.html)
[IDatumTargetSym::SetDisplay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDisplay.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
