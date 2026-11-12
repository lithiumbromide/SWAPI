---
title: "Add and Delete Appearances from Specific Display States Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm"
---

# Add and Delete Appearances from Specific Display States Example (VBA)

This example shows how to add an appearance to and delete an appearance from specific display states.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Specified model exists.
 ' 2. Specified appearance exists.
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates Display State 2 and Display State 3 for the active
 '    configuration.
 ' 2. Applies specified appearance to all display states of the active
 '    configuration.
 ' 3. Press F5.
 ' 4. Deletes specified appearance from all display states of the active
 '    configuration.
 ' 5. Press F5.
 ' 6. Closes document.
 '---------------------------------------------------------------------------
 Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swConfig As SldWorks.Configuration
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swEntity As SldWorks.Entity
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swRenderMaterial As SldWorks.RenderMaterial
 Dim displayStateNames As Variant
 Dim status As Boolean
 Dim modelName As String
 Dim materialName As String
 Dim errors As Long
 Dim warnings As Long
 Dim nbrDisplayStates As Long
 Dim i As Long
 Dim k As Long
 Dim nbrMaterials As Long
 Dim materialID1 As Long
 Dim materialID2 As Long
 Dim materialID1_ToDelete(0) As Long
 Dim materialID2_ToDelete(0) As Long
Sub main()
    modelName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\dimxpert\bracket_auto_manual.sldprt"
     Set swApp = Application.SldWorks
     Set swModel = swApp.OpenDoc6(modelName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
     Set swModelDocExt = swModel.Extension

     ' Get active configuration and create a new display
     ' state for this configuration
     Set swConfig = swModel.GetActiveConfiguration
     status = swConfig.CreateDisplayState("Display State 2")

    swModel.ForceRebuild3 True

    ' Get active configuration and create another new
     ' display state for this configuration
     Set swConfig = swModel.GetActiveConfiguration
     status = swConfig.CreateDisplayState("Display State 3")

    swModel.ForceRebuild3 True

    ' Create appearance
     materialName = "C:\Program Files\SolidWorks Corp\SolidWorks\data\graphics\materials\metal\steel\stainless steel treadplate.p2m"
     Set swRenderMaterial = swModelDocExt.CreateRenderMaterial(materialName)

    ' Select a face and add the appearance to that face
     status = swModelDocExt.SelectByID2("", "FACE", 0.07151920610502, 0.0952597996959, 0.009524999999996, False, 0, Nothing, 0)
     Set swSelMgr = swModel.SelectionManager
     Set swEntity = swSelMgr.GetSelectedObject6(1, -1)
     status = swRenderMaterial.AddEntity(swEntity)

    ' Get the names of display states
     displayStateNames = swConfig.GetDisplayStates
     nbrDisplayStates = swConfig.GetDisplayStatesCount
     Debug.Print "This configuration's display states ="
     For i = 0 To (nbrDisplayStates - 1)
         Debug.Print "  Display state name = " & displayStateNames(i)
     Next i

    ' Add appearance to all of the display states
     status = swModelDocExt.AddDisplayStateSpecificRenderMaterial(swRenderMaterial, swAllDisplayState, displayStateNames, materialID1, materialID2)

    ' Get the appearance IDs and names
     swRenderMaterial.GetMaterialIds materialID1, materialID2
     Debug.Print "    Appearance IDs:"
     Debug.Print "      ID1 = " & materialID1
     Debug.Print "      ID2 = " & materialID2
     nbrMaterials = swModelDocExt.GetRenderMaterialsCount2(swAllDisplayState, Nothing)
     Debug.Print "    Number of appearances: " & nbrMaterials
     For k = 0 To (nbrMaterials - 1)
         Debug.Print "      Name of appearance " & (k + 1) & ": " & swModel.MaterialIdName
     Next k

    Dim xcoord As Double
     Dim ycoord As Double
     Dim zcoord As Double
     swRenderMaterial.GetCenterPoint2 xcoord, ycoord, zcoord
     Debug.Print ""
     Debug.Print "Texture-based appearance data:"
     Debug.Print "X coordinate of center point: " & xcoord
     Debug.Print "Y coordinate of center point: " & ycoord
     Debug.Print "Z coordinate of center point: " & zcoord

    swRenderMaterial.GetUDirection2 xcoord, ycoord, zcoord
     Debug.Print "X coordinate of U direction: " & xcoord
     Debug.Print "Y coordinate of U direction: " & ycoord
     Debug.Print "Z coordinate of U direction: " & zcoord

    swRenderMaterial.GetVDirection2 xcoord, ycoord, zcoord
     Debug.Print "X coordinate of V direction: " & xcoord
     Debug.Print "Y coordinate of V direction: " & ycoord
     Debug.Print "Z coordinate of V direction: " & zcoord
     Debug.Print ""

    swModel.ClearSelection2 True
     swModel.ForceRebuild3 True

    Debug.Print "Model has an appearance: " & swModelDocExt.HasMaterialPropertyValues

    Dim dispStates As Variant
     status = swRenderMaterial.SetLinkedDisplayStates(swAllDisplayState, displayStateNames)
     dispStates = swRenderMaterial.GetLinkedDisplayStates

    Dim renderMaterials As Variant
     renderMaterials = swModelDocExt.GetRenderMaterials2(swAllDisplayState, Nothing)

    ' Examine the display states of the active configuration
     ' to ensure that the specified appearance was applied to all
     ' display states (click the ConfigurationManager tab and switch
     ' display states at bottom of the Configuration pane)
     ' Continue running the macro after your examination
     Stop

    ' Delete the appearance from the part
     materialID1_ToDelete(0) = materialID1
     materialID2_ToDelete(0) = materialID2
     swModelDocExt.DeleteDisplayStateSpecificRenderMaterial (materialID1_ToDelete), (materialID2_ToDelete)
     swModel.ForceRebuild3 True

    ' Examine the display states of the active configuration
     ' to ensure that the specified appearance was deleted from all
     ' display states (click the ConfigurationManager tab and switch
     ' display states at bottom of the Configuration pane)
     ' Continue running the macro after your examination
     Stop

    ' Close the part without saving changes
     modelName = swModel.GetTitle
     swApp.QuitDoc modelName

End Sub
```
