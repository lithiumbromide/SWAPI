---
title: "GetExplodedViewConfigurationName Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetExplodedViewConfigurationName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewConfigurationName.html"
---

# GetExplodedViewConfigurationName Method (IAssemblyDoc)

Gets the name of the configuration for the specified exploded view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExplodedViewConfigurationName( _
   ByVal ExplodedViewName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim ExplodedViewName As System.String
Dim value As System.String

value = instance.GetExplodedViewConfigurationName(ExplodedViewName)
```

### C#

```csharp
System.string GetExplodedViewConfigurationName(
   System.string ExplodedViewName
)
```

### C++/CLI

```cpp
System.String^ GetExplodedViewConfigurationName(
   System.String^ ExplodedViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExplodedViewName`: Name of the exploded view

### Return Value

Name of the configuration for the specified exploded view

## VBA Syntax

See [AssemblyDoc::GetExplodedViewConfigurationName](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetExplodedViewConfigurationName.html).

## Examples

[Get Exploded Views for Configuration (C#)](Get_Exploded_Views_for_Configuration_Example_CSharp.htm)
[Get Exploded Views for Configuration (VB.NET)](Get_Exploded_Views_for_Configuration_Example_VBNET.htm)
[Get Exploded Views for Configuration (VBA)](Get_Exploded_Views_for_Configuration_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetExplodedViewCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount2.html)
[IAssemblyDoc::GetExplodedViewNames2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames2.html)
[IAssemblyDoc::CreateExplodedView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateExplodedView.html)
[IAssemblyDoc::AutoExplode Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.html)
[IAssemblyDoc::ShowExploded2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.html)
[IAssemblyDoc::ViewExplodeAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.html)
[IAssemblyDoc::ViewCollapseAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.html)
[IModelDocExtension::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsExploded.html)
[IView::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsExploded.html)
[IView::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowExploded.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
