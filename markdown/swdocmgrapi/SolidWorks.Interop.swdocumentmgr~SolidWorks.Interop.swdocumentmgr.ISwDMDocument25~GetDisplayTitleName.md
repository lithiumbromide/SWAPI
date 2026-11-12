---
title: "GetDisplayTitleName Method (ISwDMDocument25)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument25"
member: "GetDisplayTitleName"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument25~GetDisplayTitleName.html"
---

# GetDisplayTitleName Method (ISwDMDocument25)

Gets the display title name of this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayTitleName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument25
Dim value As System.String

value = instance.GetDisplayTitleName()
```

### C#

```csharp
System.string GetDisplayTitleName()
```

### C++/CLI

```cpp
System.String^ GetDisplayTitleName();
```

### Return Value

Display title name

## VBA Syntax

See [SwDMDocument25::GetDisplayTitleName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument25~GetDisplayTitleName.html).

## Examples

'VB.NET

'----------------------------------------------------------------------------
' Preconditions:

' 1. Read the SOLIDWORKS Document Manager API **Getting Started**
' topic and ensure that the required DLLs are registered.
'
' 2. Copy and paste this code into a VB.NET console application
' in Microsoft Visual Studio.
'
' 3. Add the **SolidWorks.Interop.swdocumentmgr.dll** reference to the project:
' a. Right-click the solution in Solution Explorer.
' b. Click **Add Reference**.
' c. Click **Browse**.
' d. Click:
' `install_dir`**\api\redist\SolidWorks.Interop.swdocumentmgr.dll**
' e. Click **Add.**
' f. Click **Close.**
'
' 4. Substitute `model_path_and_filename` with the path and filename of the model to open.
'
' 5. Substitute `your_license_key` with your SOLIDWORKS Document
' Manager license key.
'
' 6. Open the Immediate window.
'
' Postconditions: Inspect the Immediate window.
'
' **NOTE**: If the model is used elsewhere, do not save changes.
'--------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swdocumentmgr

Imports SolidWorks.Interop.swconst

Imports System.Runtime.InteropServices

Imports System

Partial Class SolidWorksMacro

Sub main()

Dim swClassFact As SwDMClassFactory

Dim swDocMgr As SwDMApplication

Dim swDoc As SwDMDocument25

Dim sLicenseKey As String

sLicenseKey = "your_license_key"

Dim sDocFileName As String

sDocFileName = "model_path_and_filename"

Dim nDocType As Integer

nDocType = SwDmDocumentType.swDmDocumentPart

swClassFact = New SwDMClassFactory

swDocMgr = swClassFact.GetApplication(sLicenseKey)

Dim retval As SwDmDocumentOpenError

swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, False, retval)

Debug.Print("File = " + swDoc.FullName)

Debug.Print("DisplayTitleName = " + swDoc.**GetDisplayTitleName**)

swDoc.CloseDoc

End Sub

''' <summary>

''' The SldWorks swApp variable is pre-assigned for you.

''' </summary>

Public swApp As SldWorks

End Class

## Examples

[Get Display Title Name (C#)](Get_Display_Title_Name_Example_CSharp.htm)

## See Also

[ISwDMDocument25 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument25.html)
[ISwDMDocument25 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument25_members.html)

## Availability

SOLIDWORKS Document Manager API 2020 SP04
