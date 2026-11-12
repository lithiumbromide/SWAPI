---
title: "GetSketchManager Method (IModel)"
project: ""
interface: "IModel"
member: "GetSketchManager"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModel~GetSketchManager.html"
---

# GetSketchManager Method (IModel)

Gets the sketch interface.

## Syntax

### Visual Basic

```vb
Function GetSketchManager() As SketchManager
```

### C#

```csharp
SketchManager GetSketchManager()
```

### JScript

```
function GetSketchManager() : SketchManager;
```

### Managed Extensions for C++

```
SketchManager* GetSketchManager();
```

### C++/CLI

```cpp
SketchManager^ GetSketchManager();
```

### Return Value

[ISketchManager](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)

## Examples

This code snippet shows how to get the sketch interface.

##### COM native C++

IModelPtr dsModel( dsDoc->GetModel() );

if(NULL == dsModel)
{
return;
}

ISketchManagerPtr dsSketchManager( dsModel->GetSketchManager() );

if(NULL == dsSketchManager)
{
return;
}

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)
[Construct Circle (C#)](Construct_Circle_Example_CSharp.htm)
[Construct Circle (VB.NET)](Construct_Circle_Example_VBNET.htm)
[Construct Circle (VBA)](Construct_Circle_Example_VBA.htm)
[Insert Lines and Angular Dimension (JavaScript)](Insert_Lines_and_Angular_Dimension_Example_JS.htm)
[Create Circles on Different Layers (JavaScript)](Create_Circles_on_Different_Layers_Example_JS.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)
[Insert Splines (JavaScript)](Insert_Splines_Example_JS.htm)
[Insert HyperLink (JavaScript)](Insert_HyperLink_Example_JS.htm)
[Insert and Dimension Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)
[Mirror Entities (JavaScript)](Mirror_Entities_Example_JS.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)
[Insert Hatch (JavaScript)](Insert_Hatch_Example_JS.htm)

## See Also

[IModel Interface](Interop.dsAutomation~Interop.dsAutomation.IModel.html)
[IModel Members](Interop.dsAutomation~Interop.dsAutomation.IModel_members.html)

## Availability

DraftSight V1R1
