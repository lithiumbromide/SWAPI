---
title: "CreateDrawViewFromModelView2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateDrawViewFromModelView2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView2.html"
---

# CreateDrawViewFromModelView2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateDrawViewFromModelView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDrawViewFromModelView2( _
   ByVal ModelName As System.String, _
   ByVal ViewName As System.String, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double _
) As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim ViewName As System.String
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim value As View

value = instance.CreateDrawViewFromModelView2(ModelName, ViewName, LocX, LocY, LocZ)
```

### C#

```csharp
View CreateDrawViewFromModelView2(
   System.string ModelName,
   System.string ViewName,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

### C++/CLI

```cpp
View^ CreateDrawViewFromModelView2(
   System.String^ ModelName,
   System.String^ ViewName,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelName`:
- `ViewName`:
- `LocX`:
- `LocY`:
- `LocZ`:

## VBA Syntax

See [DrawingDoc::CreateDrawViewFromModelView2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateDrawViewFromModelView2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
