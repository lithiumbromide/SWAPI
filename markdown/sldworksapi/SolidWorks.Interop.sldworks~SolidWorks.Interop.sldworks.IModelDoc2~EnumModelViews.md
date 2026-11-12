---
title: "EnumModelViews Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EnumModelViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EnumModelViews.html"
---

# EnumModelViews Method (IModelDoc2)

Gets the model views enumeration in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumModelViews() As EnumModelViews
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As EnumModelViews

value = instance.EnumModelViews()
```

### C#

```csharp
EnumModelViews EnumModelViews()
```

### C++/CLI

```cpp
EnumModelViews^ EnumModelViews();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Model views enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumModelViews.html)

## VBA Syntax

See [ModelDoc2::EnumModelViews](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EnumModelViews.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetModelViewCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetModelViewCount.html)
[IModelDoc2::GetModelViewNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetModelViewNames.html)
[IModelDoc2::IGetModelViewNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetModelViewNames.html)
[IModelDoc2::ActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ActiveView.html)
[IModelDoc2::IActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IActiveView.html)
[IModelDoc2::ModelViewManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ModelViewManager.html)
[IModelDoc2::IGetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.html)
[IModelDoc2::GetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
