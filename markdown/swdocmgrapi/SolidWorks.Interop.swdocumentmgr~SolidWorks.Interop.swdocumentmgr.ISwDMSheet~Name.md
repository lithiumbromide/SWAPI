---
title: "Name Property (ISwDMSheet)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSheet"
member: "Name"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~Name.html"
---

# Name Property (ISwDMSheet)

Gets the name of the drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSheet
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of drawing sheet.

## VBA Syntax

See [SwDMSheet::Name](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSheet~Name.html).

## Examples

[Get Preview Bitmaps of Drawing Sheets (C#)](Get_Preview_Bitmaps_of_Drawing_Sheets_Example_CSharp.htm)
[Get Preview Bitmaps of Drawing Sheets (VB.NET)](Get_Preview_Bitmaps_of_Drawing_Sheets_Example_VBNET.htm)

## See Also

[ISwDMSheet Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.html)
[ISwDMSheet Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
