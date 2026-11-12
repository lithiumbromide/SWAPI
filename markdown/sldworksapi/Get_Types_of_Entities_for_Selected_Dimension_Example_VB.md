---
title: "Get Types of Entities Attached to Selected Annotation Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Types_of_Entities_for_Selected_Dimension_Example_VB.htm"
---

# Get Types of Entities Attached to Selected Annotation Example (VBA)

This example shows how to get the types of entities attached to a selected annotation.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part with annotations.
 ' 2. Select an annotation for which you want to get attached entities.
 ' 3. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '-----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swSelObj                As Object
     Dim swAnn                   As SldWorks.Annotation
     Dim vAttEntTypeArr          As Variant
     Dim vAttEntArr              As Variant
     Dim i                       As Long
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swSelObj = swSelMgr.GetSelectedObject6(1, -1)
     Set swAnn = swSelObj.GetAnnotation
    Debug.Print "Name              = " & swAnn.GetName
     Debug.Print "  Selection Type as defined in swSelectType_e = " & swSelMgr.GetSelectedObjectType3(1, -1)
     Debug.Print "  Annotation Type as defined in swAnnotationType_e = " & swAnn.GetType
    vAttEntArr = swAnn.GetAttachedEntities3
     vAttEntTypeArr = swAnn.GetAttachedEntityTypes2
    If Not IsEmpty(vAttEntTypeArr) Then
        For i = 0 To UBound(vAttEntTypeArr)
             ' A dangling annotation has at least one entity of type swSelNOTHING
             Debug.Print "  Type of attached entity(" & i & ") as defined in swSelectType_e  = " & vAttEntTypeArr(i)
         Next i
     End If
End Sub
```
