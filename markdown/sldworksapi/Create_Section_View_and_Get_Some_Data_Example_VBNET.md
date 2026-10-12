---
title: "Create Section View and Get Some Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Section_View_and_Get_Some_Data_Example_VBNET.htm"
---

# Create Section View and Get Some Data Example (VB.NET)

This example creates a section view and sets and gets some of the section view's data.

```vb
'--------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\driveworksxpress\mobile gantry.slddrw
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a section view of Drawing View4.
 ' 2. Sets and gets some section view settings.
 ' 3. Examine the drawing and the Immediate window.
 '
 ' NOTE: Because this drawing is used elsewhere, do not save changes.
 '--------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swDrawing As DrawingDoc
     Dim swSketchMgr As SketchManager
     Dim swSketchSegment As SketchSegment
     Dim excludedComponents As Object
     Dim swView As View
     Dim swSectionView As DrSection
     Dim boolstatus As Boolean

     Sub main()

         swModel = swApp.ActiveDoc
         swDrawing = swModel

         ' Activate the view for which you want to create a section view
         boolstatus = swDrawing.ActivateView("Drawing View4")
         swModel.ClearSelection2(True)

         ' Create section-view line
         swSketchMgr = swModel.SketchManager
         swSketchSegment = swSketchMgr.CreateLine(-1.383705, 2.078706, 0.0#, 2.747162, 0.0441, 0.0#)

         ' Create the section view at the specified coordinates
         ' and up to the specified distance from the section-view line
         excludedComponents =  Nothing
         swView = swDrawing.CreateSectionViewAt5(0.1604082711061, 0.2048687170364, 0, "D", 32, (excludedComponents), 0.00835)
         Debug.Print("View data:")
         Debug.Print(" Emphasize outlines of section views? " & swView.EmphasizeOutline)
         swSectionView = swView.GetSection

          ' Set some section-view settings
         swSectionView.SetAutoHatch(True)
         swSectionView.SetLabel2("ABCD")
         swSectionView.SetDisplayOnlySurfaceCut(False)
         swSectionView.SetPartialSection(False)
         swSectionView.SetReversedCutDirection(False)
         swSectionView.SetScaleWithModelChanges(True)
         swSectionView.CutSurfaceBodies = True
         swSectionView.DisplaySurfaceBodies = True
         swSectionView.ExcludeSliceSectionBodies = False

        ' Get some section-view settings
         Debug.Print("Section view data: ")
         Debug.Print(" Label: " & swSectionView.GetLabel)
         Debug.Print(" Name of section line: " & swSectionView.GetName)
         Debug.Print(" Depth: " & swSectionView.SectionDepth * 1000.0# & " mm")
         Debug.Print(" Cut direction reversed from default direction? " & swSectionView.GetReversedCutDirection)
         Debug.Print(" Partial section cut? " & swSectionView.GetPartialSection)
         Debug.Print(" Display only the surface cut by the section line? " & swSectionView.GetDisplayOnlySurfaceCut)
         Debug.Print(" Display surface bodies? " & swSectionView.DisplaySurfaceBodies)
         Debug.Print(" Exclude slice section bodies? " & swSectionView.ExcludeSliceSectionBodies)

         swSectionView.SetDisplayOnlySpeedPakBodies(True)

         Debug.Print(" Display only SpeedPak bodies? " & swSectionView.GetDisplayOnlySpeedPakBodies)
         Debug.Print(" Scale with model changes? " & swSectionView.GetScaleWithModelChanges)
         Debug.Print(" Auto-hatch enabled? " & swSectionView.GetAutoHatch)
         Debug.Print(" Hide cut surface bodies? " & swSectionView.CutSurfaceBodies)
```

swModel.**EditRebuild3**()

End Sub

Public swApp As SldWorks

End Class
