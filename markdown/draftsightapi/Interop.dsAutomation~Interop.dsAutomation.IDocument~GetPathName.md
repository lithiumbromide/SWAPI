---
title: "GetPathName Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetPathName"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetPathName.html"
---

# GetPathName Method (IDocument)

Gets the path and file name of the document.

## Syntax

### Visual Basic

```vb
Function GetPathName() As System.String
```

### C#

```csharp
System.string GetPathName()
```

### JScript

```
function GetPathName() : System.String;
```

### Managed Extensions for C++

```
System.string* GetPathName();
```

### C++/CLI

```cpp
System.String^ GetPathName();
```

### Return Value

Path and file name of the document

## Examples

This code snippet shows how to get the path and file name of the document (from the DraftSight API [COM native C++ template file](GettingStarted-draftsightapi.html) **DsAddinDocument.cpp**).

##### COM native C++

m_sDocName = m_DsDoc->GetPathName();

## Examples

[Get and Set Document Settings (C#)](Get_and_Set_Document_Settings_Example_CSharp.htm)
[Get and Set Document Settings (VB.NET)](Get_and_Set_Document_Settings_Example_VBNET.htm)
[Get and Set Document Settings (VBA)](Get_and_Set_Document_Settings_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight V1R1
