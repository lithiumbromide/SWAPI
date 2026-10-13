---
title: "IGetNext Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "IGetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~IGetNext.html"
---

# IGetNext Method (IDatumTargetSym)

Gets the next datum target symbol in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNext() As DatumTargetSym
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim value As DatumTargetSym

value = instance.IGetNext()
```

### C#

```csharp
DatumTargetSym IGetNext()
```

### C++/CLI

```cpp
DatumTargetSym^ IGetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the next [datum target symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym.html)

## VBA Syntax

See [DatumTargetSym::IGetNext](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~IGetNext.html).

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetNext.html)
[IAnnotation::GetSpecificAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSpecificAnnotation.html)
[IAnnotation::IGetSpecificAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.html)
[IModelDocExtension::InsertDatumTargetSymbol2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertDatumTargetSymbol2.html)
[IView::GetFirstDatumTargetSym Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumTargetSym.html)
[IView::IGetFirstDatumTargetSym Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstDatumTargetSym.html)
