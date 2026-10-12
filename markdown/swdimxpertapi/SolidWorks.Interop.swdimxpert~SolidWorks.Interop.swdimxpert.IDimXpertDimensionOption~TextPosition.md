---
title: "TextPosition Property (IDimXpertDimensionOption)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDimensionOption"
member: "TextPosition"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption~TextPosition.html"
---

# TextPosition Property (IDimXpertDimensionOption)

Gets and sets coordinates of the dimension text.

## Syntax

### Visual Basic (Declaration)

```vb
Property TextPosition As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDimensionOption
Dim value As System.Object

instance.TextPosition = value

value = instance.TextPosition
```

### C#

```csharp
System.object TextPosition {get; set;}
```

### C++/CLI

```cpp
property System.Object^ TextPosition {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

### Property Value

Array of double values corresponding to x, y, and z coordinates of the dimension text

## VBA Syntax

See [DimXpertDimensionOption::TextPosition](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDimensionOption~TextPosition.html).

## Examples

[Get and Set Size Dimension Example (C#)](Get_and_Set_Size_Dimension_Example_CSharp.htm)
[Get and Set Size Dimension Example (VB.NET)](Get_and_Set_Size_Dimension_Example_VBNET.htm)
[Get and Set Size Dimension Example (VBA)](Get_and_Set_Size_Dimension_Example_VB.htm)

## See Also

[IDimXpertDimensionOption Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption.html)
[IDimXpertDimensionOption Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption_members.html)
[IDimXpertPart::InsertSizeDimension Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertSizeDimension.html)
[IDimXpertPart::InsertLocationDimension Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertLocationDimension.html)
[IDimXpertPart::InsertBasicDimension Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
