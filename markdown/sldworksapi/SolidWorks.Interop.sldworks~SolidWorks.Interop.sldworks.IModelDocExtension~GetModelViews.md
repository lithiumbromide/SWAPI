---
title: "GetModelViews Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetModelViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelViews.html"
---

# GetModelViews Method (IModelDocExtension)

Gets the model views in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelViews() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetModelViews()
```

### C#

```csharp
System.object GetModelViews()
```

### C++/CLI

```cpp
System.Object^ GetModelViews();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [model views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::GetModelViews](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetModelViews.html).

## Examples

[Get Scale Factor of Each Model View (C++)](Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm)
[Get Scale Factor of Each Model View (C#)](Get_Scale_of_Each_Model_View_Example_CSharp.htm)
[Get Scale Factor of Each Model View (VB.NET)](Get_Scale_of_Each_Model_View_Example_VBNET.htm)
[Get Scale Factor of Each Model View (VBA)](Get_Scale_of_Each_Model_View_Example_VB.htm)

## Remarks

The model views are set using either **SOLIDWORKS menu > Window > Viewport** or [IModelViewManager::ViewportDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ViewportDisplay.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IGetModelViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetModelViews.html)
[IModelDocExtension::GetModelViewCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelViewCount.html)
[IModelDoc2::GetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.html)
[IModelDoc2::IGetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.html)
[IModelView::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetNext.html)
[IModelView::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetNext.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
