---
title: "Add Objects to Selection List Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Objects_to_Selection_List_Example_VBNET.htm"
---

# Add Objects to Selection List Example (VB.NET)

This example shows how to populate the selection list with objects that have not been pre-selected through the user interface.

```vb
  '----------------------------------------------------------------------------
  ' Preconditions:
  ' 1. Open Public_documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\api\multi_local.sldprt.
  ' 2. Open the Immediate window.
  '
  ' Postconditions:
  ' 1. Suspends the selection list containing Sketch2.
  ' 2. Populates another selection list with six sketch objects.
  ' 3. Gets the type of the last object in the selection list.
  ' 4. Appends the last selection list of six objects to the previously suspended
  '       selection list that contains Sketch2, placing Sketch2 at the top of the
  '       combined and resumed selection list.
  ' 5. Places Sketch2 in edit mode.
  ' 6. Inspect the Immediate window and graphics area.
  ' 7. Discard changes to the model.
  '
  ' NOTE: Because the model is used elsewhere, do not save any changes.
  ' ---------------------------------------------------------------------------
  Imports SolidWorks.Interop.sldworks
  Imports SolidWorks.Interop.swconst
  Imports System.Runtime.InteropServices
  Imports System
```

```vb
  Partial   Class   SolidWorksMacro
        Public   Sub main()
```

```vb
            Dim swModel   As   ModelDoc2
            Dim selMgr   As   SelectionMgr
            Dim selData   As   SelectData
            Dim featMgr   As   FeatureManager
            Dim feat   As   Feature
            Dim selObjs()   As   Object
            Dim selObj   As   Object
            Dim featCount   As   Integer
            Dim i   As   Integer
            Dim typeName   As   String
            Dim j   As   Integer
            Dim numAdded   As   Integer
            Dim boolstatus   As   Boolean
            Dim ret   As   Integer
            Dim count   As   Integer
```

```vb
            swModel = swApp.ActiveDoc
            selMgr = swModel.SelectionManager
            selData = selMgr.CreateSelectData
            featMgr = swModel.FeatureManager
```

```vb
            featCount = featMgr.GetFeatureCount(True)
            feat = swModel.FirstFeature
            j = 0
            ReDim selObjs(j + 1)
            For i = 0   To featCount
                If   Not feat   Is   Nothing   Then
```

```vb
                    typeName = feat.Name
                    typeName = UCase(typeName)
                    If   "SKETCH" = Left(typeName, 6)   Then
                        selObjs(j) = feat
                        j = j + 1
                        ReDim   Preserve selObjs(j + 1)
                    End   If
                    feat = feat.GetNextFeature
                End   If
            Next i
```

```vb
          ' Add one object to the current selection list
            boolstatus = swModel.Extension.SelectByID2("Sketch2",   "SKETCH", 0, 0, 0,   False, 0,   Nothing, 0)
```

```vb
            ' Start a new selection list
            ret = selMgr.SuspendSelectionList
            Debug.Print("The current selection list with " & ret    " object (Sketch2) is suspended.")
```

```vb
            ' Add six objects to the new selection list
            numAdded = selMgr.AddSelectionListObjects((selObjs), selData)
            Debug.Print("A new selection list is started.")
```

```vb
            ' Get number of objects in the new selection list (should be 6)
            count = selMgr.GetSelectedObjectCount
            Debug.Print("The selection list now contains " & count    " objects.")
```

```vb
            ' Get the last object in the new selection list
            selObj = selMgr.GetSelectedObject6(count, -1)
            Debug.Print("The last object in the selection list is of swSelectType_e = " & selMgr.GetSelectedObjectType3(count, -1)    ".")
```

```vb
            ' Resume the previously suspended selection list (Sketch2), appending the new selection list to it
            selMgr.ResumeSelectionList2(True)
            Debug.Print("The previous selection list is resumed and appended with the new selection list.")
```

```vb
            ' Get the number of objects in the selection list (should be 7)
            count = selMgr.GetSelectedObjectCount
            Debug.Print("The selection list now contains " & count    " objects, including Sketch2, which is at the top of the selection list.")
```

```vb
            ' Edit sketch2
            swModel.EditSketch()
```

```vb
        End   Sub
        '''   <summary>
        ''' The SldWorks swApp variable is pre-assigned for you.
        '''   </summary>
        Public swApp   As   SldWorks
```

End Class
