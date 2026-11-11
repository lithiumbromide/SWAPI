---
title: "GetBoundingBox Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "GetBoundingBox"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetBoundingBox.html"
---

# GetBoundingBox Method (ISketchManager)

Gets the bounding box enclosing the sketch entity.

## Syntax

### Visual Basic

```vb
Sub GetBoundingBox( _
   ByRef X1 As System.Double, _
   ByRef Y1 As System.Double, _
   ByRef Z1 As System.Double, _
   ByRef X2 As System.Double, _
   ByRef Y2 As System.Double, _
   ByRef Z2 As System.Double _
)
```

### C#

```csharp
void GetBoundingBox(
   out System.double X1,
   out System.double Y1,
   out System.double Z1,
   out System.double X2,
   out System.double Y2,
   out System.double Z2
)
```

### JScript

```
function GetBoundingBox(
   X1 : System.double,
   Y1 : System.double,
   Z1 : System.double,
   X2 : System.double,
   Y2 : System.double,
   Z2 : System.double
);
```

### Managed Extensions for C++

```
void GetBoundingBox(
   [PARAMFLAG::Out] System.double X1,
   [PARAMFLAG::Out] System.double Y1,
   [PARAMFLAG::Out] System.double Z1,
   [PARAMFLAG::Out] System.double X2,
   [PARAMFLAG::Out] System.double Y2,
   [PARAMFLAG::Out] System.double Z2
)
```

### C++/CLI

```cpp
void GetBoundingBox(
   [Out] System.double X1,
   [Out] System.double Y1,
   [Out] System.double Z1,
   [Out] System.double X2,
   [Out] System.double Y2,
   [Out] System.double Z2
)
```

### Parameters

- `X1`: x coordinate of a corner of the bounding box
- `Y1`: y coordinate of a corner of the bounding box
- `Z1`: z coordinate of a corner of the bounding box
- `X2`: x coordinate of the opposite diagonal corner of the bounding box
- `Y2`: y coordinate of the opposite diagonal corner of the bounding box
- `Z2`: z coordinate of the opposite diagonal corner of the bounding box

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

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1
