---
title: "IBlockDefinition Interface"
project: ""
interface: "IBlockDefinition"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html"
---

# IBlockDefinition Interface

Allows access to a Block definition.

## Syntax

### Visual Basic

```vb
Public Interface IBlockDefinition
```

### C#

```csharp
public interface IBlockDefinition
```

### JScript

```
public interface IBlockDefinition
```

### Managed Extensions for C++

```
public __gc __interface IBlockDefinition
```

### C++/CLI

```cpp
public interface class IBlockDefinition
```

## Examples

This code snippet shows how to write the names of the Block definitions to a file.

##### COM native C++

void CAddinDumpManager::DumpBlockDefinitions( CStdioFile& fileOutput, LPCWSTR tabStr, IDocumentPtr dsDoc )
{
CString strPrint;

_variant_t pVariantArray = dsDoc->GetBlockDefinitions();
if( V_VT( &pVariantArray ) != VT_EMPTY )
{
IBlockDefinitionPtr *blkDefs = NULL;
int countOfBlockDefs = 0;
[TypeConverter::convertVariantArrayToPtrArray](GettingStarted-draftsightapi.html#convertVariantArrayToPtrArray)<IBlockDefinitionPtr, IBlockDefinition>( pVariantArray, blkDefs, countOfBlockDefs );

strPrint.Format( L"Block definitions (%d):\r\n", countOfBlockDefs );
fileOutput.WriteString( strPrint );

if( blkDefs && countOfBlockDefs > 0)
{
for( int i = 0; i < countOfBlockDefs; ++i )
{
bstr_t BLockName= blkDefs[i]->GetName();
strPrint.Format(L"Block definition name: %s\r\n", BLockName.operator const wchar_t*());
fileOutput.WriteString(strPrint);

CAddinDumpManager::DumpAttributeDefinitions( fileOutput, L"", blkDefs[i] );

CAddinDumpManager::DumpBlockInstances( fileOutput, L"\t", blkDefs[i] );

}
delete[] blkDefs;
}
}
else
fileOutput.WriteString( L"ERROR GetBlockDefinitions\r\n" );
}

## Examples

[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)

## Accessors

[IBlockInstance::GetBlockDefinition](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetBlockDefinition.html)

[IDocument::CreateBlockDefinition](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateBlockDefinition.html)

[IDocument::GetBlockDefinition](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBlockDefinition.html)

[IDocument::GetBlockDefinitions](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBlockDefinitions.html)

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[IExternalReference::GetBlockDefinition](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~GetBlockDefinition.html)

## Access Diagram

DSObjectModel.pdf#BlockDefinition

[BlockDefinition](DSObjectModel.pdf#BlockDefinition)

## See Also

[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
