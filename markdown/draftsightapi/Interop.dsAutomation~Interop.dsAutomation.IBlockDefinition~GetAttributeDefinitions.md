---
title: "GetAttributeDefinitions Method (IBlockDefinition)"
project: ""
interface: "IBlockDefinition"
member: "GetAttributeDefinitions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetAttributeDefinitions.html"
---

# GetAttributeDefinitions Method (IBlockDefinition)

Gets the BlockAttribute definitions for the Block definition.

## Syntax

### Visual Basic

```vb
Function GetAttributeDefinitions() As System.Object
```

### C#

```csharp
System.object GetAttributeDefinitions()
```

### JScript

```
function GetAttributeDefinitions() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetAttributeDefinitions();
```

### C++/CLI

```cpp
System.Object^ GetAttributeDefinitions();
```

### Return Value

Array of [BlockAttribute definitions](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)

## Examples

This code snippet shows how to write the captions, names, and values of the BlockAttribute definitions to a file.

##### COM native C++

void CAddinDumpManager::DumpAttributeDefinitions( CStdioFile& fileOutput, LPCWSTR tabStr, IBlockDefinitionPtr blkDefs )
{
CString strPrint;

_variant_t pVariantArrayAD = blkDefs->GetAttributeDefinitions();
if( V_VT( &pVariantArrayAD ) != VT_EMPTY )
{
IAttributeDefinitionPtr *blkAttDefs = NULL;
int countOfAttDefs = 0;
[TypeConverter::convertVariantArrayToPtrArray](GettingStarted-draftsightapi.html#convertVariantArrayToPtrArray)<IAttributeDefinitionPtr, IAttributeDefinition>( pVariantArrayAD, blkAttDefs, countOfAttDefs );

strPrint.Format( L"\tAttribute definitions (%d):\r\n", countOfAttDefs );
fileOutput.WriteString( strPrint );

if( blkAttDefs && countOfAttDefs > 0)
{
for( int i = 0; i < countOfAttDefs; ++i )
{
bstr_t AttDefCaption= blkAttDefs[i]->GetCaption();
strPrint.Format( L"\tCaption: %s\r\n", AttDefCaption.operator const wchar_t*() );
fileOutput.WriteString( strPrint );

bstr_t AttDefName= blkAttDefs[i]->GetName();
strPrint.Format( L"\tName: %s\r\n", AttDefName.operator const wchar_t*() );
fileOutput.WriteString(strPrint);

bstr_t AttDefValue= blkAttDefs[i]->GetValue();
strPrint.Format( L"\tValue: %s\r\n", AttDefValue.operator const wchar_t*() );
fileOutput.WriteString( strPrint );

}
delete[] blkAttDefs;
}
else
fileOutput.WriteString( L"\tERROR GetAttributeDefinitions\r\n" );
}
else
fileOutput.WriteString( L"\tERROR GetAttributeDefinitions\r\n" );
}

## Examples

[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)

## See Also

[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)

## Availability

DraftSight V1R1
