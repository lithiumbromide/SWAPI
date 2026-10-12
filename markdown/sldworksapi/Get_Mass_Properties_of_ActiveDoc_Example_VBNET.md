---
title: "Get Mass Properties Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_of_ActiveDoc_Example_VBNET.htm"
---

# Get Mass Properties Example (VB.NET)

This example shows how to retrieve the mass properties of selected components in an assembly.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Open an assembly with one or more components.
  ' 2. Multi-select the components for which to get mass properties.
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Gets the mass properties of the selected components
 '    in the assembly.
 ' 2. Inspect the Immediate window for the mass properties of
 '    the selected components.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swModelExt As ModelDocExtension
         Dim swSelMgr As SelectionMgr
         Dim swComp As Component2
         Dim nStatus As Integer
         Dim vMassProp As Object
         Dim i As Integer
         Dim nbrSelections As Integer

         swModel = swApp.ActiveDoc
         swModelExt = swModel.Extension
         swSelMgr = swModel.SelectionManager

         nbrSelections = swSelMgr.GetSelectedObjectCount2(-1)

         If nbrSelections = 0 Then
             Debug.Print("Please select one or more components and rerun the macro.")
              Exit Sub
         End  If

         nbrSelections = nbrSelections - 1

         Debug.Print("Getting mass properties for components: ")
         For i = 0 To nbrSelections
             swComp = swSelMgr.GetSelectedObject6(i + 1, -1)
             Debug.Print("  " & swComp.Name2)
         Next

         vMassProp = swModelExt.GetMassProperties2(1, nStatus, True)

         Debug.Print("Status as defined in swMassPropertiesStatus_e (0 = Mass properties calculation successful)  = " & nStatus)

         If Not IsNothing(vMassProp) Then

             Debug.Print("Center of mass:")
             Debug.Print("  X-coordinate = " & vMassProp(0))
             Debug.Print("  Y-coordinate = " & vMassProp(1))
             Debug.Print("  Z-coordinate = " & vMassProp(2))
             Debug.Print("Volume = " & vMassProp(3))
             Debug.Print("Surface area = " & vMassProp(4))
             Debug.Print("Mass = " & vMassProp(5))
             Debug.Print("Density = " & vMassProp(5) / vMassProp(3))
             Debug.Print("Moments of inertia taken at the center of mass and aligned with the output coordinate system:")
             Debug.Print("  Lxx = " & vMassProp(6))
             Debug.Print("  Lyy = " & vMassProp(7))
             Debug.Print("  Lzz = " & vMassProp(8))
             Debug.Print("  Lxy = " & vMassProp(9))
             Debug.Print("  Lzx = " & vMassProp(10))
             Debug.Print("  Lyz = " & vMassProp(11))

         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
