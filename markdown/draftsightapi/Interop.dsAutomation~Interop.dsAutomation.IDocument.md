---
title: "IDocument Interface"
project: ""
interface: "IDocument"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument.html"
---

# IDocument Interface

Allows access to a document.

## Syntax

### Visual Basic

```vb
Public Interface IDocument
```

### C#

```csharp
public interface IDocument
```

### JScript

```
public interface IDocument
```

### Managed Extensions for C++

```
public __gc __interface IDocument
```

### C++/CLI

```cpp
public interface class IDocument
```

## Examples

This code snippet shows how to get the active document.

##### COM native C++

//Get active document

CComQIPtr<IDocument> m_DsActiveDoc;

m_DsActiveDoc = m_DsApp->GetActiveDocument();

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)
[Get and Set Document Settings (C#)](Get_and_Set_Document_Settings_Example_CSharp.htm)
[Get and Set Document Settings (VB.NET)](Get_and_Set_Document_Settings_Example_VBNET.htm)
[Get and Set Document Settings (VBA)](Get_and_Set_Document_Settings_Example_VBA.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)
[Get and Set Print Options (C#)](Get_and_Set_Print_Options_Example_CSharp.htm)
[Get and Set Print Options (VB.NET)](Get_and_Set_Print_Options_Example_VBNET.htm)
[Get and Set Print Options (VBA)](Get_and_Set_Print_Options_Example_VBA.htm)
[Switch Layouts (C#)](Switch_Layouts_Example_CSharp.htm)
[Switch Layouts (VB.NET)](Switch_Layouts_Example_VBNET.htm)
[Switch Layouts (VBA)](Switch_Layouts_Example_VBA.htm)
[Insert Lines and Angular Dimension (JavaScript)](Insert_Lines_and_Angular_Dimension_Example_JS.htm)
[Create Circles on Different Layers (JavaScript)](Create_Circles_on_Different_Layers_Example_JS.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)
[Insert Splines (JavaScript)](Insert_Splines_Example_JS.htm)
[Insert HyperLink (JavaScript)](Insert_HyperLink_Example_JS.htm)
[Insert and Dimension Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)
[Mirror Entities (JavaScript)](Mirror_Entities_Example_JS.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)
[Insert Hatch (JavaScript)](Insert_Hatch_Example_JS.htm)
[Create Model and Sheet Views (JavaScript)](Create_Model_and_Sheet_Views_Example_JS.htm)

## Accessors

[IApplication::GetActiveDocument](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetActiveDocument.html)

[IApplication::GetDocuments](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetDocuments.html)

[IApplication::NewDocument](Interop.dsAutomation~Interop.dsAutomation.IApplication~NewDocument.html)

[IApplication::OpenDocument2](Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenDocument2.html)

[IApplication::Recover](Interop.dsAutomation~Interop.dsAutomation.IApplication~Recover.html)

## Access Diagram

DSObjectModel.pdf#Document

[Document](DSObjectModel.pdf#Document)

## See Also

[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument Event DestroyNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_DestroyNotifyEventHandler.html)
[IDocument Event FileSavePostNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileSavePostNotifyEventHandler.html)
[IDocument Event FileSavePreNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileSavePreNotifyEventHandler.html)
[IDocument Event ModifyNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ModifyNotifyEventHandler.html)
