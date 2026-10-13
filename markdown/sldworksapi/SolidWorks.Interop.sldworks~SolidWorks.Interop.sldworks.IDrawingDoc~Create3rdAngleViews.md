---
title: "Create3rdAngleViews Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "Create3rdAngleViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews.html"
---

# Create3rdAngleViews Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::Create3rdAngleViews2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Create3rdAngleViews( _
   ByVal ModelName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim value As System.Boolean

value = instance.Create3rdAngleViews(ModelName)
```

### C#

```csharp
System.bool Create3rdAngleViews(
   System.string ModelName
)
```

### C++/CLI

```cpp
System.bool Create3rdAngleViews(
   System.String^ ModelName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelName`:

## VBA Syntax

See [DrawingDoc::Create3rdAngleViews](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~Create3rdAngleViews.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
