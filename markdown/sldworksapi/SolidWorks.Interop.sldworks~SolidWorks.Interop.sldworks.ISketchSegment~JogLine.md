---
title: "JogLine Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "JogLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~JogLine.html"
---

# JogLine Method (ISketchSegment)

Creates rectangular jog on the specified line.

## Syntax

### Visual Basic (Declaration)

```vb
Sub JogLine( _
   ByVal XOnLine As System.Double, _
   ByVal YOnLine As System.Double, _
   ByVal ZOnLine As System.Double, _
   ByVal XOnJog As System.Double, _
   ByVal YOnJog As System.Double, _
   ByVal ZOnJog As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim XOnLine As System.Double
Dim YOnLine As System.Double
Dim ZOnLine As System.Double
Dim XOnJog As System.Double
Dim YOnJog As System.Double
Dim ZOnJog As System.Double

instance.JogLine(XOnLine, YOnLine, ZOnLine, XOnJog, YOnJog, ZOnJog)
```

### C#

```csharp
void JogLine(
   System.double XOnLine,
   System.double YOnLine,
   System.double ZOnLine,
   System.double XOnJog,
   System.double YOnJog,
   System.double ZOnJog
)
```

### C++/CLI

```cpp
void JogLine(
   System.double XOnLine,
   System.double YOnLine,
   System.double ZOnLine,
   System.double XOnJog,
   System.double YOnJog,
   System.double ZOnJog
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XOnLine`: x coordinate where to begin the jog on the selected line
- `YOnLine`: y coordinate where to begin the jog on the selected line
- `ZOnLine`: z coordinate where to begin the jog on the selected line
- `XOnJog`: x coordinate of the width and depth of the jog
- `YOnJog`: y coordinate of the width and depth of the jog
- `ZOnJog`: z coordinate of the width and depth of the jog

## VBA Syntax

See [SketchSegment::JogLine](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~JogLine.html).

## Examples

[Insert Explode Line Sketch and Jog Line (VB.NET)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VBNET.htm)
[Insert Explode Line Sketch and Jog Line (VBA)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VB.htm)
[Insert Explode Line Sketch and Jog Line (C#)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_CSharp.htm)

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchManager::InsertExplodeLineSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertExplodeLineSketch.html)
[ISketchManager::Insert3DSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Insert3DSketch.html)
[ISketch::InsertRouteLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~InsertRouteLine.html)
[ISketchManager::CreateLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateLine.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
