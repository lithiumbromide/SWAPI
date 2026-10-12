---
title: "ProfileDirection Property (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "ProfileDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~ProfileDirection.html"
---

# ProfileDirection Property (ISFSymbol)

Gets or sets the profile direction of this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Integer

instance.ProfileDirection = value

value = instance.ProfileDirection
```

### C#

```csharp
System.int ProfileDirection {get; set;}
```

### C++/CLI

```cpp
property System.int ProfileDirection {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Profile direction as defined by [swSFProfileDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSFProfileDirection_e.html)

## VBA Syntax

See [SFSymbol::ProfileDirection](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~ProfileDirection.html).

## Remarks

If this property sets swSFProfileDirection_e.swSFProfileDirectionDefinedAngle, then use [ISFSymbol::ProfileAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~ProfileAngle.html) to specify the angle.

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
