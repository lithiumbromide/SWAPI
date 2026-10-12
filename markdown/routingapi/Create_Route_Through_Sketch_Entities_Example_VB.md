---
title: "Create Route Through Sketch Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Create_Route_Through_Sketch_Entities_Example_VB.htm"
---

# Create Route Through Sketch Entities Example (VBA)

This example shows how to create a route by specifying sketch entity types and their IDs.

```
'--------------------------------------------
' Preconditions:
' 1. Add SOLIDWORKS Routing as an add-in
'   (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
' 2. Add the SOLIDWORKS <version> Routing Type Library as a reference
'   (in the IDE select Tools > References).
' 3. Open public documents\samples\tutorial\api\AutoRouteThroughSketchEntities.sldasm
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
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swTopLevelAssembly As SldWorks.AssemblyDoc
    Dim rtRouteManager As SWRoutingLib.RouteManager
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSketchPt1 As SldWorks.SketchPoint
    Dim swSketchPt2 As SldWorks.SketchPoint
    Dim status As Boolean
    Dim routeStatus as Long
    Dim sketchEntityTypes(1) As Long
    Dim sketchPt1IDs As Variant
    Dim sketchPt2IDs As Variant
    Dim sketchPtIDs(1) As Long
```

```
    ' Connect to SOLIDWORKS
    Set swApp = Application.SldWorks
```

```
    ' Get the active document
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
```

```
    ' Downcast from model document to assembly document
    Set swTopLevelAssembly = swModel
```

```
    ' Get the RouteManager from the top-level assembly
    Set rtRouteManager = swTopLevelAssembly.GetRouteManager
```

```
    If rtRouteManager Is Nothing Then
        Debug.Print "No RouteManager found in top-level document"
        Exit Sub
    End If
```

```
    ' Get and edit the route
    status = swModelDocExt.SelectByID2("Route1@Harness_1-AutoRouteThroughSketchEntities-1@AutoRouteThroughSketchEntities", "ROUTEFABRICATED", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditRoute
```

```
    ' Get the AutoRoute
    Dim rtAutoRoute As AutoRoute
    Set rtAutoRoute = rtRouteManager.GetAutoRoute
```

```
    If rtAutoRoute Is Nothing Then
        Debug.Print "No AutoRoute found"
        Exit Sub
    End If
```

```
   'Assign the types of sketch entities to be sketch points
   sketchEntityTypes(0) = 0
   sketchEntityTypes(1) = 0
```

```
   ' Get the IDs of the sketch points
   status = swModelDocExt.SelectByID2("Point3@3DSketch1@Harness_1-AutoRouteThroughSketchEntities-1@AutoRouteThroughSketchEntities", "EXTSKETCHPOINT", 4.86125655897816E-02, 2.44300235589649E-02, 1.30597511505374E-02, False, 0, Nothing, 0)
   Set swSketchPt1 = swSelMgr.GetSelectedObject6(1, -1)
   sketchPt1IDs = swSketchPt1.GetID
   Debug.Print "sketchPt1IDs: " & sketchPt1IDs(0); ", " & sketchPt1IDs(1)
```

```
   swModel.ClearSelection2 True

   status = swModelDocExt.SelectByID2("Point7@3DSketch1@Harness_1-AutoRouteThroughSketchEntities-1@AutoRouteThroughSketchEntities", "EXTSKETCHPOINT", 0.145249999302905, -1.58029634039849E-02, -2.22342355241044E-02, False, 0, Nothing, 0)
   Set swSketchPt2 = swSelMgr.GetSelectedObject6(1, -1)
   sketchPt2IDs = swSketchPt2.GetID
   Debug.Print "sketchPt2IDs: " & sketchPt2IDs(0); ", " & sketchPt2IDs(1)
```

```
   ' Create an array containing the first
   ' member of each sketch point ID array
   ' to pass to IAutoRoute::CreateRouteThroughSketchEntities
   sketchPtIDs(0) = sketchPt1IDs(0)
   sketchPtIDs(1) = sketchPt2IDs(0)
```

```
   ' Create the route
   routeStatus = rtAutoRoute.CreateRouteThroughSketchEntities(swAutoRouteConversionMode_e.swOrthogonalAutoRouteMode, swAutoRouteAutoTangencyMode_e.swAutoTangencyMode_ON, sketchEntityTypes, sketchPtIDs)
```

```
    ' Clear selection
    swModel.ClearSelection2 True
```

```
    ' Return to editing the top-level assembly
    swTopLevelAssembly.EditAssembly
```

```
End Sub
```
