---
title: "WatermarkNote Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "WatermarkNote"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkNote.html"
---

# WatermarkNote Property (INote)

Gets or sets whether the note is a watermark in a part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property WatermarkNote As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

instance.WatermarkNote = value

value = instance.WatermarkNote
```

### C#

```csharp
System.bool WatermarkNote {get; set;}
```

### C++/CLI

```cpp
property System.bool WatermarkNote {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the note is a watermark in a part or assembly, false if not

## VBA Syntax

See [Note::WatermarkNote](ms-its:sldworksapivb6.chm::/sldworks~Note~WatermarkNote.html).

## Examples

[Add Watermark to Part (C#)](Add_Watermark_to_Part_Example_CSharp.htm)
[Add Watermark to Part (VB.NET)](Add_Watermark_to_Part_Example_VBNET.htm)
[Add Watermark to Part (VBA)](Add_Watermark_to_Part_Example_VB.htm)

## Remarks

To add a watermark to a part or assembly document:

1. Open a part or assembly document.
2. Expand the **Annotations** folder in the FeatureManager design tree.
3. Right click **Notes Area** and click **Activate**.
4. Click **Insert > Annotations > Note**
5. Place the note in the graphics area, type the note text, and click **OK** in the Notes PropertyManager page.
6. Right-click the note and click **Watermark**.

Use [ISheet::BehindSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~BehindSheet.html) to place a note on the sheet format behind a drawing sheet, which allows you to display the note as watermark in a drawing.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::WatermarkBehindGeometry Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkBehindGeometry.html)
[INote::WatermarkTransparencyLevel Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkTransparencyLevel.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
