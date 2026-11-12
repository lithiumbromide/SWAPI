---
title: "WatermarkBehindGeometry Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "WatermarkBehindGeometry"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkBehindGeometry.html"
---

# WatermarkBehindGeometry Property (INote)

Gets or sets whether to place this note, specified to be a watermark, behind the geometry in a part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property WatermarkBehindGeometry As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

instance.WatermarkBehindGeometry = value

value = instance.WatermarkBehindGeometry
```

### C#

```csharp
System.bool WatermarkBehindGeometry {get; set;}
```

### C++/CLI

```cpp
property System.bool WatermarkBehindGeometry {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to place this note behind the geometry in a part or assembly, false to place this note in front of the geometry in a part or assembly

## VBA Syntax

See [Note::WatermarkBehindGeometry](ms-its:sldworksapivb6.chm::/sldworks~Note~WatermarkBehindGeometry.html).

## Examples

[Add Watermark to Part (C#)](Add_Watermark_to_Part_Example_CSharp.htm)
[Add Watermark to Part (VB.NET)](Add_Watermark_to_Part_Example_VBNET.htm)
[Add Watermark to Part (VBA)](Add_Watermark_to_Part_Example_VB.htm)

## Remarks

This property is only available when [INote::WatermarkNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkNote.html) is true.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::WatermarkTransparencyLevel Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkTransparencyLevel.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
