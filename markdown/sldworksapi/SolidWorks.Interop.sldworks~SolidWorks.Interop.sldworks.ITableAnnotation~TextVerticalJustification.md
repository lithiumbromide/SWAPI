---
title: "TextVerticalJustification Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "TextVerticalJustification"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TextVerticalJustification.html"
---

# TextVerticalJustification Property (ITableAnnotation)

Gets or sets the vertical justification for the text in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Property TextVerticalJustification As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Integer

instance.TextVerticalJustification = value

value = instance.TextVerticalJustification
```

### C#

```csharp
System.int TextVerticalJustification {get; set;}
```

### C++/CLI

```cpp
property System.int TextVerticalJustification {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Vertical justification as defined by [swTextAlignmentVertical_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextAlignmentVertical_e.html)

## VBA Syntax

See [TableAnnotation::TextVerticalJustification](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~TextVerticalJustification.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::TextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TextHorizontalJustification.html)
[ITableAnnotation::CellTextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextHorizontalJustification.html)
[ITableAnnotation::CellTextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextVerticalJustification.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
