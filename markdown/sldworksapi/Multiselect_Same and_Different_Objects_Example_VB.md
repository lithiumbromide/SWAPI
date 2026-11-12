---
title: "Multiselect Same and Different Objects Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Multiselect_Same and_Different_Objects_Example_VB.htm"
---

# Multiselect Same and Different Objects Example (VBA)

This example shows how to select multiple faces, multiple edges, and multiple faces and edges.

```
'---------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects and adds three faces to an array of faces.
' 3. Selects and adds two edges to an array of edges.
' 4. Selects one face and three edges and adds them to an
'    array of entities.
' 5. Multiselects each array of faces, edges, and entities.
' 6. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere do not save
' changes.
'---------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim faceArray(2) As SldWorks.Face2
Dim edgeArray(1) As SldWorks.Edge
Dim entitiesArray(3) As SldWorks.Entity
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim nbrSelections As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
```

```
    'Select three faces and add them to an array of faces
    status = swModelDocExt.SelectByID2("", "FACE", 3.39003579642849E-03, 1.65689832048201E-02, 4.60521566345733E-02, False, 0, Nothing, 0)
    Set faceArray(0) = swSelMgr.GetSelectedObject6(1, -1)
    status = swModelDocExt.SelectByID2("", "FACE", -4.64858017755887E-03, 2.99999999999159E-02, -2.13158882201014E-03, False, 0, Nothing, 0)
    Set faceArray(1) = swSelMgr.GetSelectedObject6(1, -1)
    status = swModelDocExt.SelectByID2("", "FACE", -3.10506911185371E-02, 2.99999999999159E-02, -0.016600178364456, False, 0, Nothing, 0)
    Set faceArray(2) = swSelMgr.GetSelectedObject6(1, -1)
    swModel.ClearSelection2 True
```

```
    'Select two edges and them to an array of edges
    status = swModelDocExt.SelectByID2("", "EDGE", -1.03092369793103E-02, 3.04904435424191E-02, 4.57189565300382E-02, False, 0, Nothing, 0)
    Set edgeArray(0) = swSelMgr.GetSelectedObject6(1, -1)
    status = swModelDocExt.SelectByID2("", "EDGE", 4.37175784318242E-02, 3.01364202527452E-02, 0.028332486890065, False, 0, Nothing, 0)
    Set edgeArray(1) = swSelMgr.GetSelectedObject6(1, -1)
    swModel.ClearSelection2 True
```

```
    'Select one face and three edges and add them to an array of entities
    status = swModelDocExt.SelectByID2("", "FACE", -7.25501009526397E-03, 2.99999999999159E-02, -2.36379374842954E-03, False, 0, Nothing, 0)
    Set entitiesArray(0) = swSelMgr.GetSelectedObject6(1, -1)
    status = swModelDocExt.SelectByID2("", "EDGE", 4.35139962395397E-02, 1.48277472299014E-02, 4.62522660892546E-02, False, 0, Nothing, 0)
    Set entitiesArray(1) = swSelMgr.GetSelectedObject6(1, -1)
    status = swModelDocExt.SelectByID2("", "EDGE", 4.41251049156222E-02, -1.80110278279244E-04, 1.39372949385006E-02, False, 0, Nothing, 0)
    Set entitiesArray(2) = swSelMgr.GetSelectedObject6(1, -1)
    status = swModelDocExt.SelectByID2("", "EDGE", 3.03098420922652E-02, 3.54499639115602E-04, 4.58113148115444E-02, False, 0, Nothing, 0)
    Set entitiesArray(3) = swSelMgr.GetSelectedObject6(1, -1)
    swModel.ClearSelection2 True
```

```
    'Multiselect faces, edges, and entities using IModelDocExtension::MultiSelect2
    Debug.Print "Number of selections in:"
    nbrSelections = swModelDocExt.MultiSelect2(faceArray, False, Nothing)
    Debug.Print "  face array: " & nbrSelections
    swModel.ClearSelection2 True
    nbrSelections = swModelDocExt.MultiSelect2(edgeArray, False, Nothing)
    Debug.Print "  edge array: " & nbrSelections
    swModel.ClearSelection2 True
    nbrSelections = swModelDocExt.MultiSelect2(entitiesArray, False, Nothing)
    Debug.Print "  entities (face and edges) array: " & nbrSelections
    swModel.ClearSelection2 True
```

```
End Sub
```
