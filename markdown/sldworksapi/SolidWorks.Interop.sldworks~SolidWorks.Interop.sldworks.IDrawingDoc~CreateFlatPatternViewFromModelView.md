---
title: "CreateFlatPatternViewFromModelView Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateFlatPatternViewFromModelView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView.html"
---

# CreateFlatPatternViewFromModelView Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateFlatPatternViewFromModelView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFlatPatternViewFromModelView( _
   ByVal ModelName As System.String, _
   ByVal ConfigName As System.String, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim ConfigName As System.String
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim value As System.Boolean

value = instance.CreateFlatPatternViewFromModelView(ModelName, ConfigName, LocX, LocY, LocZ)
```

### C#

```csharp
System.bool CreateFlatPatternViewFromModelView(
   System.string ModelName,
   System.string ConfigName,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

### C++/CLI

```cpp
System.bool CreateFlatPatternViewFromModelView(
   System.String^ ModelName,
   System.String^ ConfigName,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelName`:
- `ConfigName`:
- `LocX`:
- `LocY`:
- `LocZ`:

## VBA Syntax

See [DrawingDoc::CreateFlatPatternViewFromModelView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateFlatPatternViewFromModelView.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
