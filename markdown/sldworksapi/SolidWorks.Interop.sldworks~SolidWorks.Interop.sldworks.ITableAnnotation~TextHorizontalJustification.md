---
title: "TextHorizontalJustification Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "TextHorizontalJustification"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TextHorizontalJustification.html"
---

# TextHorizontalJustification Property (ITableAnnotation)

Gets or sets the horizontal justification setting for the text in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Property TextHorizontalJustification As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Integer

instance.TextHorizontalJustification = value

value = instance.TextHorizontalJustification
```

### C#

```csharp
System.int TextHorizontalJustification {get; set;}
```

### C++/CLI

```cpp
property System.int TextHorizontalJustification {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Horizontal justification as defined in [swTextJustification_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextJustification_e.html)

## VBA Syntax

See [TableAnnotation::TextHorizontalJustification](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~TextHorizontalJustification.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::TextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TextVerticalJustification.html)
[ITableAnnotation::CellTextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextHorizontalJustification.html)
[ITableAnnotation::CellTextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextVerticalJustification.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
