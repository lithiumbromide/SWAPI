---
title: "Flipped Property (IDowelSymbol)"
project: "SOLIDWORKS API Help"
interface: "IDowelSymbol"
member: "Flipped"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~Flipped.html"
---

# Flipped Property (IDowelSymbol)

Gets or sets whether to flip this dowel symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Property Flipped As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDowelSymbol
Dim value As System.Boolean

instance.Flipped = value

value = instance.Flipped
```

### C#

```csharp
System.bool Flipped {get; set;}
```

### C++/CLI

```cpp
property System.bool Flipped {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the dowel is flipped, false if it is not

## VBA Syntax

See [DowelSymbol::Flipped](ms-its:sldworksapivb6.chm::/sldworks~DowelSymbol~Flipped.html).

## Examples

[Flip Dowel Pin Symbol (VBA)](Flip_Dowel_Pin_Symbol_Example_VB.htm)
[Flip Dowel Pin Symbol (C#)](Flip_Dowel_Pin_Symbol_Example_CSharp.htm)
[Flip Dowel Pin Symbol (VB.NET)](Flip_Dowel_Pin_Symbol_Example_VBNET.htm)

## Remarks

Call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html) after flipping the dowel pin symbol.

## See Also

[IDowelSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.html)
[IDowelSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
