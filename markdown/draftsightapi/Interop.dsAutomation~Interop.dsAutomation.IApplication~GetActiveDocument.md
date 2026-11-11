---
title: "GetActiveDocument Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetActiveDocument"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetActiveDocument.html"
---

# GetActiveDocument Method (IApplication)

Gets the active document.

## Syntax

### Visual Basic

```vb
Function GetActiveDocument() As Document
```

### C#

```csharp
Document GetActiveDocument()
```

### JScript

```
function GetActiveDocument() : Document;
```

### Managed Extensions for C++

```
Document* GetActiveDocument();
```

### C++/CLI

```cpp
Document^ GetActiveDocument();
```

### Return Value

Active [document](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)

## Examples

This code snippet shows how to get the active document.

##### COM native C++

//Get active document
m_DsActiveDoc = m_DsApp->GetActiveDocument();

## Examples

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

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetDocuments Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetDocuments.html)
[IApplication::CloseDocument Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~CloseDocument.html)
[IApplication::OpenDocument Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenDocument.html)

## Availability

DraftSight V1R1
