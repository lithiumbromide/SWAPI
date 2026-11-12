---
title: "ShowExploded2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ShowExploded2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.html"
---

# ShowExploded2 Method (IAssemblyDoc)

Displays the specified exploded view for the current assembly configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowExploded2( _
   ByVal ShowIt As System.Boolean, _
   ByVal ExplodeViewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim ShowIt As System.Boolean
Dim ExplodeViewName As System.String
Dim value As System.Boolean

value = instance.ShowExploded2(ShowIt, ExplodeViewName)
```

### C#

```csharp
System.bool ShowExploded2(
   System.bool ShowIt,
   System.string ExplodeViewName
)
```

### C++/CLI

```cpp
System.bool ShowExploded2(
   System.bool ShowIt,
   System.String^ ExplodeViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ShowIt`: True if you want to show ExplodeViewName in its exploded state, false if you want to show it in its collapsed state
- `ExplodeViewName`: Name of the exploded view to show

### Return Value

True if the exploded view displays, false if not

## VBA Syntax

See [AssemblyDoc::ShowExploded2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ShowExploded2.html).

## Examples

[Create Exploded Views of an Assembly (VBA)](Create_Exploded_Views_Example_VB.htm)
[Create Exploded Views of an Assembly (VB.NET)](Create_Exploded_Views_Example_VBNET.htm)
[Create Exploded Views of an Assembly (C#)](Create_Exploded_Views_Example_CSharp.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AutoExplode Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.html)
[IAssemblyDoc::CreateExplodedView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateExplodedView.html)
[IAssemblyDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewConfigurationName.html)
[IAssemblyDoc::GetExplodedViewCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount2.html)
[IAssemblyDoc::GetExplodedViewNames2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames2.html)
[IAssemblyDoc::ViewCollapseAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.html)
[IAssemblyDoc::ViewExplodeAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.html)
[IModelDocExtension::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsExploded.html)
[IView::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsExploded.html)
[IView::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowExploded.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
