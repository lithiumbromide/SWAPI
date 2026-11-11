---
title: "Name Property (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "Name"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Name.html"
---

# Name Property (IAttributeDefinition)

Gets or sets the BlockAttribute name.

## Syntax

### Visual Basic

```vb
Property Name As System.String
```

### C#

```csharp
System.string Name {get; set;}
```

### JScript

```
function get,set Name : System.String
```

### Managed Extensions for C++

```
__property System.string* get_Name();
__property void set_Name(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the BlockAttribute

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

This code snippet shows how to write the name, caption, and value of the BlockAttribute definition to a file, if the selected object is an IAttributeDefinition object.

##### COM native C++

long selCount = dsSelManager->GetSelectedObjectCount( dsSelectionSetType_Current );
strPrint.Format( L"Selected objects: (%d):\r\n", selCount );
fileOutput.WriteString( strPrint );

if( selCount > 0 )
{
for( long i = 0; i < selCount; ++i )
{
//Get selected object type
dsObjectType_e retObjType;
IDispatchPtr selObj = dsSelManager->GetSelectedObject( dsSelectionSetType_Current, i, &retObjType );

//If selected object is BlockAttribute definition
if( dsAttributeDefinitionType == retObjType )
{
IAttributeDefinitionPtr AttDefs( selObj );

//Get BlockAttribute definition name
bstr_t AttDefName = AttDefs->GetName();

strPrint.Format( L"Attribute definition (%s) \r\n", AttDefName.operator const wchar_t*() );
fileOutput.WriteString( strPrint );

//Get BlockAttribute definition caption
bstr_t AttDefCaption = AttDefs->GetCaption();

strPrint.Format( L"\tCaption: %s\r\n", AttDefCaption.operator const wchar_t*() );
fileOutput.WriteString( strPrint );

strPrint.Format( L"\tName: %s\r\n", AttDefName.operator const wchar_t*() );
fileOutput.WriteString( strPrint );

//Get BlockAttribute definition value
bstr_t AttDefValue = AttDefs->GetValue();

strPrint.Format( L"\tValue: %s\r\n", AttDefValue.operator const wchar_t*() );
fileOutput.WriteString( strPrint );

## Examples

[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)

## See Also

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)

## Availability

DraftSight V1R1
