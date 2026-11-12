---
title: "WatermarkTransparencyLevel Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "WatermarkTransparencyLevel"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkTransparencyLevel.html"
---

# WatermarkTransparencyLevel Property (INote)

Gets or sets the transparency level of a note specified to be a watermark.

## Syntax

### Visual Basic (Declaration)

```vb
Property WatermarkTransparencyLevel As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Double

instance.WatermarkTransparencyLevel = value

value = instance.WatermarkTransparencyLevel
```

### C#

```csharp
System.double WatermarkTransparencyLevel {get; set;}
```

### C++/CLI

```cpp
property System.double WatermarkTransparencyLevel {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= Level of transparency <= 1.0 (see **Remarks**)

## VBA Syntax

See [Note::WatermarkTransparencyLevel](ms-its:sldworksapivb6.chm::/sldworks~Note~WatermarkTransparencyLevel.html).

## Examples

[Add Watermark to Part (C#)](Add_Watermark_to_Part_Example_CSharp.htm)
[Add Watermark to Part (VB.NET)](Add_Watermark_to_Part_Example_VBNET.htm)
[Add Watermark to Part (VBA)](Add_Watermark_to_Part_Example_VB.htm)

## Remarks

This property is only available when [INote::WatermarkNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkNote.html) is true.

A transparency level of 0.0 indicates that the transparency level is not set for the watermark; a transparency level of 1.0 indicates that the watermark is fully transparent.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::WatermarkBehindGeometry Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkBehindGeometry.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
