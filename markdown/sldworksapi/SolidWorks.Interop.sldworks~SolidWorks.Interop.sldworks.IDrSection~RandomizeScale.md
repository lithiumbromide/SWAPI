---
title: "RandomizeScale Property (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "RandomizeScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~RandomizeScale.html"
---

# RandomizeScale Property (IDrSection)

Gets or sets whether to randomize the scale when auto hatching this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property RandomizeScale As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

instance.RandomizeScale = value

value = instance.RandomizeScale
```

### C#

```csharp
System.bool RandomizeScale {get; set;}
```

### C++/CLI

```cpp
property System.bool RandomizeScale {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to randomize the scale when auto hatching, false to not

## VBA Syntax

See [DrSection::RandomizeScale](ms-its:sldworksapivb6.chm::/sldworks~DrSection~RandomizeScale.html).

## Remarks

This property is valid only if [IDrSectionView::GetAutoHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetAutoHatch.html) is true.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::ScaleHatchPattern Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ScaleHatchPattern.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
