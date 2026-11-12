---
title: "GetFirstModelView Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetFirstModelView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.html"
---

# GetFirstModelView Method (IModelDoc2)

Gets the first view in a model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstModelView() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.GetFirstModelView()
```

### C#

```csharp
System.object GetFirstModelView()
```

### C++/CLI

```cpp
System.Object^ GetFirstModelView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [model view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) in this document

## VBA Syntax

See [ModelDoc2::GetFirstModelView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetFirstModelView.html).

## Examples

[Run SOLIDWORKS Commands and Synthesize Mouse Events (C#)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_CSharp.htm)
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VB.NET)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_VBNET.htm)
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VBA)](Run_SOLIDWORKS_Commands_and_Synthesize_Mouse_Events_Example_VB.htm)

## Remarks

You can traverse through the model views in a document by using this method to get the initial view and [IModelView::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetNext.html) to get each of subsequent views. You have reached the end of the list when IModelView::GetNext returns Nothing or null.

See [IModelDoc2::EnumModelViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EnumModelViews.html) for traversing the model views on a document.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IGetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.html)
[IModelDoc2::ActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ActiveView.html)
[IModelDoc2::IActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IActiveView.html)
[IModelDoc2::GetModelViewCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetModelViewCount.html)
[IModelDoc2::GetModelViewNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetModelViewNames.html)
[IModelDoc2::IGetModelViewNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetModelViewNames.html)
[IModelDoc2::ModelViewManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ModelViewManager.html)
[IModelDocExtension::GetModelViewCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelViewCount.html)
[IModelDocExtension::GetModelViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelViews.html)
[IModelDocExtension::IGetModelViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetModelViews.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
