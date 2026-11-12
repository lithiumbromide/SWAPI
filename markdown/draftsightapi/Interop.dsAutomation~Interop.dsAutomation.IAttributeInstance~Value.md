---
title: "Value Property (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "Value"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Value.html"
---

# Value Property (IAttributeInstance)

Gets or sets the value of the BlockAttribute instance.

## Syntax

### Visual Basic

```vb
Property Value As System.String
```

### C#

```csharp
System.string Value {get; set;}
```

### JScript

```
function get,set Value : System.String
```

### Managed Extensions for C++

```
__property System.string* get_Value();
__property void set_Value(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ Value {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Value of the BlockAttribute instance

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

[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)

## See Also

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)

## Availability

DraftSight V1R1
