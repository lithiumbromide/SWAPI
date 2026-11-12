---
title: "Insert Explode Line Sketch and Jog Line Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Explode_Line_Sketch_and_Jog_Line_Example_VBNET.htm"
---

# Insert Explode Line Sketch and Jog Line Example (VB.NET)

This example shows how to insert a jog line in an explode line sketch, a type of 3D sketch.

```
'--------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
'
' Postconditions:
' 1. Creates an exploded view of the assembly.
' 2. Adds a jog line, which is a type of explode line.
' 3. Examine the graphics area.
' 4. Locate 3DExplode1, the explode line sketch, on the
'    ConfigurationManager tab (click the ConfigurationManager tab and
'    expand default and ExplView1.)
'
' NOTE: Because this assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
```

```vb
Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
    Dim swAssembly As AssemblyDoc
     Dim swSketchMgr As SketchManager
     Dim swSketchSegment As SketchSegment

     Sub main()

        swModel = SwApp.ActiveDoc
         swAssembly = swModel
         swSketchMgr = swModel.SketchManager

         ' Explode the assembly
         swAssembly.AutoExplode()

         swModel.EditRebuild3()

         swModel.ViewZoomtofit2()

         ' Insert an explode line sketch
         swSketchMgr.InsertExplodeLineSketch()

         'Create a line
         swSketchSegment = swSketchMgr.CreateLine(0, 0.1, 0, 0, 0.3, 0)

         swModel.ViewZoomtofit2()
        ' Create a jog line using the line
         swSketchSegment.JogLine(0, 0.2, 0, 0.04, 0.25, 0)

         ' Close the 3D sketch
         swSketchMgr.Insert3DSketch(True)

    End Sub

    ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
