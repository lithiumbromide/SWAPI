---
title: "Create Route Through Sketch Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Create_Route_Through_Sketch_Entities_Example_VBNET.htm"
---

# Create Route Through Sketch Entities Example (VB.NET)

This example shows how to create a route by specifying sketch entity types and their IDs.

```
'--------------------------------------------
' Preconditions:
' 1. Add SOLIDWORKS Routing as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Routing).
' 2. Add the SOLIDWORKS Routing interop assembly as a reference
'    (right-click the project in Project Explorer, click Add Reference,
'    browse to install_dir\api\redist, and select
'    SolidWorks.Interop.SWRoutingLib.dll).
' 3. Open public_documents\samples\tutorial\api\AutoRouteThroughSketchEntities.sldasm
' 4. Open the Immediate window.
' 5. Run the macro.
'
' Postconditions:
' 1. Creates a route using the sketch
'    points whose entity types and IDs were passed
'    to IAutoRoute::CreateRouteThroughSketchEntities.
' 2. Examine the the assembly document to verify.
' 3. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere,
' do not save any changes when closing it.
'-------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics
Imports SolidWorks.Interop.swRoutingLib

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swTopLevelAssembly As AssemblyDoc
        Dim rtRouteManager As RouteManager
        Dim swSelMgr As SelectionMgr
        Dim swSketchPt1 As SketchPoint
        Dim swSketchPt2 As SketchPoint
        Dim status As Boolean
        Dim routeStatus as Integer
        Dim sketchEntityTypes(1) As Integer
        Dim sketchPt1IDs(1) As Integer
        Dim sketchPt2IDs(1) As Integer
        Dim sketchPtIDs(1) As Integer

        ' Get the active document
        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager

        ' Downcast from model document to assembly document
        swTopLevelAssembly = swModel

        ' Get the RouteManager from the top-level assembly
        rtRouteManager = swTopLevelAssembly.GetRouteManager

        If rtRouteManager Is Nothing Then
            Debug.Print("No RouteManager found in top-level document")
            Exit Sub
        End If

        ' Get and edit the route
        status = swModelDocExt.SelectByID2("Route1@Harness_1-AutoRouteThroughSketchEntities-1@AutoRouteThroughSketchEntities", "ROUTEFABRICATED", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditRoute()

        ' Get the AutoRoute
        Dim rtAutoRoute As AutoRoute
        rtAutoRoute = rtRouteManager.GetAutoRoute

        If rtAutoRoute Is Nothing Then
            Debug.Print("No AutoRoute found")
            Exit Sub
        End If

        'Assign the types of sketch entities to be sketch points
        sketchEntityTypes(0) = 0
        sketchEntityTypes(1) = 0

        ' Get the IDs of the sketch points
        status = swModelDocExt.SelectByID2("Point3@3DSketch1@Harness_1-AutoRouteThroughSketchEntities-1@AutoRouteThroughSketchEntities", "EXTSKETCHPOINT", 0.0486125655897816, 0.0244300235589649, 0.0130597511505374, False, 0, Nothing, 0)
        swSketchPt1 = swSelMgr.GetSelectedObject6(1, -1)
        sketchPt1IDs = swSketchPt1.GetID
        Debug.Print("sketchPt1IDs: " & sketchPt1IDs(0) & ", " & sketchPt1IDs(1))

        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Point7@3DSketch1@Harness_1-AutoRouteThroughSketchEntities-1@AutoRouteThroughSketchEntities", "EXTSKETCHPOINT", 0.145249999302905, -0.0158029634039849, -0.0222342355241044, False, 0, Nothing, 0)
        swSketchPt2 = swSelMgr.GetSelectedObject6(1, -1)
        sketchPt2IDs = swSketchPt2.GetID
        Debug.Print("sketchPt2IDs: " & sketchPt2IDs(0) & ", " & sketchPt2IDs(1))

        ' Create an array containing the first
        ' member of each sketch point ID array
        ' to pass to IAutoRoute::CreateRouteThroughSketchEntities
        sketchPtIDs(0) = sketchPt1IDs(0)
        sketchPtIDs(1) = sketchPt2IDs(0)

        ' Create the Auto Route
        routeStatus = rtAutoRoute.CreateRouteThroughSketchEntities(swAutoRouteConversionMode_e.swOrthogonalAutoRouteMode, swAutoRouteAutoTangencyMode_e.swAutoTangencyMode_ON, sketchEntityTypes, sketchPtIDs)

        ' Clear selection
        swModel.ClearSelection2(True)

        ' Return to editing the top-level assembly
        swTopLevelAssembly.EditAssembly()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
