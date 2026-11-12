---
title: "IBlockInstance Interface"
project: ""
interface: "IBlockInstance"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html"
---

# IBlockInstance Interface

Allows access to a Block instance.

## Syntax

### Visual Basic

```vb
Public Interface IBlockInstance
```

### C#

```csharp
public interface IBlockInstance
```

### JScript

```
public interface IBlockInstance
```

### Managed Extensions for C++

```
public __gc __interface IBlockInstance
```

### C++/CLI

```cpp
public interface class IBlockInstance
```

## Examples

This code snippet shows how to get the Block instances.

##### COM native C++

_variant_t pVariantArrayBI = blkDefs->GetBlockInstances();
if( V_VT( &pVariantArrayBI ) != VT_EMPTY )
{
IBlockInstancePtr *blkIns = NULL;
int countOfBI = 0;
[TypeConverter::convertVariantArrayToPtrArray](GettingStarted-draftsightapi.html#convertVariantArrayToPtrArray)<IBlockInstancePtr, IBlockInstance>( pVariantArrayBI, blkIns, countOfBI );
}

This code snippet shows how to get the IBlockInstance object if the selected object is an IBlockInstance object.

##### COM native C++

long selCount = dsSelManager->GetSelectedObjectCount( dsSelectionSetType_Current );

if( selCount > 0 )
{
for( long i = 0; i < selCount; ++i )
{
//Get selected object type
dsObjectType_e retObjType;
IDispatchPtr selObj = dsSelManager->GetSelectedObject( dsSelectionSetType_Current, i, &retObjType );

//If selected object is Block instance
if( dsBlockInstanceType == retObjType )
{
IBlockInstancePtr blkIns( selObj );

. . .

This code snippet shows how to insert a Block instance.

##### COM native C++

//Insert the existing Block instance or insert Block instance from a DWG file

bstr_t blockFileName ( L"<`path_and_DWG_file_name_OR_existing_Block_name`>" );

double insertX = 0, insertY = 0, insertZ = 0, scaleX = 1, scaleY = 1, scaleZ = 1, rotation = 0;

BlockInstancePtr blockInstance = sketchMgr->InsertBlock2( blockFileName, insertX, insertY, insertZ, scaleX, scaleY, scaleZ, rotation );

## Examples

[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)
[Insert Block Instance (C#)](Insert_Block_Instance_Example_CSharp.htm)
[Insert Block Instance (VB.NET)](Insert_Block_Instance_Example_VBNET.htm)
[Insert Block Instance (VBA)](Insert_Block_Instance_Example_VBA.htm)
[Insert External Reference (C#)](Insert_External_Reference_Example_CSharp.htm)
[Insert External Reference (VB.NET)](Insert_External_Reference_Example_VBNET.htm)
[Insert External Reference (VBA)](Insert_External_Reference_Example_VBA.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)

## Accessors

[IBlockDefinition::GetBlockInstances](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetBlockInstances.html)

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ILeader::GetBlockAnnotation](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetBlockAnnotation.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::FlatShotByInsertAsBlock](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FlatShotByInsertAsBlock.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertBlock2](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertBlock2.html)

[ISketchManager::InsertExternalReference](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertExternalReference.html)

## Access Diagram

DSObjectModel.pdf#BlockInstance

[BlockInstance](DSObjectModel.pdf#BlockInstance)

## See Also

[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IDrawingSupportFiles::LibraryFilesPath Property ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~LibraryFilesPath.html)
