---
title: "Name Property (ISheet)"
project: ""
interface: "ISheet"
member: "Name"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheet~Name.html"
---

# Name Property (ISheet)

Gets or sets the name of the Sheet.

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

Name of the Sheet

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

## Examples

[Switch Layouts (C#)](Switch_Layouts_Example_CSharp.htm)
[Switch Layouts (VB.NET)](Switch_Layouts_Example_VBNET.htm)
[Switch Layouts (VBA)](Switch_Layouts_Example_VBA.htm)
[Create Rectangular Viewport (C#0](Create_Rectangular_Viewport_Example_CSharp.htm)
[Create Rectangular Viewport (VB.NET)](Create_Rectangular_Viewport_Example_VBNET.htm)
[Create Rectangular Viewport (VBA)](Create_Rectangular_Viewport_Example_VBA.htm)
[Create Rectangular Viewport (JavaScript)](Create_Rectangular_Viewport_Example_JS.htm)

## See Also

[ISheet Interface](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
[ISheet Members](Interop.dsAutomation~Interop.dsAutomation.ISheet_members.html)

## Availability

DraftSight V1R1
