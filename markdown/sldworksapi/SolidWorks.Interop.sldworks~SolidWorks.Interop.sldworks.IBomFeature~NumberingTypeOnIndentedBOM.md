---
title: "NumberingTypeOnIndentedBOM Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "NumberingTypeOnIndentedBOM"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~NumberingTypeOnIndentedBOM.html"
---

# NumberingTypeOnIndentedBOM Property (IBomFeature)

Gets and sets the type of numbering for this indented BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberingTypeOnIndentedBOM As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Integer

instance.NumberingTypeOnIndentedBOM = value

value = instance.NumberingTypeOnIndentedBOM
```

### C#

```csharp
System.int NumberingTypeOnIndentedBOM {get; set;}
```

### C++/CLI

```cpp
property System.int NumberingTypeOnIndentedBOM {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of numbering as defined in [swNumberingType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberingType_e.html)

## VBA Syntax

See [BomFeature::NumberingTypeOnIndentedBOM](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~NumberingTypeOnIndentedBOM.html).

## Examples

See [IBomFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature.html) examples.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IView::InsertBomTable4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable4.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
