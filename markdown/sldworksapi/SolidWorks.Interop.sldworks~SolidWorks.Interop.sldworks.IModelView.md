---
title: "IModelView Interface"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html"
---

# IModelView Interface

Allows you access to the model view's orientation, translation, and the Microsoft handle to the window.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IModelView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
```

### C#

```csharp
public interface IModelView
```

### C++/CLI

```cpp
public interface class IModelView
```

## VBA Syntax

See [ModelView](ms-its:sldworksapivb6.chm::/sldworks~ModelView.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Get Scale Factor of Each Model View (C++)](Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm)
[Get Scale Factor of Each Model View (C#)](Get_Scale_of_Each_Model_View_Example_CSharp.htm)
[Get Scale Factor of Each Model View (VB.NET)](Get_Scale_of_Each_Model_View_Example_VBNET.htm)
[Get Scale Factor of Each Model View (VBA)](Get_Scale_of_Each_Model_View_Example_VB.htm)
[Create a Callout in a Model View (C#)](Create_Model_View_Callouts_Example_CSharp.htm)
[Create a Callout in a Model View (VB.NET)](Create_Model_View_Callouts_Example_VBNET.htm)
[Create a Callout in a Model View (VBA)](Create_Model_View_Callouts_Example_VB.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (C#)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_CSharp.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VB.NET)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VBNET.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VBA)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm)

## Remarks

Events are implemented with delegates in the Microsoft .NET Framework. See the [Overview](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks_namespace.html) topic for a list of delegates for this interface.

## Accessors

[IEnumModelViews::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumModelViews~Next.html)

[IModelDoc2::ActiveView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ActiveView.html) and [IModelDoc2::IActiveView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IActiveView.html)

[IModelDoc2::GetFirstModelView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetFirstModelView.html) and [IModelDoc2::IGetFirstModelView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetFirstModelView.html)

[IModelDocExtension::GetModelViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetModelViews.html) and [IModelDocExtension::IGetModelViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetModelViews.html)

[IModelView::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetNext.html) and [IModelView::IGetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGetNext.html)

## Access Diagram

[ModelView](SWObjectModel.pdf#ModelView)

## See Also

[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.html)
