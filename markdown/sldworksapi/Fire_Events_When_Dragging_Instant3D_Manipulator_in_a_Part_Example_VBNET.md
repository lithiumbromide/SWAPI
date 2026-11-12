---
title: "Fire Events When Dragging Instant3D Manipulator in a Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Dragging_Instant3D_Manipulator_in_a_Part_Example_VBNET.htm"
---

# Fire Events When Dragging Instant3D Manipulator in a Part Example (VB.NET)

This example shows how to fire events when dragging an Instant3D manipulator in a part document.

```vb
'------------------------------------
 ' Preconditions:
 ' 1. Open a part document.
 ' 2. Open the Immediate window.
 '
 ' NOTE: Instant3D is enabled by the macro.
 '
 ' Postconditions:
 ' 1. Select an Instant3D manipulator in the
 '    open part. For example,
 '    double-click an extrude feature in a part,
 '    then select one of the Instant3D manipulators
 '    and drag it.
 ' 2. Writes a debug statement to the Immediate window
 '    informing you that dragging of an Instant3D
 '    manipulator has started.
 ' 3. Stop dragging the manipulator.
 ' 4. Writes a debug statement to the Immediate
 '    window informing you that dragging of
 '    an Instant3D manipulator has stopped.
 ' 5. Examine the Immediate window.
 '----------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Collections
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public WithEvents pDoc As PartDoc

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swFeatMgr As FeatureManager
         Dim openPart As Hashtable

         swModel = swApp.ActiveDoc

         ' Enable Instant3D
         swFeatMgr = swModel.FeatureManager
         swFeatMgr.MoveSizeFeatures = True

         ' Execute events
         pDoc = swModel
         openPart = New Hashtable
         AttachEventHandlers()

     End Sub

     Sub AttachEventHandlers()
         AttachSWEvents()
     End Sub

     Sub AttachSWEvents()
         If Not pDoc Is Nothing Then
             AddHandler pDoc.DragStateChangeNotify, AddressOf Me.pDoc_DragStateChangeNotify
         End If
     End Sub

     Private Function pDoc_DragStateChangeNotify(ByVal State As Boolean) As Integer
         ' Write debug statement when dragging of manipulator started and stopped
         If State = True Then
             Debug.Print("Dragging of manipulator started.")
         Else
             Debug.Print("Dragging of manipulator stopped.")
         End If
     End Function

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
