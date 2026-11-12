---
title: "IsExploded Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IsExploded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsExploded.html"
---

# IsExploded Method (IModelDocExtension)

Gets the name of the exploded view currently shown in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsExploded( _
   ByRef ViewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ViewName As System.String
Dim value As System.Boolean

value = instance.IsExploded(ViewName)
```

### C#

```csharp
System.bool IsExploded(
   out System.string ViewName
)
```

### C++/CLI

```cpp
System.bool IsExploded(
   [Out] System.String^ ViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewName`: Name of the exploded view currently shown in the model or an empty string if the model is collapsed

### Return Value

True if the specified exploded view is currently shown in the model, false if the model is currently collapsed

## VBA Syntax

See [ModelDocExtension::IsExploded](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IsExploded.html).

## Examples

[Get Exploded Views for Configuration (C#)](Get_Exploded_Views_for_Configuration_Example_CSharp.htm)
[Get Exploded Views for Configuration (VB.NET)](Get_Exploded_Views_for_Configuration_Example_VBNET.htm)
[Get Exploded Views for Configuration (VBA)](Get_Exploded_Views_for_Configuration_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IAssemblyDoc::AutoExplode Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.html)
[IAssemblyDoc::CreateExplodedView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateExplodedView.html)
[IAssemblyDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewConfigurationName.html)
[IAssemblyDoc::GetExplodedViewCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount2.html)
[IAssemblyDoc::GetExplodedViewNames2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames2.html)
[IAssemblyDoc::ShowExploded2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.html)
[IAssemblyDoc::ViewCollapseAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.html)
[IAssemblyDoc::ViewExplodeAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.html)
[IView::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsExploded.html)
[IView::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowExploded.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
