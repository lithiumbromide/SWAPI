---
title: "IGetNext Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "IGetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetNext.html"
---

# IGetNext Method (IDatumTag)

Gets the next datum tag in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNext() As DatumTag
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim value As DatumTag

value = instance.IGetNext()
```

### C#

```csharp
DatumTag IGetNext()
```

### C++/CLI

```cpp
DatumTag^ IGetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the next [datum tag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag.html)

## VBA Syntax

See [DatumTag::IGetNext](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~IGetNext.html).

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatum::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetNext.html)
[IView::GetFirstDatumTag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumTag.html)
[IView::IGetFirstDatumTag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstDatumTag.html)
[IModelDoc2::IInsertDatumTag2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertDatumTag2.html)
[IModelDoc2::InsertDatumTag2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertDatumTag2.html)
[IAnnotation::GetSpecificAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSpecificAnnotation.html)
[IAnnotation::IGetSpecificAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.html)
