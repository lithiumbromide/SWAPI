---
title: "Change Drafting Standard to Custom Example VB"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Drafting_Standard_to_Custom_Example_VB.htm"
---

# Change Drafting Standard to Custom Example VB

## Change Drafting Standard to Custom Drafting Standard (VBA)

This example shows how to change the drafting standard to a custom drafting standard.

```vb
'-------------------------------------------------
' Preconditions: Model document is open and a
'                SOLIDWORKS-supplied drafting standard is set.
'
' Postconditions: Drafting standard is set to the
'                specified custom drafting standard.
'-------------------------------------------------
Option Explicit

Dim swApp           As SldWorks.SldWorks
Dim swModel         As SldWorks.ModelDoc2
Dim swModExt        As SldWorks.ModelDocExtension
Dim bRetVal         As Boolean
Dim sPath           As String
Dim sFileName       As String
Dim vDSNames        As Variant
Dim i               As Integer

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swModExt = swModel.Extension

'Get current SOLIDWORKS-supplied drafting standard
Debug.Print "Current drafting standard..."
Debug.Print "  (Standard, NoOptionSpecified) before = " & swModExt.GetUserPreferenceInteger(SwConst.swDetailingDimensionStandard, SwConst.swDetailingNoOptionSpecified)
Debug.Print "  (StandardName, NoOptionSpecified) before = " & swModExt.GetUserPreferenceString(SwConst.swDetailingDimensionStandardName, SwConst.swDetailingNoOptionSpecified)
Debug.Print "  "

' Get drafting standard names
' Only the SOLIDWORKS-supplied drafting standards
' are returned; any custom drafting standards are
' not returned
Debug.Print "SOLIDWORKS-supplied drafting standards..."
vDSNames = swModExt.GetDraftingStandardNames
PrintNames vDSNames
Debug.Print "  "

' Load custom drafting standard
bRetVal = swModExt.LoadDraftingStandard("C:\test\MyANSI.sldstd") ' Substitute your custom drafting standard path and filename

' Get custom drafting standard just-specified
Debug.Print "Standard that custom drafting standard is based on or derived from..."
Debug.Print "  (Standard, NoOptionSpecified) after custom loaded = " & swModExt.GetUserPreferenceInteger(SwConst.swDetailingDimensionStandard, SwConst.swDetailingNoOptionSpecified)
Debug.Print "  (StandardName, NoOptionSpecified) after custom loaded = " & swModExt.GetUserPreferenceString(SwConst.swDetailingDimensionStandardName, SwConst.swDetailingNoOptionSpecified)
Debug.Print "  "

' Get drafting standard names
' Remember, only the SOLIDWORKS-supplied drafting standards
' are returned; any custom drafting standards are
' not returned
Debug.Print "SOLIDWORKS-supplied drafting standards..."
vDSNames = swModExt.GetDraftingStandardNames
PrintNames vDSNames
Debug.Print "  "

End Sub

Function PrintNames(ByVal vDSNames As Variant)
For i = LBound(vDSNames) To UBound(vDSNames)
    Debug.Print "  " & vDSNames(i)
Next i
End Function
```
