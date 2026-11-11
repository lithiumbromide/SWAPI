---
title: "GetSketchManager Method (ISheet)"
project: ""
interface: "ISheet"
member: "GetSketchManager"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheet~GetSketchManager.html"
---

# GetSketchManager Method (ISheet)

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

This code snippet shows how to get the Sheets, their names, and the bounding box coordinates.

##### COM native C++

void CAddinDumpManager::DumpSheets( CStdioFile& fileOutput, LPCWSTR tabStr, IDocumentPtr dsDoc )
{
CString strPrint;
_variant_t pVariantArray = dsDoc->GetSheets();
if( V_VT( &pVariantArray ) != VT_EMPTY )
{
ISheetPtr *sheets = NULL;
int count = 0;
[TypeConverter::convertVariantArrayToPtrArray](GettingStarted-draftsightapi.html#convertVariantArrayToPtrArray)<ISheetPtr, ISheet>( pVariantArray, sheets, count );

strPrint.Format( L"Sheets: (%d):\r\n", count );
fileOutput.WriteString( strPrint );

if( sheets && count > 0 )
{
//Iterate through Block instances
for( int i = 0; i < count; ++i )
{
//Get Sheet name
bstr_t SheetName= sheets[i]->GetName();

strPrint.Format( L"Name: %s\r\n", SheetName.operator const wchar_t*() );
fileOutput.WriteString( strPrint );

//Get ISketchManager object
ISketchManagerPtr dsSketchManagerSheet( sheets[i]->GetSketchManager() );
if( dsSketchManagerSheet != NULL )
{
//Get Sheet bounding box
double x1, y1, z1, x2, y2, z2;
dsSketchManagerSheet->GetBoundingBox( &x1, &y1, &z1, &x2, &y2, &z2 );

strPrint.Format( L"Bounding box: %.4f %.4f %.4f %.4f\r\n", x1, y1, x2, y2 );
fileOutput.WriteString( strPrint );
}
else
fileOutput.WriteString( L"ERROR GetSketchManager\r\n" );
}
delete[] sheets;
}
}
else
fileOutput.WriteString( L"ERROR GetSheets\r\n" );
}

## See Also

[ISheet Interface](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
[ISheet Members](Interop.dsAutomation~Interop.dsAutomation.ISheet_members.html)

## Availability

DraftSight V1R1
