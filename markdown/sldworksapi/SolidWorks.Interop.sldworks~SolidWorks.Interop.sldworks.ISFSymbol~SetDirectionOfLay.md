---
title: "SetDirectionOfLay Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "SetDirectionOfLay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetDirectionOfLay.html"
---

# SetDirectionOfLay Method (ISFSymbol)

Sets the direction of lay value for this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDirectionOfLay( _
   ByVal Direction As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim Direction As System.Integer
Dim value As System.Boolean

value = instance.SetDirectionOfLay(Direction)
```

### C#

```csharp
System.bool SetDirectionOfLay(
   System.int Direction
)
```

### C++/CLI

```cpp
System.bool SetDirectionOfLay(
   System.int Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction of lay value as defined in [swSFLaySym_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFLaySym_e.html)

### Return Value

True if the direction of lay value is set, false if not

## VBA Syntax

See [SFSymbol::SetDirectionOfLay](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~SetDirectionOfLay.html).

## Remarks

If an invalid direction of lay value is specified, the symbol is not changed, and false is returned.

To see the model or drawing changes caused by running this method, you must redraw your window. See [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) for details.

To get the direction of lay value, use [ISFSymbol::GetDirectionOfLay](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetDirectionOfLay.html).

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
