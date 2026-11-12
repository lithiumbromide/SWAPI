---
title: "GetModelViewCount Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetModelViewCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelViewCount.html"
---

# GetModelViewCount Method (IModelDocExtension)

Gets the number of model views in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelViewCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.GetModelViewCount()
```

### C#

```csharp
System.int GetModelViewCount()
```

### C++/CLI

```cpp
System.int GetModelViewCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of model views (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::GetModelViewCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetModelViewCount.html).

## Examples

[Get Scale Factor of Each Model View (C++)](Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm)
[Get Scale Factor of Each Model View (C#)](Get_Scale_of_Each_Model_View_Example_CSharp.htm)
[Get Scale Factor of Each Model View (VB.NET)](Get_Scale_of_Each_Model_View_Example_VBNET.htm)
[Get Scale Factor of Each Model View (VBA)](Get_Scale_of_Each_Model_View_Example_VB.htm)

## Remarks

Call this method before calling [IModelDocExtension::IGetModelViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetModelViews.html) to determine the size of the array for that method.

This method returns the number of model views set using either **SOLIDWORKS menu > Window > Viewport** or [IModelViewManager::ViewportDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ViewportDisplay.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetModelViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelViews.html)
[IModelDoc2::GetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.html)
[IModelDoc2::IGetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.html)
[IModelView::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetNext.html)
[IModelView::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetNext.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
