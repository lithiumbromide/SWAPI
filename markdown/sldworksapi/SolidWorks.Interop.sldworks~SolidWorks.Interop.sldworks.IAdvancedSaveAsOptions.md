---
title: "IAdvancedSaveAsOptions Interface"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html"
---

# IAdvancedSaveAsOptions Interface

Allows access to all **File > Save As** options when saving a SOLIDWORKS Part, Assembly, or Drawing.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IAdvancedSaveAsOptions
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions
```

### C#

```csharp
public interface IAdvancedSaveAsOptions
```

### C++/CLI

```cpp
public interface class IAdvancedSaveAsOptions
```

## VBA Syntax

See [AdvancedSaveAsOptions](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions.html).

## Examples

'VBA

'This example shows how to save a drawing with advanced options.
'--------------------------------------------------------------
' Preconditions:
' 1. Open:
' `public_documents`**\samples\tutorial\advdrawings\foodprocessor.slddrw**
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inspect the Immediate window for the list of reference components,
' before and after name modifications to the drawing and its template.
' 2. Inspect the DrwSavedFolder and Ref sub-folders. In those
' directories, the names of top-level documents are changed to "SamplePart.*".
' The reference component names are changed to include a "Prff_" prefix and
' a "_Suff" suffix.
'
' NOTE: Because the drawing and template are used elsewhere,
' do not save changes.
'--------------------------------------------------------------

Dim swApp As SldWorks.SldWorks
Dim swModel As ModelDoc2
Dim ModelExt As ModelDocExtension

Dim AdvOptData As AdvancedSaveAsOptions
Dim aFileName As String
Dim OrFileName As String
Dim Opt As Long
Dim Error As Long
Dim Warning As Long
Dim Status As Boolean
Dim i As Long
Dim k As Long

Const Suff As String = "_Suff"
Const Prff As String = "Prff_"
Option Explicit

Sub main()

Dim DrwExtArr As Variant
DrwExtArr = Array(".slddrw", ".drwdot")

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set ModelExt = swModel.Extension

OrFileName = Left(swModel.GetPathName(), InStrRev(swModel.GetPathName(), "\"))
Debug.Print OrFileName

Dim IDList As Variant
Dim fileNameList As Variant
Dim pathNameList As Variant

If Dir(OrFileName & "DrwSavedFolder", vbDirectory) = "" Then
MkDir (OrFileName & "DrwSavedFolder")
MkDir (OrFileName & "Ref")
End If

For i = 0 To UBound(DrwExtArr)

aFileName = OrFileName & "DrwSavedFolder\SamplePart" & DrwExtArr(i)
Debug.Print aFileName

Set AdvOptData = ModelExt.**GetAdvancedSaveAsOptions**((1 + 2 + 4))

AdvOptData.**SaveAllAsCopy** = True

'Uncomment below to save model and references as SOLIDWORKS 2020

'AdvOptData.**SaveAsPreviousVersion** = 13000

AdvOptData.**GetItemsNameAndPath** IDList, fileNameList, pathNameList

PrintList fileNameList, pathNameList

AdvOptData.**SetPrefixSuffixToAll** Prff, Suff

AdvOptData.**GetItemsNameAndPath** IDList, fileNameList, pathNameList

For k = 0 To UBound(IDList)

If k = 0 Then ' For setting root folder and root file name
pathNameList(k) = OrFileName & "DrwSavedFolder"
fileNameList(k) = "SamplePart" & DrwExtArr(i)
Else
pathNameList(k) = OrFileName & "Ref"
End If

Next

Error = AdvOptData.**ModifyItemsNameAndPath**(IDList, fileNameList, pathNameList)

Debug.Print "Modify Paths Status : " & Error
Debug.Print " "
AdvOptData.**GetItemsNameAndPath** IDList, fileNameList, pathNameList

PrintList fileNameList, pathNameList

SaveFunctionCall (DrwExtArr(i))

Debug.Print " "

Next

Debug.Print "Total Count " & i

End Sub

Sub SaveFunctionCall(Typ As String)

Opt = (1 + 2)
Debug.Print aFileName
Status = ModelExt.**SaveAs3**(aFileName, 0, Opt, Nothing, AdvOptData, Error, Warning)

Debug.Print "Save Status for Type " & Typ & " is : " & Status & " " & Error & " " & Warning

End Sub

Sub PrintList(sList As Variant, sList2 As Variant)

Dim j As Long

For j = 0 To UBound(sList)

Debug.Print sList(j) & " **>>** " & sList2(j)

Next

Debug.Print "Total Count in the List is : " & j

End Sub

## Accessors

[IModelDocExtension::GetAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAdvancedSaveAsOptions.html)

## Access Diagram

[AdvancedSaveAsOptions](SWObjectModel.pdf#AdvancedSaveAsOptions)

## See Also

[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
