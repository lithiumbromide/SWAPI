---
title: "CreateOrdinateDim Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateOrdinateDim"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim.html"
---

# CreateOrdinateDim Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateOrdinateDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateOrdinateDim( _
   ByVal P0 As System.Object, _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object, _
   ByVal P3 As System.Object, _
   ByVal P4 As System.Object, _
   ByVal Angle As System.Double, _
   ByVal ArrowSize As System.Double, _
   ByVal Text As System.String, _
   ByVal TextHeight As System.Double, _
   ByVal WitnessGap As System.Double, _
   ByVal WitnessOvershoot As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim P0 As System.Object
Dim P1 As System.Object
Dim P2 As System.Object
Dim P3 As System.Object
Dim P4 As System.Object
Dim Angle As System.Double
Dim ArrowSize As System.Double
Dim Text As System.String
Dim TextHeight As System.Double
Dim WitnessGap As System.Double
Dim WitnessOvershoot As System.Double
Dim value As System.Boolean

value = instance.CreateOrdinateDim(P0, P1, P2, P3, P4, Angle, ArrowSize, Text, TextHeight, WitnessGap, WitnessOvershoot)
```

### C#

```csharp
System.bool CreateOrdinateDim(
   System.object P0,
   System.object P1,
   System.object P2,
   System.object P3,
   System.object P4,
   System.double Angle,
   System.double ArrowSize,
   System.string Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot
)
```

### C++/CLI

```cpp
System.bool CreateOrdinateDim(
   System.Object^ P0,
   System.Object^ P1,
   System.Object^ P2,
   System.Object^ P3,
   System.Object^ P4,
   System.double Angle,
   System.double ArrowSize,
   System.String^ Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P0`:
- `P1`:
- `P2`:
- `P3`:
- `P4`:
- `Angle`:
- `ArrowSize`:
- `Text`:
- `TextHeight`:
- `WitnessGap`:
- `WitnessOvershoot`:

## VBA Syntax

See [DrawingDoc::CreateOrdinateDim](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateOrdinateDim.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
