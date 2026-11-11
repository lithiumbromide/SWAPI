---
title: "GetModel Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetModel"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetModel.html"
---

# GetModel Method (IDocument)

Gets the model for the document.

## Syntax

### Visual Basic

```vb
Function GetModel() As Model
```

### C#

```csharp
Model GetModel()
```

### JScript

```
function GetModel() : Model;
```

### Managed Extensions for C++

```
Model* GetModel();
```

### C++/CLI

```cpp
Model^ GetModel();
```

### Return Value

[Model](Interop.dsAutomation~Interop.dsAutomation.IModel.html)

## Examples

This code snippet shows how to get the IModel object.

##### COM native C++

IDocumentPtr dsDoc (pConnection->GetActiveDocument());
if(dsDoc == NULL)
{
return;
}
IModelPtr dsModel( dsDoc->GetModel() );
if(NULL == dsModel)
{
return;
}

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)
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

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight V1R1
