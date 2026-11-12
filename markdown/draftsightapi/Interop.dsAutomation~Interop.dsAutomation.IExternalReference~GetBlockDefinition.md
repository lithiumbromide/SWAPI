---
title: "GetBlockDefinition Method (IExternalReference)"
project: ""
interface: "IExternalReference"
member: "GetBlockDefinition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExternalReference~GetBlockDefinition.html"
---

# GetBlockDefinition Method (IExternalReference)

Gets a Block definition in the external reference.

## Syntax

### Visual Basic

```vb
Function GetBlockDefinition() As BlockDefinition
```

### C#

```csharp
BlockDefinition GetBlockDefinition()
```

### JScript

```
function GetBlockDefinition() : BlockDefinition;
```

### Managed Extensions for C++

```
BlockDefinition* GetBlockDefinition();
```

### C++/CLI

```cpp
BlockDefinition^ GetBlockDefinition();
```

### Return Value

[Block definition](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)

## Examples

This code snippet shows how to get the names of the Block definitions in the drawing's external references.

##### COM native C++

void CAddinDumpManager::DumpXREFs( CStdioFile& fileOutput, LPCWSTR tabStr, IDocumentPtr dsDoc )
{
CString strPrint;

_variant_t pVariantArray = dsDoc->GetExternalReferences();
if( V_VT( &pVariantArray ) != VT_EMPTY )
{
IExternalReferencePtr *ExtRef = NULL;
int countOfExtRef = 0;
[TypeConverter::convertVariantArrayToPtrArray](GettingStarted-draftsightapi.html#convertVariantArrayToPtrArray)<IExternalReferencePtr, IExternalReference>( pVariantArray, ExtRef, countOfExtRef );

strPrint.Format( L"External references (%d):\r\n", countOfExtRef );
fileOutput.WriteString( strPrint );

if( ExtRef && countOfExtRef > 0)
{
for( int i = 0; i < countOfExtRef; ++i )
{
IBlockDefinitionPtr blkDefs = ExtRef[i]->GetBlockDefinition();
if( !blkDefs )
continue;

bstr_t BLockName= ExtRef[i]->GetName();
strPrint.Format( L"Block definition name: %s\r\n", BLockName.operator const wchar_t*() );
fileOutput.WriteString( strPrint );
}
delete[] ExtRef;
}
}
else
fileOutput.WriteString( L"ERROR GetExternalReferences\r\n" );
}

## See Also

[IExternalReference Interface](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html)
[IExternalReference Members](Interop.dsAutomation~Interop.dsAutomation.IExternalReference_members.html)

## Availability

DraftSight V1R1
