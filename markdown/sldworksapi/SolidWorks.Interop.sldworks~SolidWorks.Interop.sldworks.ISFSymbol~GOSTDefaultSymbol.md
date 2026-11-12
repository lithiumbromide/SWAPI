---
title: "GOSTDefaultSymbol Property (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GOSTDefaultSymbol"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GOSTDefaultSymbol.html"
---

# GOSTDefaultSymbol Property (ISFSymbol)

Gets whether the GOST Add default symbol option is set.

## Syntax

### Visual Basic (Declaration)

```vb
Property GOSTDefaultSymbol As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Boolean

instance.GOSTDefaultSymbol = value

value = instance.GOSTDefaultSymbol
```

### C#

```csharp
System.bool GOSTDefaultSymbol {get; set;}
```

### C++/CLI

```cpp
property System.bool GOSTDefaultSymbol {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the GOST Add default symbol option is set, false if it is not

## VBA Syntax

See [SFSymbol::GOSTDefaultSymbol](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GOSTDefaultSymbol.html).

## Remarks

[ISFSymbol::GOSTNotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GOSTNotation.html) must be True to set this property.

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
