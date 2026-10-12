---
title: "Fire Events When Dragging Instant3D Manipulator in an Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Dragging_Instant3D_Manipulator_in_an_Assembly_Example_VBNET.htm"
---

# Fire Events When Dragging Instant3D Manipulator in an Assembly Example (VB.NET)

This example shows how to fire events when dragging an Instant3D manipulator in an assembly document.

```vb
'------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document.
 ' 2. Open the Immediate window.
 '
 ' NOTE: Instant3D is enabled by the macro.
 '
 ' Postconditions:
 ' 1. Select an Instant3D manipulator in the
 '    open assembly by right-clicking a floating
 '    assembly component, clicking the down arrows
 '    at the bottom of the shortcut menu, and selecting
 '    Move with Triad.
 ' 2. Drag the Instant3D handle to move the assembly
 '    component.
 ' 3. Writes a debug statement to the Immediate window
 '    informing you that dragging of an Instant3D
 '    manipulator has started.
 ' 4. Stop dragging the manipulator.
 ' 5. Writes a debug statement to the Immediate window
 '    informing you that dragging of an Instant3D
 '    manipulator has stopped.
 ' 6. Examine the Immediate window.
 '----------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Collections
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public WithEvents pDoc As AssemblyDoc

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swFeatMgr As FeatureManager
         Dim openAssembly As Hashtable

         swModel = swApp.ActiveDoc

         ' Enable Instant3D
         swFeatMgr = swModel.FeatureManager
         swFeatMgr.MoveSizeFeatures = True

         ' Execute events
         pDoc = swModel
         openAssembly = New Hashtable

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
