---
title: "Change Color of Component in Specific Display State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Color_of_Component_in_Specific_Display_State_Example_VB.htm"
---

# Change Color of Component in Specific Display State Example (VBA)

This example shows how to change the color of a:

- selected component in a
  specific display state at the assembly and part levels.
- component in its part document.

```
'----------------------------------------------
' Postconditions:
'  1. Verify that the specified assembly and part exist.
'  2. Add the Microsoft Excel Object Library as a reference
'     for the Min and Max functions.
'
' Postconditions:
'  1. Opens the specified assembly document.
'  2. Changes the selected component's, USB_cover1,
'     assembly-level color from the default red
'     to gray in the specified display state. This
'     is the overriding color level.
'  3. To verify, examine the component in the graphics area and
'     click Show Display Pane (>) in the FeatureManager design tree
'     and examine the Appearance column to see the level where the
'     appearance color was applied.
'  4. Press F5 to continue.
'  5. Changes the selected component's, USB_cover1, part-level
'     color from red to green in the specified display state of
'     the component part. This is not the overriding color level.
'  6. To verify, examine the Appearance column to see the
'     level where the appearance color was applied.
'  7. Press F5 to continue.
'  8. Closes, but does not save, the assembly document.
'  9. Opens the component's part document, USB_cover1.sldprt.
' 10. Examine the graphics area.
' 11. Press F5 to continue.
' 12. Changes the part's color from red to green in the specified
'     display state of the part. This is the overriding color
'     level.
' 13. To verify, examine the graphics area.
' 14. Press F5 to continue.
' 15. Closes, but does not save, the part document.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModelDoc As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDisplayStateSetting As SldWorks.DisplayStateSetting
    Dim swComponent As SldWorks.Component2
    Dim swComponents(0) As SldWorks.Component2
    Dim swConfig As SldWorks.Configuration
    Dim displayStateNames(0) As String
    Dim appearances As Variant
    Dim swAppearanceSetting As SldWorks.AppearanceSetting
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim newAppearances(0) As Object
    Dim status As Boolean
    Dim errors As Long
    Dim warnings As Long
    Dim fileName As String
    Dim red_rgb As Long
    Dim green_rgb As Long
    Dim blue_rgb As Long
    Dim newColor As Long
```

```
    Set swApp = Application.SldWorks
```

```
    'Open assembly document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\appearances\usb_flash_drive1.sldasm"
    Set swModelDoc = swApp.OpenDoc6(fileName, swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Select component, USB_cover1
    Set swModelDocExt = swModelDoc.Extension
    Set swSelMgr = swModelDoc.SelectionManager
    status = swModelDocExt.SelectByID2("USB_cover1-1@usb_flash_drive1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swComponent = swSelMgr.GetSelectedObject6(1, -1)
    Set swComponents(0) = swComponent
```

```
    swModelDoc.ClearSelection2 True
```

```
    'Get display state
    Set swDisplayStateSetting = swModelDocExt.GetDisplayStateSetting(swAllDisplayState)
    swDisplayStateSetting.Entities = swComponents
    swDisplayStateSetting.Option = swSpecifyDisplayState
    displayStateNames(0) = "Display State-1"
    swDisplayStateSetting.Names = displayStateNames
```

```
    'Assembly level is the default
    swDisplayStateSetting.PartLevel = False
```

```
    'Change the selected component's, USB_cover1,
    'assembly-level color from the default red
    'to gray in the specified display state; this
    'is the overriding color level
    appearances = swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting)
    Set swAppearanceSetting = appearances(0)
    red_rgb = 50
    green_rgb = 50
    blue_rgb = 50
    newColor = Excel.WorksheetFunction.Max(Excel.WorksheetFunction.Min(red_rgb, 255), 0) + Excel.WorksheetFunction.Max(Excel.WorksheetFunction.Min(green_rgb, 255), 0) * 16 * 16 + Excel.WorksheetFunction.Max(Excel.WorksheetFunction.Min(blue_rgb, 255), 0) * 16 * 16 * 16 * 16
    swAppearanceSetting.Color = newColor
```

swAppearanceSetting. Diffuse = 0.8

swAppearanceSetting. Specular = 0.5

swAppearanceSetting. SpecularColor = newColor

swAppearanceSetting. Luminous = 0.1

swAppearanceSetting. Transparent = 0.0

```
    Set newAppearances(0) = swAppearanceSetting
    swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting) = newAppearances
```

```
    Stop
    'Examine the component in the graphics area
    'Click Show Display Pane (>) in the FeatureManager
    'design tree and examine the Appearance column to see
    'the level where the appearance color was applied
    'Press F5 to continue
```

```
    swModelDoc.ClearSelection2 True
```

```
    status = swModelDocExt.SelectByID2("USB_cover1-1@usb_flash_drive1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swComponent = swSelMgr.GetSelectedObject6(1, -1)
    Set swComponents(0) = swComponent
```

```
    swModelDoc.ClearSelection2 True
```

```
    'Get display state
    Set swDisplayStateSetting = swModelDocExt.GetDisplayStateSetting(swAllDisplayState)
    swDisplayStateSetting.Entities = swComponents
    swDisplayStateSetting.Option = swSpecifyDisplayState
    displayStateNames(0) = "<Default>_Display State 1"
    swDisplayStateSetting.Names = displayStateNames
    'Set to part level
    swDisplayStateSetting.PartLevel = True
```

```
    'Change the selected component's, USB_cover1, part-level
    'color from red to green in the specified display state of
    'the component part; this is not the overriding color level
    appearances = swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting)
    Set swAppearanceSetting = appearances(0)
    red_rgb = 0
    green_rgb = 255
    blue_rgb = 0
    newColor = Excel.WorksheetFunction.Max(Excel.WorksheetFunction.Min(red_rgb, 255), 0) + Excel.WorksheetFunction.Max(Excel.WorksheetFunction.Min(green_rgb, 255), 0) * 16 * 16 + Excel.WorksheetFunction.Max(Excel.WorksheetFunction.Min(blue_rgb, 255), 0) * 16 * 16 * 16 * 16
    swAppearanceSetting.Color = newColor
```

swAppearanceSetting. Diffuse = 0.8

swAppearanceSetting. Specular = 0.5

swAppearanceSetting. SpecularColor = newColor

swAppearanceSetting. Luminous = 0.1

swAppearanceSetting. Transparent = 0.0

```
    Set newAppearances(0) = swAppearanceSetting
    swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting) = newAppearances
```

```
    Stop
    'Examine the Appearance column to see the level
    'where the appearance color was applied
    'Press F5 to continue
```

```
    'Close the assembly document without saving
    'changes
    swApp.CloseDoc "usb_flash_drive1"
```

```
    'Open the assembly component USB_cover1 as a part document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\appearances\usb_cover1.sldprt"
    Set swModelDoc = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    Set swModelDocExt = swModelDoc.Extension
    Set swSelMgr = swModelDoc.SelectionManager
    Set swConfigMgr = swModelDoc.ConfigurationManager
    Set swConfig = swConfigMgr.ActiveConfiguration
```

```
    Set swComponents(0) = Nothing
    Set swComponents(0) = swConfig.GetRootComponent3(True)
```

```
    swModelDoc.ClearSelection2 True
```

```
    'Get display state
    Set swDisplayStateSetting = Nothing
    Set swDisplayStateSetting = swModelDocExt.GetDisplayStateSetting(swAllDisplayState)
    swDisplayStateSetting.Entities = swComponents
    swDisplayStateSetting.Option = swSpecifyDisplayState
    displayStateNames(0) = "<Default>_Display State 1"
    swDisplayStateSetting.Names = displayStateNames
```

```
    Stop
    'Examine the graphics area
    'Press F5 to continue
```

```
    'Change color of selected component in specified display state
    'from default red to green; this is the overriding color
    appearances = swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting)
    Set swAppearanceSetting = Nothing
    Set swAppearanceSetting = appearances(0)
    red_rgb = 0
    green_rgb = 255
    blue_rgb = 0
    newColor = Excel.WorksheetFunction.Max(Excel.WorksheetFunction.Min(red_rgb, 255), 0) + Excel.WorksheetFunction.Max(Excel.WorksheetFunction.Min(green_rgb, 255), 0) * 16 * 16 + Excel.WorksheetFunction.Max(Excel.WorksheetFunction.Min(blue_rgb, 255), 0) * 16 * 16 * 16 * 16
    swAppearanceSetting.Color = newColor
```

swAppearanceSetting. Diffuse = 0.8

swAppearanceSetting. Specular = 0.5

swAppearanceSetting. SpecularColor = newColor

swAppearanceSetting. Luminous = 0.1

swAppearanceSetting. Transparent = 0.0

```
    Set newAppearances(0) = swAppearanceSetting
    swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting) = newAppearances
```

```
    Stop
    'Examine the graphics area
    'Press F5 to continue
```

```
    'Close the part document without saving
    'changes
    swApp.CloseDoc "usb_cover1"
```

```
End Sub
```
