---
title: "IModel Interface"
project: ""
interface: "IModel"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModel.html"
---

# IModel Interface

Allows access to a model.

## Syntax

### Visual Basic

```vb
Public Interface IModel
```

### C#

```csharp
public interface IModel
```

### JScript

```
public interface IModel
```

### Managed Extensions for C++

```
public __gc __interface IModel
```

### C++/CLI

```cpp
public interface class IModel
```

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
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)
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

## Accessors

[IBlockInstance::GetWorkingSpace](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetWorkingSpace.html)

[IDocument::GetModel](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetModel.html)

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

## Access Diagram

DSObjectModel.pdf#Model

[Model](DSObjectModel.pdf#Model)

## See Also

[IModel Members](Interop.dsAutomation~Interop.dsAutomation.IModel_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IViewTile Interface](Interop.dsAutomation~Interop.dsAutomation.IViewTile.html)
