---
title: "CreateText Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText.html"
---

# CreateText Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateText2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateText2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateText( _
   ByVal TextString As System.String, _
   ByVal TextX As System.Double, _
   ByVal TextY As System.Double, _
   ByVal TextZ As System.Double, _
   ByVal TextHeight As System.Double, _
   ByVal TextAngle As System.Double _
) As System.Boolean
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
Dim value As System.Boolean

value = instance.CreateText(TextString, TextX, TextY, TextZ, TextHeight, TextAngle)
```

### C#

```csharp
System.bool CreateText(
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
System.bool CreateText(
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

- `TextString`:
- `TextX`:
- `TextY`:
- `TextZ`:
- `TextHeight`:
- `TextAngle`:

## VBA Syntax

See [DrawingDoc::CreateText](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateText.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
