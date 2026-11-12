---
title: "ProfileAngle Property (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "ProfileAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~ProfileAngle.html"
---

# ProfileAngle Property (ISFSymbol)

Gets or sets the profile angle of this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Double

instance.ProfileAngle = value

value = instance.ProfileAngle
```

### C#

```csharp
System.double ProfileAngle {get; set;}
```

### C++/CLI

```cpp
property System.double ProfileAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Profile angle

## VBA Syntax

See [SFSymbol::ProfileAngle](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~ProfileAngle.html).

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
