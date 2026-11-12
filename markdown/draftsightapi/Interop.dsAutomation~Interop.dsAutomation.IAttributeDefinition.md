---
title: "IAttributeDefinition Interface"
project: ""
interface: "IAttributeDefinition"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html"
---

# IAttributeDefinition Interface

Allows access to a BlockAttribute definition.

## Syntax

### Visual Basic

```vb
Public Interface IAttributeDefinition
```

### C#

```csharp
public interface IAttributeDefinition
```

### JScript

```
public interface IAttributeDefinition
```

### Managed Extensions for C++

```
public __gc __interface IAttributeDefinition
```

### C++/CLI

```cpp
public interface class IAttributeDefinition
```

## Examples

This code snippet shows how to get the captions, names, and values of the BlockAttribute definitions.

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

This code snippet shows how to get a BlockAttribute definition, if the selected object is an IAttributeDefinition object.

##### COM native C++

long selCount = dsSelManager->GetSelectedObjectCount( dsSelectionSetType_Current );
strPrint.Format( L"Selected objects: (%d):\r\n", selCount );
fileOutput.WriteString( strPrint );

if( selCount > 0 )
{
for( long i = 0; i < selCount; ++i )
{
dsObjectType_e retObjType;
IDispatchPtr selObj = dsSelManager->GetSelectedObject( dsSelectionSetType_Current, i, &retObjType );

//If selected object is a BlockAttribute definition
if( dsAttributeDefinitionType == retObjType )
{

IAttributeDefinitionPtr AttDefs( selObj );

. . .

## Examples

[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)

## Accessors

[IBlockDefinition::GetAttributeDefinitions](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetAttributeDefinitions.html)

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISketchManager::InsertAttributeDefinition](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertAttributeDefinition.html)

## Access Diagram

DSObjectModel.pdf#AttributeDefinition

[AttributeDefinition](DSObjectModel.pdf#AttributeDefinition)

## See Also

[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
