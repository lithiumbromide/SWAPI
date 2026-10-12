---
title: "CreateDrawViewFromModelView Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateDrawViewFromModelView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView.html"
---

# CreateDrawViewFromModelView Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateDrawViewFromModelView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDrawViewFromModelView( _
   ByVal ModelName As System.String, _
   ByVal ViewName As System.String, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim ViewName As System.String
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim value As System.Boolean

value = instance.CreateDrawViewFromModelView(ModelName, ViewName, LocX, LocY, LocZ)
```

### C#

```csharp
System.bool CreateDrawViewFromModelView(
   System.string ModelName,
   System.string ViewName,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

### C++/CLI

```cpp
System.bool CreateDrawViewFromModelView(
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

See [DrawingDoc::CreateDrawViewFromModelView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateDrawViewFromModelView.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
