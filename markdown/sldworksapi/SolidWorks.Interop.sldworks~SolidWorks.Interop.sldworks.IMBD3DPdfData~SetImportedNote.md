---
title: "SetImportedNote Method (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "SetImportedNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetImportedNote.html"
---

# SetImportedNote Method (IMBD3DPdfData)

Sets the specified imported note.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetImportedNote( _
   ByVal Name As System.String, _
   ByVal Note As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim Name As System.String
Dim Note As System.Object
Dim value As System.Boolean

value = instance.SetImportedNote(Name, Note)
```

### C#

```csharp
System.bool SetImportedNote(
   System.string Name,
   System.object Note
)
```

### C++/CLI

```cpp
System.bool SetImportedNote(
   System.String^ Name,
   System.Object^ Note
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the imported note to set (see **Remarks**)
- `Note`: [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)

### Return Value

True if note set successfully, false if not

## VBA Syntax

See [MBD3DPdfData::SetImportedNote](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~SetImportedNote.html).

## Examples

```
'VBA
```

```
'Open a model with two notes.
```

```
'Ensure that the specified theme.xml exists or set IMBD3DPdfData::ThemeName to a standard SOLIDWORKS theme.
```

```
'See IMBD3DPdfData::ThemeName for details.
```

```
'Run the following macro to create MBDPart1.PDF.
```

```
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMBDPdfData As SldWorks.MBD3DPdfData
Dim fileName As String
Dim standardViews As Variant
Dim viewIDs(2) As Long
Dim viewNames(1) As String
Dim status As Long
Dim Vtitle As Variant
Dim swnote1 As SldWorks.Note
Dim swnote2 As SldWorks.Note
Dim boolstatus As Boolean
Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension

    'Get MBD3DPdfData object
    Set swMBDPdfData = swModelDocExt.GetMBD3DPdfData

    'Set path and file name for SOLIDWORKS MBD 3D PDF
    swMBDPdfData.FilePath = swApp.GetCurrentMacroPathFolder + "\MBDPart1.PDF"

    'Display SOLIDWORKS MBD 3D PDF after saving
    swMBDPdfData.ViewPdfAfterSaving = True

    'Set SOLIDWORKS MBD 3D PDF theme
    swMBDPdfData.ThemeName = swApp.GetCurrentMacroPathFolder + "\multipage assembly 1 (a4 landscape)\theme.xml"

    viewIDs(0) = swStandardViews_e.swIsometricView
    standardViews = viewIDs
    swMBDPdfData.SetStandardViews (standardViews)

    Vtitle = swMBDPdfData.GetImportedNotes()

    Debug.Print "Number of imported notes: " & UBound(Vtitle)
    Debug.Print "Names of imported notes in theme.xml: " & Vtitle(0) & "," & Vtitle(1)

    swModel.ClearSelection2 True

    boolstatus = swModel.Extension.SelectByID2("DetailItem1@Annotations", "NOTE", 4.4204917724824E-03, 3.51478241987688E-02, -1.41024939463153E-02, True, 0, Nothing, 0)
    boolstatus = swModel.Extension.SelectByID2("DetailItem2@Annotations", "NOTE", 0.023510157479254, 2.73959875410024E-02, -1.89093669451609E-02, True, 0, Nothing, 0)
```

```
    Set swnote1 = swModel.SelectionManager.GetSelectedObject6(1, -1)
    Set swnote2 = swModel.SelectionManager.GetSelectedObject6(2, -1)

    boolstatus = swMBDPdfData.SetImportedNote(Vtitle(0), swnote1)
    boolstatus = swMBDPdfData.SetImportedNote(Vtitle(1), swnote2)

    'Create SOLIDWORKS MBD 3D PDF
    status = swModelDocExt.PublishTo3DPDF(swMBDPdfData)
    Debug.Print ("Status of publishing part to SOLIDWORKS MBD 3D PDF (0 = success): " & status)

End Sub
```

## Remarks

Use [IMBD3DPdfData::GetImportedNotes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetImportedNotes.html) to get the names of available imported note names you can use to set notes in this PDF.

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
