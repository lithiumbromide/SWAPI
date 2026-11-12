---
title: "ISheet Interface"
project: ""
interface: "ISheet"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheet.html"
---

# ISheet Interface

Allows access to a Sheet.

## Syntax

### Visual Basic

```vb
Public Interface ISheet
```

### C#

```csharp
public interface ISheet
```

### JScript

```
public interface ISheet
```

### Managed Extensions for C++

```
public __gc __interface ISheet
```

### C++/CLI

```cpp
public interface class ISheet
```

## Examples

This code snippet shows how to get the ID and working space of a Block instance. This code snippet also shows how to determine if the working space is a model or sheet.

##### COM native C++

//Get Block instance ID
bstr_t blkInstanceID = blkIns->GetID();

//Get working space
dsObjectType_e oType;
IDispatch pWorkingSpace;
blkIns->GetWorkingSpace( &oType, &pWorkingSpace );

//If working space is a model
if( dsModelType == oType )
{

IModel modelSpace ( pWorkingSpace );
. . .

}
else
{
//If working space is a sheet
if( dsSheetType == oType )
{
ISheetPtr sheet( pWorkingSpace );

. . .

}

}

##### COM native C++

This code snippet shows how to get the Sheets, their names, and the bounding box coordinates.

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
// Iterate through Block instances
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

[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)
[Switch Layouts (C#)](Switch_Layouts_Example_CSharp.htm)
[Switch Layouts (VB.NET)](Switch_Layouts_Example_VBNET.htm)
[Switch Layouts (VBA)](Switch_Layouts_Example_VBA.htm)
[Create Rectangular Viewport (C#)](Create_Rectangular_Viewport_Example_CSharp.htm)
[Create Rectangular Viewport (VB.NET)](Create_Rectangular_Viewport_Example_VBNET.htm)
[Create Rectangular Viewport (VBA)](Create_Rectangular_Viewport_Example_VBA.htm)
[Create Rectangular Viewport (JavaScript)](Create_Rectangular_Viewport_Example_JS.htm)

## Accessors

[IBlockInstance::GetWorkingSpace](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetWorkingSpace.html)

[IDocument::CopySheet](Interop.dsAutomation~Interop.dsAutomation.IDocument~CopySheet.html)

[IDocument::CreateSheet](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheet.html)

[IDocument::CreateSheetByTemplate](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheetByTemplate.html)

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[IDocument::GetSheet](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheet.html)

[IDocument::GetSheets](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheets.html)

[IExportSettings::Sheets](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~Sheets.html)

[ISheetNamedView::GetSheet](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView~GetSheet.html)

## Access Diagram

DSObjectModel.pdf#Sheet

[Sheet](DSObjectModel.pdf#Sheet)

## See Also

[ISheet Members](Interop.dsAutomation~Interop.dsAutomation.ISheet_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument::RemoveSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~RemoveSheet.html)
[IDocument::HasSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~HasSheet.html)
[ISheet Interface](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
