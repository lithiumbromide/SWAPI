---
title: "BehindSheet Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "BehindSheet"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~BehindSheet.html"
---

# BehindSheet Property (INote)

Places this note, located on the sheet format in a drawing, behind the drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Property BehindSheet As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

instance.BehindSheet = value

value = instance.BehindSheet
```

### C#

```csharp
System.bool BehindSheet {get; set;}
```

### C++/CLI

```cpp
property System.bool BehindSheet {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to place this note, located on the sheet format in a drawing, behind the drawing sheet; false to not

## VBA Syntax

See [Note::BehindSheet](ms-its:sldworksapivb6.chm::/sldworks~Note~BehindSheet.html).

## Examples

[Place Note Behind Drawing Sheet (C#)](Place_Note_Behind_Drawing_Sheet_Example_CSharp.htm)
[Place Note Behind Drawing Sheet (VB.NET)](Place_Note_Behind_Drawing_Sheet_Example_VBNET.htm)
[Place Note Behind Drawing Sheet (VBA)](Place_Note_Behind_Drawing_Sheet_Example_VB.htm)

## Remarks

This property places a note on the sheet format behind a drawing sheet, which allows you to display the note as watermark in a drawing. Before calling this property, you must call [IDrawingDoc::EditTemplate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditTemplate.html) and [IDrawingDoc::EditSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditSheet.html).

Use these properties to modify watermarks in parts and assemblies:

- [INote::WatermarkNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkNote.html)
- [INote::WatermarkBehindGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkBehindGeometry.html)
- [INote::WatermarkTransparencyLevel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkTransparencyLevel.html)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
