---
title: "InsertChainDim Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertChainDim"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertChainDim.html"
---

# InsertChainDim Method (IDrawingDoc)

Obsolete. Superseded by [IModelDocExtension::InsertChainDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertChainDimensions.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertChainDim()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.InsertChainDim()
```

### C#

```csharp
void InsertChainDim()
```

### C++/CLI

```cpp
void InsertChainDim();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::InsertChainDim](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertChainDim.html).

## Remarks

To insert a chain dimension into a drawing:

1. Call this method.
2. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the first entity. This entity is used to create all dimensions in the chain.
3. Call IModelDocExtension::SelectByID2 to select the second entity to dimension with respect to the first.
4. Call [IModelDoc2::AddDimension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2.html).
5. Call IModelDocExtension::SelectByID2 to select the next entity to dimension with respect to the first.
6. Call IModelDoc2::AddDimension2 to add the dimension to the chain.
7. Repeat steps 5 and 6 to add more dimensions to the chain.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
