---
title: "Capture 3D View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Capture_3DView_Example_VBNET.htm"
---

# Capture 3D View Example (VB.NET)

This example shows how to capture the 3D view of a part or assembly and get its properties.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part or assembly.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Captures 3DViewn.
 ' 2. Prints out all of the 3D View names.
 ' 3. Renames 3DViewn to Aleph.
 ' 4. Refreshes the model's 3D Views.
 ' 5. Observe Aleph on the 3DViews tab.
 ' 6. Inspect the Immediate window.
  ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swDoc As ModelDoc2
     Dim swModelExt As ModelDocExtension
     Dim sw3DView As View3D
     Dim viewNames As Object
     Dim v_counter As Integer
     Dim modelBreakViewName as String =  ""

     Sub main()

         swDoc = swApp.ActiveDoc
         swModelExt = swDoc.Extension

         sw3DView = swModelExt.Capture3DView
         viewNames = swModelExt.Get3DViewNames
         Debug.Print("3D Views:")
         For v_counter = 0 To UBound(viewNames)
             Debug.Print("  " & viewNames(v_counter))
         Next

         sw3DView.Activate(True)
         sw3DView.Name = "Aleph"
         swModelExt.Refresh3DViews()
         Debug.Print("Number of 3D Views: " & swModelExt.Get3DViewCount)
         Debug.Print("Name of active 3D View: " & sw3DView.Name)
         Debug.Print("Configuration: " & sw3DView.ConfigurationName)
         Debug.Print("Display state: " & sw3DView.DisplayState)
         Debug.Print("Display mode as defined in swDisplayMode_e: " & sw3DView.DisplayMode)
         Debug.Print("Scale: " & sw3DView.Scale)
         modelBreakViewName = sw3DView.ModelBreakViewName
         If modelBreakViewName = "" Then
             Debug.Print("No model break view")
          Else
             Debug.Print("Model break view name: " & modelBreakViewName)
          End If

     End Sub

     Public swApp As SldWorks

 End Class
```
