---
title: "SetDisplay Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "SetDisplay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDisplay.html"
---

# SetDisplay Method (IDatumTargetSym)

Sets the display characteristics of the datum target symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDisplay( _
   ByVal Symbol As System.Boolean, _
   ByVal TargetArea As System.Boolean, _
   ByVal SizeOutside As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim Symbol As System.Boolean
Dim TargetArea As System.Boolean
Dim SizeOutside As System.Boolean
Dim value As System.Boolean

value = instance.SetDisplay(Symbol, TargetArea, SizeOutside)
```

### C#

```csharp
System.bool SetDisplay(
   System.bool Symbol,
   System.bool TargetArea,
   System.bool SizeOutside
)
```

### C++/CLI

```cpp
System.bool SetDisplay(
   System.bool Symbol,
   System.bool TargetArea,
   System.bool SizeOutside
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Symbol`: True displays the datum target symbol part of the annotation, false hides it
- `TargetArea`: True displays the datum target area part of the annotation, false hides it
- `SizeOutside`: True displays the datum target area size outside of the symbol, false displays it
  inside

### Return Value

True if the display characteristics were set successfully, false if not

## VBA Syntax

See [DatumTargetSym::SetDisplay](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~SetDisplay.html).

## Remarks

Use:

- [IDatumTargetSym::GetDisplaySymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~GetDisplaySymbol.html) to determine if the datum target symbol part of the annotation is displayed.
- [IDatumTargetSym::GetDisplayTargetArea](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~GetDisplayTargetArea.html) to determine if the datum target area part of the annotation is displayed.
- [IDatumTargetSym::GetDisplaySizeOutside](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~GetDisplaySizeOutside.html) to determine whether the target area size is displayed inside or outside of the symbol.

To see the model or drawing changes caused by running this method, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw your window.

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
