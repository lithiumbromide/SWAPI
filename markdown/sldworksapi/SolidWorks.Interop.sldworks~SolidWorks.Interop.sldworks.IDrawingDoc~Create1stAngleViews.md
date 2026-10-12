---
title: "Create1stAngleViews Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "Create1stAngleViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews.html"
---

# Create1stAngleViews Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::1stAngleViews2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Create1stAngleViews( _
   ByVal ModelName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim value As System.Boolean

value = instance.Create1stAngleViews(ModelName)
```

### C#

```csharp
System.bool Create1stAngleViews(
   System.string ModelName
)
```

### C++/CLI

```cpp
System.bool Create1stAngleViews(
   System.String^ ModelName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelName`:

## VBA Syntax

See [DrawingDoc::Create1stAngleViews](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~Create1stAngleViews.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
