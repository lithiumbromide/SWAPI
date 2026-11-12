---
title: "AutoExplode Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AutoExplode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.html"
---

# AutoExplode Method (IAssemblyDoc)

Automatically generates an exploded view of the current assembly configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function AutoExplode() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.AutoExplode()
```

### C#

```csharp
System.bool AutoExplode()
```

### C++/CLI

```cpp
System.bool AutoExplode();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the exploded view is automatically generated, false if not

## VBA Syntax

See [AssemblyDoc::AutoExplode](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AutoExplode.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Insert Explode Line Sketch and Route Line (VB.NET)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VBNET.htm)
[Insert Explode Line Sketch and Route Line (VBA)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VB.htm)
[Insert Explode Line Sketch and Route Line (C#)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_CSharp.htm)

## Remarks

This method creates only one exploded view per assembly configuration. To create multiple exploded views, use [IAssemblyDoc::CreateExplodedView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~CreateExplodedView.html).

It is difficult to get the exploded view perfect without some user interaction. However, this method makes an attempt based on the current mate conditions.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewConfigurationName.html)
[IAssemblyDoc::GetExplodedViewCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount2.html)
[IAssemblyDoc::GetExplodedViewNames2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames2.html)
[IAssemblyDoc::ShowExploded2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.html)
[IAssemblyDoc::ViewCollapseAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.html)
[IAssemblyDoc::ViewExplodeAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.html)
[IModelDocExtension::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsExploded.html)
[ISketchManager::InsertExplodeLineSketch Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertExplodeLineSketch.html)
[IView::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsExploded.html)
[IView::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowExploded.html)
[IConfiguration::AddRadialExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep.html)
[IConfiguration::AddExplodeStep2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep2.html)
