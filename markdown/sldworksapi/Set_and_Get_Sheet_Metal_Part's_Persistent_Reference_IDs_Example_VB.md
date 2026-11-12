---
title: "Set and Get Sheet Metal Part's Persistent Reference IDs Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VB.htm"
---

# Set and Get Sheet Metal Part's Persistent Reference IDs Example (VBA)

This example shows how to set and get persistent reference IDs (PIDs) on a sheet metal part.

The entities in flattened and unflattened (folded) states of sheet metal in SOLIDWORKS Design do not have the same properties, making it difficult to track entities across states of sheet metal.

- [IModelDocExtension::GetFlattenSheetMetalPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetFlattenSheetMetalPersistReference.html) returns a PID array for an entity in the flattened state of the sheet metal part.
- [IModelDocExtension::GetSheetmetalObjectsByPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSheetMetalObjectsByPersistReference.html) uses the PID byte array to retrieve an array of objects that comprise the previously selected entity in the folded state of the part.

Together these methods provide a way to track entities across sheet metal states.

```
'------------------------------------------
' Preconditions:
' 1. Verify that specified part exists.
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
' do not save changes.
'--------------------------------------------
```

```
Option Explicit
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelectionMgr As SldWorks.SelectionMgr
    Dim swFace As SldWorks.Face2
    Dim swSelectData As SldWorks.SelectData
    Dim pid As Variant
    Dim selObj As Object
    Dim swObjList As Variant
    Dim errors As Long
    Dim warnings As Long
    Dim boolstatus As Boolean
    Dim i As Long
    Dim j As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open part document
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.sldprt", swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    ' Get flat-pattern feature
    Set swModelDocExt = swModel.Extension
    boolstatus = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
```

```
    ' Unsuppress (unfold) flat-pattern feature
    boolstatus = swModel.EditUnsuppress2
```

```
    ' Select the top face on the flattened sheet metal part
    boolstatus = swModelDocExt.SelectByID2("", "FACE", -3.46526388559596E-02, 0, 0.011695220708134, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFace = swSelectionMgr.GetSelectedObject6(1, -1)
```

```
    ' Get the persistent reference IDs for the
    ' the selected face on the flattened sheet
    ' metal part
    pid = swModelDocExt.GetFlattenSheetMetalPersistReference(swFace)
```

```
    ' Print the PID values to the Immediate window
    j = 0
    For j = LBound(pid) To UBound(pid)
        Debug.Print ("PID = " & pid(j))
    Next j
```

```
    ' Suppress (fold) flat-pattern feature
    boolstatus = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    swModel.EditSuppress2
```

```
    ' Use the persistent reference IDs to
    ' retrieve and highlight an array of objects
    ' that comprise the previously selected entity in
    ' the folded state of the part
    swObjList = swModelDocExt.GetSheetMetalObjectsByPersistReference((pid), errors)
```

```
    If Not (IsEmpty(swObjList)) Then
        swModel.ClearSelection2 (True)
        For i = LBound(swObjList) To UBound(swObjList)
            Set selObj = swObjList(i)
            If selObj Is Nothing Then
                Debug.Print "PID conversion error."
                Exit Sub
            Else
                SelectObject selObj, True
            End If
        Next i
    End If
```

```
    Debug.Print "The entities that comprise the previously selected entity in the folded state are selected."
```

```
End Sub
```

```
    Private Sub SelectObject(selObj As Object, append As Boolean)
        If TypeOf selObj Is SldWorks.Entity Then
            Set swSelectData = swSelectionMgr.CreateSelectData
            selObj.Select4 append, swSelectData
        Else
            Debug.Print ("Need selection handle.")
        End If
```

```
    End Sub
```
