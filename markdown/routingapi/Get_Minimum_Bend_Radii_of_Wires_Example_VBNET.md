---
title: "Get Minimum Bend Radii of Wires Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_Minimum_Bend_Radii_of_Wires_Example_VBNET.htm"
---

# Get Minimum Bend Radii of Wires Example (VB.NET)

This example shows how to get:

- minimum bend radius for the bundle of wires in each route segment,
- minimum bend radius for each route segment, and
- types of routes.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Add SOLIDWORKS Routing as an add-in
'   (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
' 2. Add Solidworks.interop.SwRoutingLib.dll as a reference
'   (in the IDE right-click the project,
'    select Add Reference, and browse install_dir\api\redist).
' 3. Open public_documents\samples\tutorial\api\RoutingAssem1.sldasm.
' 4. Open the Immediate window.
' 5. Run the macro.
'
' Postconditions: Examine the Immediate window.
'
' NOTE: Because the assembly document is used elsewhere, do not save
' any changes when closing it.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics
Imports SolidWorks.Interop.SWRoutingLib

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDoc As ModelDocExtension
        Dim swTopLevelAssembly As AssemblyDoc
        Dim rtRouteManager As RouteManager
        Dim bRetVal As Boolean

        ' Get the active document
        swModel = swApp.ActiveDoc
        swModelDoc = swModel.Extension

        ' Downcast from model document to assembly document
        swTopLevelAssembly = swModel

        ' Get the RouteManager from the top-level assembly
        ' Use selection tied to the current document, which is the
        ' top-level assembly, so get the RouteManager from there
        ' instead of from the route subassembly
        rtRouteManager = swTopLevelAssembly.GetRouteManager

        If rtRouteManager Is Nothing Then
            Debug.Print("No RouteManager found in top-level document")
            Exit Sub
        End If

        ' Select route in subassembly
        bRetVal = swModelDoc.SelectByID2("Route1@Harness1^RoutingAssem1-1@RoutingAssem1", "ROUTEFABRICATED", 0, 0, 0, False, 0, Nothing, 0)

        swModel.EditRoute()

        ' Clear selection
        swModel.ClearSelection2(True)

        ' Select the 3D Sketch
        bRetVal = swModelDoc.SelectByID2("3DSketch1@Harness1-RoutingAssem1-1@RoutingAssem1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)

        ' Edit the 3D Sketch
        Debug.Print("Spline1:")
        TestRoute(swModelDoc, rtRouteManager, "Spline1")
        Debug.Print("Spline2:")
        TestRoute(swModelDoc, rtRouteManager, "Spline2")

        ' Stop editing
        swModel.Insert3DSketch2(True)

        ' Return to editing the top-level assembly
        swTopLevelAssembly.EditAssembly()

    End Sub
    Private Sub TestRoute(ByVal swModelDoc As ModelDocExtension, ByVal rtRouteManager As RouteManager, ByVal strSketchSegmentName As String)
        ' Select a sketch segment
        Dim bRetVal As Boolean
        bRetVal = swModelDoc.SelectByID2(strSketchSegmentName, "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)

        If (Not (bRetVal = False)) Then
            ' Get the RouteProperty for the selected sketch segment
            Dim rtRouteProperty As ElectricalRouteProperty
            rtRouteProperty = rtRouteManager.GetRouteProperty

            If Not rtRouteProperty Is Nothing Then
                Debug.Print("  Bundle minimum bend radius      = " & rtRouteProperty.BundleMinimumBendRadius)
                Debug.Print("  Minimum bend radius             = " & rtRouteProperty.MinimumBendRadius)
                Dim rtProperty As Integer
                rtProperty = rtRouteProperty.RouteType
                Select Case rtProperty
                    Case swRouteType_e.swRouteType_Electrical
                        Debug.Print("  Type                            = Electrical")
                End Select
            End If
        End If
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
