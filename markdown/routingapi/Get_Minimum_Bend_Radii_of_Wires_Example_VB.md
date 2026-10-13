---
title: "Get Minimum Radii of Wires Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_Minimum_Bend_Radii_of_Wires_Example_VB.htm"
---

# Get Minimum Radii of Wires Example (VBA)

This example shows how to get:

- minimum bend radius for the bundle of wires in each route segment,
- minimum bend radius for each route segment, and
- types of route.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Add SOLIDWORKS Routing as an add-in
'   (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
' 2. Add the SOLIDWORKS <version> Routing Type Library as a reference
'   (in the IDE select Tools > References).
' 3. Open public_documents\samples\tutorial\api\RoutingAssem1.sldasm.
' 4. Open the Immediate window.
' 5. Run the macro.
'
' Postconditions: Examine the Immediate window.
'
' NOTE: Because the assembly document is used elsewhere, do not save
' any changes when closing it.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Dim swModel              As SldWorks.ModelDoc2
    Dim swModelDoc           As SldWorks.ModelDocExtension
    Dim swTopLevelAssembly   As SldWorks.AssemblyDoc
    Dim rtRouteManager       As SWRoutingLib.RouteManager
    Dim bRetVal              As Boolean
```

```
    ' Connect to SOLIDWORKS
    Set swApp = Application.SldWorks
```

```
    ' Get the active document
    Set swModel = swApp.ActiveDoc
    Set swModelDoc = swModel.Extension
```

```
    ' Downcast from model document to assembly document
    Set swTopLevelAssembly = swModel
```

```
    ' Get the RouteManager from the top-level assembly
    ' Use selection tied to the current document, which is the
    ' top-level assembly, so get the RouteManager from there
    ' instead of from the route subassembly
    Set rtRouteManager = swTopLevelAssembly.GetRouteManager
```

```
    If rtRouteManager Is Nothing Then
        Debug.Print "No RouteManager found in top-level document"
        Exit Sub
    End If
```

```
    ' Select route in subassembly
    bRetVal = swModelDoc.SelectByID2("Route1@Harness1^RoutingAssem1-1@RoutingAssem1", "ROUTEFABRICATED", 0, 0, 0, False, 0, Nothing, 0)
```

```
    swModel.EditRoute
```

```
    ' Clear selection
    swModel.ClearSelection2 True
```

```
    ' Select the 3D Sketch
    bRetVal = swModelDoc.SelectByID2("3DSketch1@Harness1-RoutingAssem1-1@RoutingAssem1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
```

```
    ' Edit the 3D Sketch
    Debug.Print "Spline1:"
    TestRoute swModelDoc, rtRouteManager, "Spline1"
    Debug.Print "Spline2:"
    TestRoute swModelDoc, rtRouteManager, "Spline2"
```

```
    ' Stop editing
    swModel.Insert3DSketch2 True
```

```
    ' Return to editing the top-level assembly
    swTopLevelAssembly.EditAssembly
```

```
End Sub
Private Sub TestRoute(swModelDoc As ModelDocExtension, rtRouteManager As RouteManager, strSketchSegmentName As String)
    ' Select a sketch segment
    Dim bRetVal As Boolean
    bRetVal = swModelDoc.SelectByID2(strSketchSegmentName, "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
```

```
    If (Not (bRetVal = False)) Then
        ' Get the RouteProperty for the selected sketch segment
        Dim rtRouteProperty As SWRoutingLib.ElectricalRouteProperty
        Set rtRouteProperty = rtRouteManager.GetRouteProperty
```

```
        If Not rtRouteProperty Is Nothing Then
            Debug.Print "  Bundle minimum bend radius      = " & rtRouteProperty.BundleMinimumBendRadius
            Debug.Print "  Minimum bend radius             = " & rtRouteProperty.MinimumBendRadius
```

```
            Select Case rtRouteProperty.RouteType
                Case SWRoutingLib.swRouteType_e.swRouteType_Electrical
                    Debug.Print "  Type                            = Electrical"
            End Select
        End If
    End If
End Sub
```
