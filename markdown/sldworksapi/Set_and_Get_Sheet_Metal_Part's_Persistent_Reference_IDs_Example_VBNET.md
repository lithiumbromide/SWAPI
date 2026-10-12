---
title: "Set and Get Sheet Metal Part's Persistent Reference IDs Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VBNET.htm"
---

# Set and Get Sheet Metal Part's Persistent Reference IDs Example (VB.NET)

This example shows how to set and get persistent reference IDs (PIDs) on a sheet metal part.

The entities in flattened and unflattened (folded) states of sheet metal in SOLIDWORKS Design do not have the same properties, making it difficult to track entities across states of sheet metal.

- [IModelDocExtension::GetFlattenSheetMetalPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetFlattenSheetMetalPersistReference.html) returns a PID array for an entity in the flattened state of the sheet metal part.
- [IModelDocExtension::GetSheetmetalObjectsByPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSheetMetalObjectsByPersistReference.html) uses the PID byte array to retrieve an array of objects that comprise the previously selected entity in the folded state of the part.

Together these methods provide a way to track entities across sheet metal states.

```
'------------------------------------------
' Preconditions:
' 1. Verify that the specified part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens specified part document.
' 2. Unsuppresses the Flat-Pattern1 feature.
' 3. Gets the PIDs of the selected face on the
'    Flat-Pattern1 feature.
' 4. Suppresses the Flat-Pattern1 feature.
' 5. Uses the PIDs to retrieve and highlight the
'    array of objects that comprise the previously
'    selected face in the folded state of the part.
' 6. Examine the Immediate window, graphics area, and
'    FeatureManager design tree.
'
' NOTE: Because the part is used elsewhere,
' do not save any changes when closing it.
'--------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swSelectionMgr As SelectionMgr
    Dim swFace As Face2
    Dim swSelectData As SelectData
    Dim pid As Object
    Dim FileName As String
    Dim selObj As Object
    Dim swObjList As Object
    Dim errors As Integer
    Dim warnings As Integer
    Dim boolstatus As Boolean
    Dim i As Integer
    Dim j As Integer

    Sub main()

        ' Open the specified sheet metal part
        FileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.sldprt"
        swModel = swApp.OpenDoc6(FileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        ' Get flat-pattern feature
        swModelDocExt = swModel.Extension
        boolstatus = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)

        ' Unsuppress (unfold) flat-pattern feature
        boolstatus = swModel.EditUnsuppress2

        ' Select the top face on the flattened sheet metal part
        boolstatus = swModelDocExt.SelectByID2("", "FACE", -3.46526388559596E-02, 0, 0.011695220708134, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFace = swSelectionMgr.GetSelectedObject6(1, -1)

        ' Get the persistent reference IDs for the
        ' the selected face on the flattened sheet
        ' metal part
        pid = swModelDocExt.GetFlattenSheetMetalPersistReference(swFace)

        ' Print the PID values to the Immediate window
        j = 0
        For j = LBound(pid) To UBound(pid)
            Debug.Print("PID = " & pid(j))
        Next j

        ' Suppress (fold) flat-pattern feature
        boolstatus = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
        swModel.EditSuppress2()

        ' Use the persistent reference IDs to
        ' retrieve an array of objects that comprise
        ' the previously select entity in the folded state of the part
        swObjList = swModelDocExt.GetSheetmetalObjectsByPersistReference((pid), errors)
        If Not swObjList Is Nothing Then
            swModel.ClearSelection2(True)
            For i = LBound(swObjList) To UBound(swObjList)
                selObj = swObjList(i)
                If selObj Is Nothing Then
                    Debug.Print("PID conversion error.")
                    Exit Sub
                Else
                    SelectObject(selObj, True)
                End If
            Next i
        End If

        Debug.Print("The entities that comprise the previously selected entity in the folded state are selected.")

    End Sub

    Private Sub SelectObject(ByVal selObj As Object, ByVal append As Boolean)
        If TypeOf selObj Is Entity Then
            swSelectData = swSelectionMgr.CreateSelectData
            selObj.Select4(append, swSelectData)
        Else
            Debug.Print("Need selection handle.")
        End If

    End Sub
    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks
End Class
```
