---
title: "CreateText2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateText2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.html"
---

# CreateText2 Method (IDrawingDoc)

Creates a [note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) containing the specified text at a given location.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateText2( _
   ByVal TextString As System.String, _
   ByVal TextX As System.Double, _
   ByVal TextY As System.Double, _
   ByVal TextZ As System.Double, _
   ByVal TextHeight As System.Double, _
   ByVal TextAngle As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim TextString As System.String
Dim TextX As System.Double
Dim TextY As System.Double
Dim TextZ As System.Double
Dim TextHeight As System.Double
Dim TextAngle As System.Double
Dim value As System.Object

value = instance.CreateText2(TextString, TextX, TextY, TextZ, TextHeight, TextAngle)
```

### C#

```csharp
System.object CreateText2(
   System.string TextString,
   System.double TextX,
   System.double TextY,
   System.double TextZ,
   System.double TextHeight,
   System.double TextAngle
)
```

### C++/CLI

```cpp
System.Object^ CreateText2(
   System.String^ TextString,
   System.double TextX,
   System.double TextY,
   System.double TextZ,
   System.double TextHeight,
   System.double TextAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TextString`: User input text
- `TextX`: X text location in meters (see **Remarks**)
- `TextY`: Y text location in meters (see Remarks)
- `TextZ`: Z text location in meters (see Remarks)
- `TextHeight`: Text height in meters
- `TextAngle`: Text angle for rotated text in radians

### Return Value

Newly created note

## VBA Syntax

See [DrawingDoc::CreateText2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateText2.html).

## Remarks

The location specifies the position of the upper-left corner of the box containing the text with respect to the lower-left corner of the drawing.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ICreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateText2.html)
