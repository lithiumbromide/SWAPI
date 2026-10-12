---
title: "CreateAngDim3 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateAngDim3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim3.html"
---

# CreateAngDim3 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateAngDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateAngDim4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateAngDim3( _
   ByVal VP0 As System.Object, _
   ByVal VP1 As System.Object, _
   ByVal VP2 As System.Object, _
   ByVal VP3 As System.Object, _
   ByVal VP4 As System.Object, _
   ByVal VP5 As System.Object, _
   ByVal VP6 As System.Object, _
   ByVal ArrowSize As System.Double, _
   ByVal Text As System.String, _
   ByVal TextHeight As System.Double, _
   ByVal WitnessGap As System.Double, _
   ByVal WitnessOvershoot As System.Double, _
   ByVal VTextPoint As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim VP0 As System.Object
Dim VP1 As System.Object
Dim VP2 As System.Object
Dim VP3 As System.Object
Dim VP4 As System.Object
Dim VP5 As System.Object
Dim VP6 As System.Object
Dim ArrowSize As System.Double
Dim Text As System.String
Dim TextHeight As System.Double
Dim WitnessGap As System.Double
Dim WitnessOvershoot As System.Double
Dim VTextPoint As System.Object
Dim value As System.Object

value = instance.CreateAngDim3(VP0, VP1, VP2, VP3, VP4, VP5, VP6, ArrowSize, Text, TextHeight, WitnessGap, WitnessOvershoot, VTextPoint)
```

### C#

```csharp
System.object CreateAngDim3(
   System.object VP0,
   System.object VP1,
   System.object VP2,
   System.object VP3,
   System.object VP4,
   System.object VP5,
   System.object VP6,
   System.double ArrowSize,
   System.string Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   System.object VTextPoint
)
```

### C++/CLI

```cpp
System.Object^ CreateAngDim3(
   System.Object^ VP0,
   System.Object^ VP1,
   System.Object^ VP2,
   System.Object^ VP3,
   System.Object^ VP4,
   System.Object^ VP5,
   System.Object^ VP6,
   System.double ArrowSize,
   System.String^ Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   System.Object^ VTextPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VP0`:
- `VP1`:
- `VP2`:
- `VP3`:
- `VP4`:
- `VP5`:
- `VP6`:
- `ArrowSize`:
- `Text`:
- `TextHeight`:
- `WitnessGap`:
- `WitnessOvershoot`:
- `VTextPoint`:

## VBA Syntax

See [DrawingDoc::CreateAngDim3](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateAngDim3.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
