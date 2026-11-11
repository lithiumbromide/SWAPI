---
title: "GetBlockDefinitions Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetBlockDefinitions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBlockDefinitions.html"
---

# GetBlockDefinitions Method (IDocument)

Gets the Block definitions for the document.

## Syntax

### Visual Basic

```vb
Function GetBlockDefinitions() As System.Object
```

### C#

```csharp
System.object GetBlockDefinitions()
```

### JScript

```
function GetBlockDefinitions() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetBlockDefinitions();
```

### C++/CLI

```cpp
System.Object^ GetBlockDefinitions();
```

### Return Value

Array of [Block definitions](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)

## Examples

This code snippet shows how to write the names of the Block definitions to a file.

##### COM native C++

void CAddinDumpManager::DumpBlockDefinitions( CStdioFile& fileOutput, LPCWSTR tabStr, IDocumentPtr dsDoc )
{
CString strPrint;

//Dump block definitions
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

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetBlockDefinition Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBlockDefinition.html)
[IDocument::HasBlockDefinition Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~HasBlockDefinition.html)
[IDocument::CreateBlockDefinition Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateBlockDefinition.html)

## Availability

DraftSight V1R1
