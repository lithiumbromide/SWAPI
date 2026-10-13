---
title: "ScaleHatchPattern Property (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "ScaleHatchPattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~ScaleHatchPattern.html"
---

# ScaleHatchPattern Property (IDetailCircle)

Gets or sets whether to scale the hatch pattern for this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleHatchPattern As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Boolean

instance.ScaleHatchPattern = value

value = instance.ScaleHatchPattern
```

### C#

```csharp
System.bool ScaleHatchPattern {get; set;}
```

### C++/CLI

```cpp
property System.bool ScaleHatchPattern {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to scale the hatch pattern based on the scale of the detail view, false to not

## VBA Syntax

See [DetailCircle::ScaleHatchPattern](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~ScaleHatchPattern.html).

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
