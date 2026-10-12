---
title: "Attach Annotation to Entity Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Attach_Annotation_to_Entity_Example_VBNET.htm"
---

# Attach Annotation to Entity Example (VB.NET)

This example shows how to attach an annotation to a different entity.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open a part or drawing that has at least one
'    annotation.
' 2. Select an annotation.
' 3. Press Ctrl while selecting a face, edge, or vertex.
'
' Postconditions:
' 1. Attaches the selected annotation to the entity
'    selected in Preconditions step 3, if possible.
' 2. Examine the annotation in the graphics area.
'
' NOTE: If you open a drawing:
' * uncomment the statement for a drawing.
' * comment out the statement for a part.
'-------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swSelObj1 As Object
        Dim swSelObj2 As Object
        Dim swAnn As Annotation
        Dim vAttEntTypeArr As Object
        Dim vAttEntArr As Object
        Dim i As Integer
        Dim bRet As Boolean

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager

        'Select the annotation to move
        swSelObj1 = swSelMgr.GetSelectedObject6(1, -1)
        swAnn = swSelObj1.GetAnnotation

        'Part - select the entity where to move the annotation
        swSelObj2 = swSelMgr.GetSelectedObject6(2, -1)

        'Drawing - select the entity where to to move the annotation
        'swSelObj2 = swSelMgr.GetSelectedObject6(3, -1)

        Dim AttEntArr(0) As Object
        AttEntArr(0) = swSelObj2
        Dim vAttEntArrIn() As DispatchWrapper
        vAttEntArrIn = ObjectArrayToDispatchWrapperArray(AttEntArr)
        bRet = swAnn.SetAttachedEntities(vAttEntArrIn)
        Debug.Print("Name = " & swAnn.GetName)
        Debug.Print("  Selection Type = " & swSelMgr.GetSelectedObjectType3(1, -1))
        Debug.Print("  Annotation Type = " & swAnn.GetType)
        vAttEntArr = swAnn.GetAttachedEntities3
        vAttEntTypeArr = swAnn.GetAttachedEntityTypes
        If Not vAttEntTypeArr Is Nothing Then
            Debug.Assert(UBound(vAttEntArr) = UBound(vAttEntTypeArr))
            For i = 0 To UBound(vAttEntTypeArr)
                'A dangling dimension has at least one entity of type swSelNOTHING
                Debug.Print("  Entity Type(" & i & ") = " & vAttEntTypeArr(i))
                Dim swSelData As SelectData
                swSelData = swSelMgr.CreateSelectData
                Call vAttEntArr(i).Select4(False, swSelData)
            Next i
        End If

    End Sub

    Function ObjectArrayToDispatchWrapperArray(ByVal Objects As Object()) As DispatchWrapper()
        Dim ArraySize As Integer
        ArraySize = Objects.GetUpperBound(0)
        Dim d(ArraySize) As DispatchWrapper
        Dim ArrayIndex As Integer
        For ArrayIndex = 0 To ArraySize
            d(ArrayIndex) = New DispatchWrapper(Objects(ArrayIndex))
        Next
        Return d

    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
