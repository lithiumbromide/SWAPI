---
title: "GetTargetShape Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "GetTargetShape"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTargetShape.html"
---

# GetTargetShape Method (IDatumTargetSym)

Gets the shape or style of the datum target area.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTargetShape() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim value As System.Integer

value = instance.GetTargetShape()
```

### C#

```csharp
System.int GetTargetShape()
```

### C++/CLI

```cpp
System.int GetTargetShape();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Target area shape or style as defined in [swDatumTargetAreaShape_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumTargetAreaShape_e.html)

## VBA Syntax

See [DatumTargetSym::GetTargetShape](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~GetTargetShape.html).

## Remarks

Use [IDatumTargetSym::SetTargetArea](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~SetTargetArea.html) to set the shape of the target area.

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::GetDisplayTargetArea Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplayTargetArea.html)
[IDatumTargetSym::GetTargetAreaSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTargetAreaSize.html)
[IDatumTargetSym::SetTargetArea Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetTargetArea.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
