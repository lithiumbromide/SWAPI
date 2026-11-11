---
title: "GetSelectionManager Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetSelectionManager"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSelectionManager.html"
---

# GetSelectionManager Method (IDocument)

Gets the interface for selecting entities, which makes the currently and previously selected entity available.

## Syntax

### Visual Basic

```vb
Function GetSelectionManager() As SelectionManager
```

### C#

```csharp
SelectionManager GetSelectionManager()
```

### JScript

```
function GetSelectionManager() : SelectionManager;
```

### Managed Extensions for C++

```
SelectionManager* GetSelectionManager();
```

### C++/CLI

```cpp
SelectionManager^ GetSelectionManager();
```

### Return Value

[ISelectionManager](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)

## Examples

This code snippet shows how to get an ISelectionManager object.

##### COM native C++

ISelectionManagerPtr dsSelManager( dsDoc->GetSelectionManager() );
if( NULL == dsSelManager )
{
::AfxMessageBox( L"Failed to get Selection Manager of the current document." );

return;

}

## Examples

[Insert SimpleNote (C#)](Insert_SimpleNote_Example_CSharp.htm)
[Insert SimpleNote (VB.NET)](Insert_SimpleNote_Example_VBNET.htm)
[Insert SimpleNote (VBA)](Insert_SimpleNote_Example_VBA.htm)
[Insert Hatch (JavaScript)](Insert_Hatch_Example_JS.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight V1R1
