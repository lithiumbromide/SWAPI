---
title: "Creating Bounding Box Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Bounding_Box_Example_VB.htm"
---

# Creating Bounding Box Example (VBA)

This example shows how to create a bounding box.

'----------------------------------------------------------------------------
' Preconditions: Open an Immediate window and ensure that the specified model to open exists.
'
' Postconditions:
' 1. Creates **Bounding Box** in the FeatureManager design tree.
' 2. Modifies **Bounding Box**.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'----------------------------------------------------------------------------

```vb
Dim swApp As SldWorks.SldWorks
 Dim swGPData As SldWorks.BoundingBoxFeatureData
 Dim featdata As SldWorks.BoundingBoxFeatureData
 Dim Part As SldWorks.ModelDoc2
 Dim ent As SldWorks.Face2
 Dim feat As SldWorks.Feature
 Dim featmgr As SldWorks.FeatureManager
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "block20.sldprt", False, longstatus
     Set Part = swApp.ActiveDoc

    Set featmgr = Part.FeatureManager

    boolstatus = Part.Extension.SelectByRay(1.08472195143463E-02, 3.96239999998329E-02, -1.01823136031953E-03, -0.400036026779312, -0.515038074910024, -0.758094294050284, 1.1224765174324E-03, 2, False, 0, 0)

    Set ent = Part.SelectionManager.GetSelectedObject6(1, -1)
     Set swGPData = featmgr.CreateDefinition(swFmBoundingBox)
     swGPData.ReferenceFaceOrPlane = 2
     swGPData.PlanarEntity = ent

    Set feat = featmgr.CreateFeature(swGPData)
     Part.ClearSelection2 True

    Set featdata = feat.GetDefinition()
     featdata.AccessSelections Part, Nothing
     boolstatus = Part.Extension.SelectByRay(-1.03569711794194E-02, 1.88454182651299E-02, 0.049345602378537, -0.400036026779312, -0.515038074910024, -0.758094294050284, 1.1224765174324E-03, 2, False, 0, 0)
     Set ent = Part.SelectionManager.GetSelectedObject6(1, -1)
     featdata.PlanarEntity = ent
     featdata.IncludeSurfaces = True
     featdata.IncludeHiddenBodies = True
     feat.ModifyDefinition featdata, Part, Nothing
     Debug.Print "Diameter(m) of sphere enclosing the bounding box: " & Part.Extension.GetSphericalBoxDiameter()

End Sub
```
