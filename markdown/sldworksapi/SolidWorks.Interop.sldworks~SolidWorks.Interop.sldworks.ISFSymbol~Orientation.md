---
title: "Orientation Property (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "Orientation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~Orientation.html"
---

# Orientation Property (ISFSymbol)

Gets whether the orientation of this surface finish symbol is relative to the model or entity to which it is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Property Orientation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Integer

instance.Orientation = value

value = instance.Orientation
```

### C#

```csharp
System.int Orientation {get; set;}
```

### C++/CLI

```cpp
property System.int Orientation {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Orientation as defined in [swSurfaceFinishSymbolOrientation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSurfaceFinishSymbolOrientation_e.html)

## VBA Syntax

See [SFSymbol::Orientation](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~Orientation.html).

## Remarks

If setting the value to swSFOrientation_UserDefined, then the angle at which the symbol is displayed does not change. Instead, use [ISFSymbol::SetAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~SetAngle.html) to set the symbol to a user-specified angle, which automatically sets the orientation to swSFOrientation_UserDefined.

Use [ISFSymbol::GetAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetAngle.html) to get the angle of the symbol.

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
