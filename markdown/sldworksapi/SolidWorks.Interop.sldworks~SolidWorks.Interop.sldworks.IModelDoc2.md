---
title: "IModelDoc2 Interface"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html"
---

# IModelDoc2 Interface

Allows access to SOLIDWORKS documents: parts, assemblies, and drawings.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
```

### C#

```csharp
public interface IModelDoc2
```

### C++/CLI

```cpp
public interface class IModelDoc2
```

## VBA Syntax

See [ModelDoc2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2.html).

## Examples

[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Get Names of Creators of Features (C++)](Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm)
[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)
[Create Equation-driven Curve (VBA)](Create_Extruded_Thin_Feature_Example_VB.htm)

## Remarks

There are three main SOLIDWORKS document types:

- parts
- assemblies
- drawings

Each document type has its own object ([IPartDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html), [IAssemblyDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc.html), and [IDrawingDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc.html)) with its own set of related functions. For example, the [IAssemblyDoc::AddComponent4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddComponent4.html) method exists on the IAssemblyDoc object because adding components is specific to assembly documents.

The SOLIDWORKS API also has functions that are common to all document types. For example, printing, saving, or determining the file name associated with a document would be common operations. To expose common document-level functions, the SOLIDWORKS API uses the IModelDoc2 object.

## Accessors

[IAssemblyDoc::GetEditTarget](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetEditTarget.html) and [IAssemblyDoc::IGetEditTarget2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetEditTarget2.html)

[IComponent2::GetModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetModelDoc2.html)

[IConfigurationManager::Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager~Document.html)

[IEnumDocuments2::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDocuments2~Next.html)

[IFeatureManager::Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~Document.html)

[IMirrorPartFeatureData::GetModelDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData~GetModelDoc.html)

[IModelDoc2::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetNext.html) and [IModelDoc2::IGetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetNext.html)

[IModelDocExtension::Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~Document.html)

[IModelViewManager::Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~Document.html)

[IModelWindow::ModelDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelWindow~ModelDoc.html)

[IPartDoc::MirrorPart2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~MirrorPart2.html)

[ISketchManager::Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~Document.html)

[ISldWorks::ActivateDoc3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActivateDoc3.html) and [ISldWorks::IActivateDoc3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActivateDoc3.html)

[ISldWorks::ActiveDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActiveDoc.html) and [ISldWorks::IActiveDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActiveDoc2.html)

[ISldWorks::GetFirstDocument](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetFirstDocument.html) and [ISldWorks::IGetFirstDocument2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)

[ISldWorks::GetOpenDocument](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetOpenDocument.html)

[ISldWorks::GetOpenDocumentByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html) and [ISldWorks::IGetOpenDocumentByName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html)

[ISldWorks::INewDocument2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~INewDocument2.html)

[ISldWorks::LoadFile4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~LoadFile4.html)

[ISldWorks::NewDocument](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~NewDocument.html)

[ISldWorks::OpenDoc7](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc7.html)

[IView::ReferencedDocument](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~ReferencedDocument.html)

## Access Diagram

[ModelDoc2](SWObjectModel.pdf#ModelDoc2)

## See Also

[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
