---
title: "CreateDiamDim Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateDiamDim"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim.html"
---

# CreateDiamDim Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateDiamDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateDiamDim4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDiamDim( _
   ByVal DimVal As System.Double, _
   ByVal VP0 As System.Object, _
   ByVal VP1 As System.Object, _
   ByVal VP2 As System.Object, _
   ByVal VP3 As System.Object, _
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
Dim DimVal As System.Double
Dim VP0 As System.Object
Dim VP1 As System.Object
Dim VP2 As System.Object
Dim VP3 As System.Object
Dim ArrowSize As System.Double
Dim Text As System.String
Dim TextHeight As System.Double
Dim WitnessGap As System.Double
Dim WitnessOvershoot As System.Double
Dim value As System.Boolean

value = instance.CreateDiamDim(DimVal, VP0, VP1, VP2, VP3, ArrowSize, Text, TextHeight, WitnessGap, WitnessOvershoot)
```

### C#

```csharp
System.bool CreateDiamDim(
   System.double DimVal,
   System.object VP0,
   System.object VP1,
   System.object VP2,
   System.object VP3,
   System.double ArrowSize,
   System.string Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot
)
```

### C++/CLI

```cpp
System.bool CreateDiamDim(
   System.double DimVal,
   System.Object^ VP0,
   System.Object^ VP1,
   System.Object^ VP2,
   System.Object^ VP3,
   System.double ArrowSize,
   System.String^ Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DimVal`:
- `VP0`:
- `VP1`:
- `VP2`:
- `VP3`:
- `ArrowSize`:
- `Text`:
- `TextHeight`:
- `WitnessGap`:
- `WitnessOvershoot`:

## VBA Syntax

See [DrawingDoc::CreateDiamDim](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateDiamDim.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
