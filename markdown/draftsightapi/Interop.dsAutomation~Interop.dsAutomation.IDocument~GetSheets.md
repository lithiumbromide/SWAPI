---
title: "GetSheets Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetSheets"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheets.html"
---

# GetSheets Method (IDocument)

Obsolete. Superseded by [IDocument::GetSheets2.](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheets2.html)

## Syntax

### Visual Basic

```vb
Function GetSheets() As System.Object
```

### C#

```csharp
System.object GetSheets()
```

### JScript

```
function GetSheets() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetSheets();
```

### C++/CLI

```cpp
System.Object^ GetSheets();
```

### Return Value

Array of [Sheets](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)

## Examples

This code snippet shows how to get the Sheets in a document.

##### COM native C++

_variant_t pVariantArray = dsDoc->GetSheets();
if( V_VT( &pVariantArray ) != VT_EMPTY )

{

. . .

}

## Examples

[Switch Layouts (C#)](Switch_Layouts_Example_CSharp.htm)
[Switch Layouts (VB.NET)](Switch_Layouts_Example_VBNET.htm)
[Switch Layouts (VBA)](Switch_Layouts_Example_VBA.htm)
[Create Rectangular Viewport (C#)](Create_Rectangular_Viewport_Example_CSharp.htm)
[Create Rectangular Viewport (VB.NET)](Create_Rectangular_Viewport_Example_VBNET.htm)
[Create Rectangular Viewport (VBA)](Create_Rectangular_Viewport_Example_VBA.htm)
[Create Rectangular Viewport (JavaScript)](Create_Rectangular_Viewport_Example_JS.htm)

## Remarks

The [model](Interop.dsAutomation~Interop.dsAutomation.IModel.html) is the first element in the array. To get the first Sheet in the array, either:

- explicitly get the second element in the array.
- use [ISheet::Name](Interop.dsAutomation~Interop.dsAutomation.ISheet~Name.html) and iterate through the array to get the first element in the array not named **Model**.

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::CopySheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CopySheet.html)
[IDocument::CreateSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheet.html)
[IDocument::CreateSheetByTemplate Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheetByTemplate.html)
[IDocument::GetSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheet.html)
[IDocument::HasSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~HasSheet.html)
[IDocument::RemoveSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~RemoveSheet.html)

## Availability

DraftSight V1R1
