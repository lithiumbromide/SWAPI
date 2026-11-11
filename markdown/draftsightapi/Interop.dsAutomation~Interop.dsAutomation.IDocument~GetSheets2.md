---
title: "GetSheets2 Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetSheets2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheets2.html"
---

# GetSheets2 Method (IDocument)

Gets the Sheets for the document.

## Syntax

### Visual Basic

```vb
Function GetSheets2() As System.Object
```

### C#

```csharp
System.object GetSheets2()
```

### JScript

```
function GetSheets2() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetSheets2();
```

### C++/CLI

```cpp
System.Object^ GetSheets2();
```

### Return Value

Array of [Sheets](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)

## Examples

This code snippet shows how to get the Sheets in a document.

##### COM native C++

_variant_t pVariantArray = dsDoc->GetSheets2();
if( V_VT( &pVariantArray ) != VT_EMPTY )

{

. . .

}

## Examples

[Activate Sheets (C#)](Activate_Sheets_Example_CSharp.htm)
[Activate Sheets (VB.NET)](Activate_Sheets_Example_VBNET.htm)
[Activate Sheets (VBA)](Activate_Sheets_Example_VBA.htm)

## Remarks

The difference between this method and the now obsolete [IDocument::GetSheets](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheets.html) is that the obsolete method returned the [model](Interop.dsAutomation~Interop.dsAutomation.IModel.html) as the first element in the array. This method returns all of the Sheets in the drawing, excluding the model.

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

DraftSight V1R6.0
