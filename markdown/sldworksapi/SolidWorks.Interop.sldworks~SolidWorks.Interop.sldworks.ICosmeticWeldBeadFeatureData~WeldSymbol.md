---
title: "WeldSymbol Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "WeldSymbol"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~WeldSymbol.html"
---

# WeldSymbol Property (ICosmeticWeldBeadFeatureData)

Gets or sets the weld symbol for this weld bead.

## Syntax

### Visual Basic (Declaration)

```vb
Property WeldSymbol As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Object

instance.WeldSymbol = value

value = instance.WeldSymbol
```

### C#

```csharp
System.object WeldSymbol {get; set;}
```

### C++/CLI

```cpp
property System.Object^ WeldSymbol {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IWeldSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol.html)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::WeldSymbol](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~WeldSymbol.html).

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
