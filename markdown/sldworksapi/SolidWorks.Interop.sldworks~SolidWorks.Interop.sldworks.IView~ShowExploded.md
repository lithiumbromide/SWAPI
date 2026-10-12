---
title: "ShowExploded Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ShowExploded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowExploded.html"
---

# ShowExploded Method (IView)

Shows an exploded assembly in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowExploded( _
   ByVal ShowIt As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim ShowIt As System.Boolean
Dim value As System.Boolean

value = instance.ShowExploded(ShowIt)
```

### C#

```csharp
System.bool ShowExploded(
   System.bool ShowIt
)
```

### C++/CLI

```cpp
System.bool ShowExploded(
   System.bool ShowIt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ShowIt`: True if you want this drawing view to display the exploded state of the current assembly configuration, false if you want this drawing view to display the collapsed state

### Return Value

True if successful in displaying the exploded assembly state, false if not

## VBA Syntax

See [View::ShowExploded](ms-its:sldworksapivb6.chm::/sldworks~View~ShowExploded.html).

## Remarks

The explode state that is displayed is based on the current assembly configuration used by this drawing view

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsExploded.html)
[IModelDocExtension::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsExploded.html)
[IAssemblyDoc::AutoExplode Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.html)
[IAssemblyDoc::CreateExplodedView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateExplodedView.html)
[IAssemblyDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewConfigurationName.html)
[IAssemblyDoc::GetExplodedViewCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount2.html)
[IAssemblyDoc::GetExplodedViewNames2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames2.html)
[IAssemblyDoc::ShowExploded2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.html)
[IAssemblyDoc::ViewCollapseAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.html)
[IAssemblyDoc::ViewExplodeAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.html)

## Availability
