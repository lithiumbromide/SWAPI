---
title: "IAttributeInstance Interface"
project: ""
interface: "IAttributeInstance"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html"
---

# IAttributeInstance Interface

Allows access to a BlockAttribute instance.

## Syntax

### Visual Basic

```vb
Public Interface IAttributeInstance
```

### C#

```csharp
public interface IAttributeInstance
```

### JScript

```
public interface IAttributeInstance
```

### Managed Extensions for C++

```
public __gc __interface IAttributeInstance
```

### C++/CLI

```cpp
public interface class IAttributeInstance
```

## Examples

This code snippet shows how to write the names and values of the BlockAttribute instances to a file.

##### COM native C++

void CAddinDumpManager::DumpAttributeInstances( CStdioFile& fileOutput, LPCWSTR tabStr, IBlockInstancePtr blkIns )
{
CString strPrint;

_variant_t pVariantArrayAI = blkIns->GetAttributeInstances();
if( V_VT( &pVariantArrayAI ) != VT_EMPTY )
{
IAttributeInstancePtr *AttrIns = NULL;
int countOfAI = 0;
[TypeConverter::convertVariantArrayToPtrArray](GettingStarted-draftsightapi.html#convertVariantArrayToPtrArray)<IAttributeInstancePtr, IAttributeInstance>( pVariantArrayAI, AttrIns, countOfAI );

strPrint.Format(L"%sAttribute instances (%d):\r\n", tabStr, countOfAI);
fileOutput.WriteString(strPrint);

if( AttrIns && countOfAI > 0)
{
for( int i = 0; i < countOfAI; ++i )
{
bstr_t AttInstName = AttrIns[i]->GetName();
strPrint.Format( L"%s\tName: %s\r\n", tabStr, AttInstName.operator const wchar_t*() );
fileOutput.WriteString( strPrint );

bstr_t AttInstValue = AttrIns[i]->GetValue();
strPrint.Format( L"%s\tValue: %s\r\n", tabStr, AttInstValue.operator const wchar_t*() );
fileOutput.WriteString( strPrint );
}
delete[] AttrIns;
}
else
{
strPrint.Format( L"%s\tERROR GetAttributeInstances\r\n", tabStr );
fileOutput.WriteString( strPrint );
}
}
else
{
strPrint.Format( L"%s\tERROR GetAttributeInstances\r\n", tabStr );
fileOutput.WriteString( strPrint );
}
}

## Examples

[Get and Set Block Definitions, Block Instances, and Block Attribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)

## Accessors

[IBlockInstance::GetAttributeIntances](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetAttributeInstances.html)

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

## Access Diagram

DSObjectModel.pdf#AttributeInstance

[AttributeInstance](DSObjectModel.pdf#AttributeInstance)

## See Also

[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
