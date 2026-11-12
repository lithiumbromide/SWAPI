---
title: "Compare Selected Objects and Their Persistent Reference IDs Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_VB.htm"
---

# Compare Selected Objects and Their Persistent Reference IDs Example (VBA)

This example shows how to determine if two selected entities are the same entities and if those entities have the same persistent IDs.

**NOTE**: Using [IModelDocExtension::IsSamePersistentID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsSamePersistentID.html) and [ISldWorks::IsSame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsSame.html) might be helpful when your application is passed two entities that it didn't select, and your application needs to know if they're the same entity.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open a part document and select two different entities
'    (e.g., face, edge, vertex, etc.)
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Compares the selected entities.
' 2. Examine the code and Immediate window.
'----------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim selObj1 As Object
 Dim selObj2 As Object
 Dim selObjPID1 As Variant
 Dim selObjPID2 As Variant

Sub main()

         Set swApp = Application.SldWorks
         Set swModel = swApp.ActiveDoc
         Set swSelMgr = swModel.SelectionManager
         Set swModelDocExt = swModel.Extension

         ' Get the selected objects
         Set selObj1 = swSelMgr.GetSelectedObject6(1, -1)
         Set selObj2 = swSelMgr.GetSelectedObject6(2, -1)

         Debug.Print ("Compare the selected objects:")
         Select Case swApp.IsSame(selObj1, selObj2)
             Case 0
                 Debug.Print ("  Selected objects are not the same.")
             Case 1
                 Debug.Print ("  Selected objects are the same.")
             Case -1
                 Debug.Print ("  Unable to determine if selected objects are the same.")
         End Select

         Debug.Print ("")

         Debug.Print ("Compare the same objects:")
         Select Case swApp.IsSame(selObj1, selObj1)
             Case 0
                 Debug.Print ("  Selected objects are not the same.")
             Case 1
                 Debug.Print ("  Selected objects are the same.")
             Case -1
                 Debug.Print ("  Unable to determine if selected objects are the same.")
         End Select

         Debug.Print ("")

         ' Get the persistent reference IDs of the
         ' selected objects
         selObjPID1 = swModelDocExt.GetPersistReference3(selObj1)
         selObjPID2 = swModelDocExt.GetPersistReference3(selObj2)

         Debug.Print ("Compare the persistent reference IDs of the selected objects:")
         Select Case swModelDocExt.IsSamePersistentID(selObjPID1, selObjPID2)
             Case 0
                 Debug.Print ("  Selected objects do not have the same persistent reference ID.")
             Case 1
                 Debug.Print ("  Selected objects do have the same persistent reference ID.")
             Case -1
                 Debug.Print ("  Unable to determine if the selected objects have the same persistent reference ID.")
         End Select

         Debug.Print ("")

         Debug.Print ("Compare the persistent reference IDs of the same objects:")
         Select Case swModelDocExt.IsSamePersistentID(selObjPID1, selObjPID1)
             Case 0
                 Debug.Print ("  Selected objects do not have the same persistent reference ID.")
             Case 1
                 Debug.Print ("  Selected objects do have the same persistent reference ID.")
             Case -1
                 Debug.Print ("  Unable to determine if the selected objects have the same persistent reference ID.")
         End Select

 End Sub
```
