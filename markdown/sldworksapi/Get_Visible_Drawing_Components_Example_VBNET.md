---
title: "Get Visible Drawing Components Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Visible_Drawing_Components_Example_VBNET.htm"
---

# Get Visible Drawing Components Example (VB.NET)

This example shows how to get the visible drawing components in a drawing of an assembly.

```vb
  '-------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing document of an assembly that contains Drawing View1
 '    with one or more visible components.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Gets the visible components and their names.
 ' 2. Examine the Immediate window.
  '-------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial   Class   SolidWorksMacro
       Public  Sub main()

            Dim swModel  As  ModelDoc2
            Dim swModelDocExt  As   ModelDocExtension
            Dim swSelMgr  As  SelectionMgr
            Dim swView  As  View
            Dim swDrComp  As  DrawingComponent
            Dim swComp  As  Component2
            Dim vComps()  As  Object
            Dim vBodies  As  Object =   Nothing
            Dim boolstatus  As   Boolean
            Dim itr  As  Integer

           swModel = swApp.ActiveDoc
           swModelDocExt = swModel.Extension
           swSelMgr = swModel.SelectionManager
           boolstatus = swModel.ActivateView("Drawing View1")
           boolstatus = swModelDocExt.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0, 0, 0,   False, 0,   Nothing, 0)
           swView = swSelMgr.GetSelectedObject6(1, -1)
           swModel.ClearSelection2(True)

            'Get all visible components in Drawing View1
           vComps = swView.GetVisibleDrawingComponents

            'Print the number of visible components
            Debug.Print("Number of visible components:")
            Debug.Print("  " & vComps.Length)

            'Iterate through the visible components and print each one's name
            Debug.Print("Names of visible components:")
            For itr = 0  To UBound(vComps)
              swDrComp = vComps(itr)
               Debug.Print("  " & swDrComp.Name)
               ' Print the referenced assembly component name
              swComp = swDrComp.Component
               If  Not IsNothing(swComp)   Then
                  Debug.Print("    " & swComp.Name2)
                   Call swComp.GetBodies3(swBodyType_e.swAllBodies, vBodies)
                   If  Not IsNothing(vBodies)   Then
                        Debug.Print("    Component bodies exist.")
                   End  If
              End  If
            Next itr

       End  Sub
       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
