---
title: "Get Types of Entities Attached to Selected Annotation Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Types_of_Entities_for_Selected_Dimension_Example_VBNET.htm"
---

# Get Types of Entities Attached to Selected Annotation Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swSelObj As Object
         Dim swAnn As Annotation
         Dim vAttEntTypeArr As Object
         Dim vAttEntArr As Object
         Dim i As  Integer

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swSelObj = swSelMgr.GetSelectedObject6(1, -1)
         swAnn = swSelObj.GetAnnotation

         Debug.Print("Name = " & swAnn.GetName)
         Debug.Print("  Selection Type as defined in swSelectType_e = " & swSelMgr.GetSelectedObjectType3(1, -1))
         Debug.Print("  Annotation Type as defined in swAnnotationType_e = " & swAnn.GetType)

         vAttEntArr = swAnn.GetAttachedEntities3
         vAttEntTypeArr = swAnn.GetAttachedEntityTypes2

         If Not IsNothing(vAttEntTypeArr) Then
             For i = 0 To UBound(vAttEntTypeArr)
                 ' A dangling annotation has at least one entity of type swSelNOTHING
                 Debug.Print("  Type of attached entity(" & i   ") as defined in swSelectType_e  = " & vAttEntTypeArr(i))
             Next i
         End If

     End Sub

     Public swApp As SldWorks

 End  Class
```
