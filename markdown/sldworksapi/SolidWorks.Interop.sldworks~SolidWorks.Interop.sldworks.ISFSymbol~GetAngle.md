---
title: "GetAngle Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetAngle.html"
---

# GetAngle Method (ISFSymbol)

Gets the angle of this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAngle() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Double

value = instance.GetAngle()
```

### C#

```csharp
System.double GetAngle()
```

### C++/CLI

```cpp
System.double GetAngle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Symbol angle

## VBA Syntax

See [SFSymbol::GetAngle](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetAngle.html).

## Remarks

See [ISFSymbol::Orientation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~Orientation.html) and [ISFSymbol::SetAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~SetAngle.html) for details on how to set the angle of a surface finish symbol.

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
