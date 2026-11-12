---
title: "CreateExplodedView Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "CreateExplodedView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateExplodedView.html"
---

# CreateExplodedView Method (IAssemblyDoc)

Creates an explode view of the active assembly configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateExplodedView() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.CreateExplodedView()
```

### C#

```csharp
System.bool CreateExplodedView()
```

### C++/CLI

```cpp
System.bool CreateExplodedView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the explode view is successfully created, false if not

## VBA Syntax

See [AssemblyDoc::CreateExplodedView](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~CreateExplodedView.html).

## Examples

[Create Exploded Views of an Assembly (VBA)](Create_Exploded_Views_Example_VB.htm)
[Create Exploded Views of an Assembly (VB.NET)](Create_Exploded_Views_Example_VBNET.htm)
[Create Exploded Views of an Assembly (C#)](Create_Exploded_Views_Example_CSharp.htm)

## Remarks

Call this method multiple times to add multiple explode views to the active assembly configuration.

Perfect explode views often require user interaction. This method attempts to create a perfect explode view based on the current mate conditions.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AutoExplode Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.html)
[IAssemblyDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewConfigurationName.html)
[IAssemblyDoc::GetExplodedViewCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount2.html)
[IAssemblyDoc::GetExplodedViewNames2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames2.html)
[IAssemblyDoc::ShowExploded2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.html)
[IAssemblyDoc::ViewCollapseAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.html)
[IAssemblyDoc::ViewExplodeAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.html)
[IModelDocExtension::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsExploded.html)
[IView::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsExploded.html)
[IView::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowExploded.html)
[IConfiguration::AddRadialExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep.html)
[IConfiguration::AddExplodeStep2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep2.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
