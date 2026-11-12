---
title: "Custom Check Document (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "dsgnchkapi/Custom_Check_Document_Example_VB.htm"
---

# Custom Check Document (VBA)

This example shows how to find out if an isometric view exists within a drawing document using SOLIDWORKS Design Checker Custom Check.

To run this macro, register the macro in SOLIDWORKS Design Checker Custom Check, then check an active drawings document using SOLIDWORKS Design Checker and the standards file in which the macro was stored.

```vb
'--------------------------------------
Dim nFailedItemCount As Integer
Dim bCheckStatus As Boolean
Dim swApp As SldWorks.SldWorks
Dim errorCode As Long

Sub Validate()

Set swApp = Application.SldWorks

' Validate document
bCheckStatus = True

Dim FailedItemsArr() As String
bCheckStatus = RunCheck(FailedItemsArr)

' Inform SOLIDWORKS Design Checker about the results
Dim dcApp As DesignCheckerLib.SWDesignCheck

' Get the SOLIDWORKS Design Checker add-in
 ' Recommended to use the version-specific ProgID for your version of Design Checker
 ' e.g., "SWDesignChecker.SWDesignCheck.yyyy"
 ' See the Remarks section in ISWDesignCheck help
Set dcApp = swApp.GetAddInObject("SWDesignChecker.SWDesignCheck")
errorCode = dcApp.SetCustomCheckResult(bCheckStatus, (FailedItemsArr))

End Sub

Function RunCheck(ByRef FailedItemsArr() As String) As Boolean

Dim Part As ModelDoc2
Dim pViews() As View
Dim SheetNames() As String
Dim CurrentActiveSheet As Sheet
Dim strCurrentActiveSheet As String
Dim strIsometric As String

' Every view's orientation is compared with *Isometric
strIsometric = "*Isometric"

On Error GoTo ON_ERROR
RunCheck = True ' Set check to passed state
nFailedItemCount = 0

Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc

Dim eDocType As swDocumentTypes_e
eDocType = Part.GetType
If eDocType = swDocDRAWING Then
    Dim pDrawingDoc As DrawingDoc
    Set pDrawingDoc = Part
    Dim pView As View

    ' Remember current active sheet's name to activate it again later
    Dim strOriginallyActiveSheet As String
    Set CurrentActiveSheet = pDrawingDoc.GetCurrentSheet
    strOriginallyActiveSheet = CurrentActiveSheet.GetName

    ' Get sheet count
    Dim nSheetCount As Integer
    nSheetCount = pDrawingDoc.GetSheetCount

    ' Set size of the array
    ReDim Preserve SheetNames(nSheetCount) As String

    ' Activate first sheet
    Dim isFirstSheet As Boolean
    isFirstSheet = False
    While isFirstSheet = False
        Set CurrentActiveSheet = pDrawingDoc.GetCurrentSheet
        strCurrentActiveSheet = CurrentActiveSheet.GetName

        pDrawingDoc.SheetPrevious
        Dim PrevSheet As Sheet
        Dim strPrevSheet As String
        Set PrevSheet = pDrawingDoc.GetCurrentSheet
        strPrevSheet = PrevSheet.GetName

        If strPrevSheet = strCurrentActiveSheet Then
            isFirstSheet = True
        End If
    Wend

    ' Loop through all sheets
    If nSheetCount > 0 Then
        Dim nCount As Integer
        For nCount = 1 To nSheetCount
            Set CurrentActiveSheet = pDrawingDoc.GetCurrentSheet
            strCurrentActiveSheet = CurrentActiveSheet.GetName
            SheetNames(nSheetCount) = strCurrentActiveSheet
            Debug.Print strCurrentActiveSheet

            ' Variable to track if any *Isometric view found in sheet
            Dim IsIsometricViewPresent As Boolean
            ' Set to not found
            IsIsometricViewPresent = False

            ' Loop through all views
            Dim nViewCount As Integer
            nViewCount = 0
            Dim pTempView As View
            Set pTempView = pDrawingDoc.GetFirstView

            While (Not pTempView Is Nothing)
                nViewCount = nViewCount + 1
                ReDim Preserve pViews(nViewCount)
                Set pViews(nViewCount) = pTempView

                ' Validate view
                ' Check if *Isometric view is found
                Dim strViewOrientation As String
                strViewOrientation = pViews(nViewCount).GetOrientationName
                If strViewOrientation = strIsometric Then
                    IsIsometricViewPresent = True
                End If
                Debug.Print pViews(nViewCount).GetOrientationName

                Set pTempView = pTempView.GetNextView
            Wend ' End Loop (While pTempView <> Nothing)

            ' If *Isometric view is not found, then add sheet's name to failed items list
            If IsIsometricViewPresent = False Then
                ' Redimension failed item array to accommodate the new item
                nFailedItemCount = nFailedItemCount + 1
                ReDim Preserve FailedItemsArr(1 To 2, 1 To nFailedItemCount) As String

                ' Add failed entity name and its type to array
                ' With these two pieces of information, the failed entity should be highlighted
                ' NOTE: If you don't add entity type (e.g., "SHEET" in this case), then the entity cannot be highlighted
                ' Also, if you give the wrong entity type, then the entity cannot be highlighted
                ' Refer to swSelectType_e in SOLIDWORKS API Help to find the correct entity type
                FailedItemsArr(1, nFailedItemCount) = strCurrentActiveSheet
                FailedItemsArr(2, nFailedItemCount) = "SHEET"
            End If

            pDrawingDoc.SheetNext
        Next nCount ' End Loop (For nCount = 1 To nSheetCount)
    End If ' End condition (If nSheetCount > 0)
End If ' End condition (If eDocType = swDocDRAWING)

' Set Check status
If nFailedItemCount > 0 Then
    RunCheck = False
End If

pDrawingDoc.ActivateSheet (strOriginallyActiveSheet)

Exit Function

ON_ERROR:
Debug.Print "Check failed to execute."

End Function
```
