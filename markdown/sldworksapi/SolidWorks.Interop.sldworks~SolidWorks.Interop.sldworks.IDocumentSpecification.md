---
title: "IDocumentSpecification Interface"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html"
---

# IDocumentSpecification Interface

Allows you to specify how to open a model document. Use this interface's properties before calling [ISldWorks::OpenDoc7](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc7.html) to specify how you want to open a model document.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDocumentSpecification
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
```

### C#

```csharp
public interface IDocumentSpecification
```

### C++/CLI

```cpp
public interface class IDocumentSpecification
```

## VBA Syntax

See [DocumentSpecification](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification.html).

## Examples

See the [IPLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification.html) examples.

## Examples

[Hide All Edges in Drawing View (VBA)](Hide_All_Edges_in_Drawing_View_Example_VB.htm)
[Open Drawing Document Read-only (VBA)](Open_Drawing_Document_Read-only_Example_VB.htm)
[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

## Remarks

The following properties are not valid when opening a 3DEXPERIENCE file using [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm):

- [IDocumentSpecification::FileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~FileName.html)
- [IDocumentSpecification::ConfigurationName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ConfigurationName.html)
- [IDocumentSpecification::DocumentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DocumentType.html)
- [IDocumentSpecification::DisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DisplayState.html)
- [IDocumentSpecification::InteractiveAdvancedOpen](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveAdvancedOpen.html)
- [IDocumentSpecification::InteractiveComponentSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveComponentSelection.html)
- [IDocumentSpecification::LoadExternalReferencesInMemory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LoadExternalReferencesInMemory.html)

## Accessors

[ISldWorks::GetOpenDocSpec](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetOpenDocSpec.html)

## Access Diagram

[DocumentSpecification](SWObjectModel.pdf#DocumentSpecification)

## See Also

[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISldWorks::OpenDoc6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html)
