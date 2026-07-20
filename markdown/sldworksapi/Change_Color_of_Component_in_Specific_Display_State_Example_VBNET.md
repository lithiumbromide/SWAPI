---
title: "Change Color of Component in Specific Display State Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Color_of_Component_in_Specific_Display_State_Example_VBNET.htm"
---

# Change Color of Component in Specific Display State Example (VB.NET)

This example shows how to change the color of a:

- selected component in a
  specific display state at the assembly and part levels.
- component in its part document.

```
'------------------------------------------------------------------
' Postconditions: Verify that the specified assembly and part exist.
'
' Postconditions:
'  1. Opens the specified assembly document.
'  2. Examine the graphics areas, then press F5.
'  3. Changes the selected component's, USB_cover1,
'     assembly-level color from the default red
'     to gray in the specified display state. This
'     is the overriding color level.
'  4. Examine the component in the graphics area, then press F5.
'  5. Changes the selected component's, USB_cover1, part-level
'     color from red to green in the specified display state of
'     the component part. This is not the overriding color level.
'  6. Closes, but does not save, the assembly document.
'  7. Opens the component's part document, USB_cover1.sldprt.
'  8. Examine the graphics area, then press F5.
'  9. Changes the part's color from red to green in the specified
'     display state of the part. This is the overriding color
'     level.
' 10. Examine the graphics area, then press F5.
' 11. Closes, but does not save, the part document.
'------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModelDoc As ModelDoc2 = Nothing
        Dim swModelDocExt As ModelDocExtension = Nothing
        Dim swSelMgr As SelectionMgr = Nothing
        Dim swDisplayStateSetting As DisplayStateSetting = Nothing
        Dim swComponent As Component2 = Nothing
        Dim swComponents(0) As Component2
        Dim displayStateNames(0) As String
        Dim appearances As Object
        Dim swAppearanceSetting As AppearanceSetting
        Dim newAppearanceSetting(0) As AppearanceSetting
        Dim swConfigMgr As ConfigurationManager
        Dim swConfig As Configuration
        Dim status As Boolean = False
        Dim errors As Integer = 0
        Dim warnings As Integer = 0
        Dim fileName As String = ""
        Dim red_rgb As Integer = 0
        Dim green_rgb As Integer = 0
        Dim blue_rgb As Integer = 0
        Dim newColor As Integer = 0

        'Open assembly document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\appearances\usb_flash_drive1.sldasm"
        swModelDoc = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

	Stop
	'Examine the graphics area
	'Press F5 to continue

	'Select component, USB_cover1
        swModelDocExt = swModelDoc.Extension
        swSelMgr = swModelDoc.SelectionManager
        status = swModelDocExt.SelectByID2("USB_cover1-1@usb_flash_drive1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swComponent = swSelMgr.GetSelectedObject6(1, -1)
        swComponents(0) = swComponent

        swModelDoc.ClearSelection2(True)

        'Get display state
        swDisplayStateSetting = swModelDocExt.GetDisplayStateSetting(swDisplayStateOpts_e.swAllDisplayState)
        swDisplayStateSetting.Entities = swComponents
        swDisplayStateSetting.Option = swDisplayStateOpts_e.swSpecifyDisplayState
        displayStateNames(0) = "Display State-1"
        swDisplayStateSetting.Names = displayStateNames
        'Assembly level is default
        swDisplayStateSetting.PartLevel = False

        'Change the selected component's, USB_cover1,
        'assembly-level color from the default red
        'to gray in the specified display state; this
        'is the overriding color level
        appearances = swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting)
        swAppearanceSetting = appearances(0)
        red_rgb = 50
        green_rgb = 50
        blue_rgb = 50
        newColor = Math.Max(Math.Min(red_rgb, 255), 0) + Math.Max(Math.Min(green_rgb, 255), 0) * 16 * 16 + Math.Max(Math.Min(blue_rgb, 255), 0) * 16 * 16 * 16 * 16
        swAppearanceSetting.Color = newColor
```

swAppearanceSetting. Diffuse = 0.8

swAppearanceSetting. Specular = 0.5

swAppearanceSetting. SpecularColor = newColor

swAppearanceSetting. Luminous = 0.1

swAppearanceSetting. Transparent = 0.0

```
        newAppearanceSetting(0) = swAppearanceSetting
        swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting) = newAppearanceSetting

        Stop
        'Examine the component in the graphics area
        'Press F5 to continue

        swModelDoc.ClearSelection2(True)

        status = swModelDocExt.SelectByID2("USB_cover1-1@usb_flash_drive1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swComponent = swSelMgr.GetSelectedObject6(1, -1)
        swComponents(0) = swComponent

        swModelDoc.ClearSelection2(True)

        'Get display state
        swDisplayStateSetting = swModelDocExt.GetDisplayStateSetting(swDisplayStateOpts_e.swAllDisplayState)
        swDisplayStateSetting.Entities = swComponents
        swDisplayStateSetting.Option = swDisplayStateOpts_e.swSpecifyDisplayState
        displayStateNames(0) = "<Default>_Display State 1"
        swDisplayStateSetting.Names = displayStateNames
        'Set to part level
        swDisplayStateSetting.PartLevel = True

        'Change the selected component's, USB_cover1, part-level
        'color from red to green in the specified display state of
        'the component part; this is not the overriding color level
        appearances = swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting)
        swAppearanceSetting = appearances(0)
        red_rgb = 0
        green_rgb = 255
        blue_rgb = 0
        newColor = Math.Max(Math.Min(red_rgb, 255), 0) + Math.Max(Math.Min(green_rgb, 255), 0) * 16 * 16 + Math.Max(Math.Min(blue_rgb, 255), 0) * 16 * 16 * 16 * 16
        swAppearanceSetting.Color = newColor
```

swAppearanceSetting. Diffuse = 0.8

swAppearanceSetting. Specular = 0.5

swAppearanceSetting. SpecularColor = newColor

swAppearanceSetting. Luminous = 0.1

swAppearanceSetting. Transparent = 0.0

```
        newAppearanceSetting(0) = swAppearanceSetting
        swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting) = newAppearanceSetting

        'Close the assembly document without saving
        'changes
        swApp.CloseDoc("usb_flash_drive1")

        'Open the assembly component USB_cover1 as a part document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\appearances\usb_cover1.sldprt"
        swModelDoc = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        swModelDocExt = swModelDoc.Extension
        swSelMgr = swModelDoc.SelectionManager
        swConfigMgr = swModelDoc.ConfigurationManager
        swConfig = swConfigMgr.ActiveConfiguration

        swComponents(0) = Nothing
        swComponents(0) = swConfig.GetRootComponent3(True)

        swModelDoc.ClearSelection2(True)

        'Get display state
        swDisplayStateSetting = Nothing
        swDisplayStateSetting = swModelDocExt.GetDisplayStateSetting(swDisplayStateOpts_e.swAllDisplayState)
        swDisplayStateSetting.Entities = swComponents
        swDisplayStateSetting.Option = swDisplayStateOpts_e.swSpecifyDisplayState
        displayStateNames(0) = "<Default>_Display State 1"
        swDisplayStateSetting.Names = displayStateNames

        Stop
        'Examine the graphics area
        'Press F5 to continue

        'Change color of selected component in specified display state
        'from default red to green; this is the overriding color
        appearances = swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting)
        swAppearanceSetting = Nothing
        swAppearanceSetting = appearances(0)
        red_rgb = 0
        green_rgb = 255
        blue_rgb = 0
        newColor = Math.Max(Math.Min(red_rgb, 255), 0) + Math.Max(Math.Min(green_rgb, 255), 0) * 16 * 16 + Math.Max(Math.Min(blue_rgb, 255), 0) * 16 * 16 * 16 * 16
        swAppearanceSetting.Color = newColor
```

swAppearanceSetting. Diffuse = 0.8

swAppearanceSetting. Specular = 0.5

swAppearanceSetting. SpecularColor = newColor

swAppearanceSetting. Luminous = 0.1

swAppearanceSetting. Transparent = 0.0

```
        newAppearanceSetting(0) = swAppearanceSetting
        swModelDocExt.DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting) = newAppearanceSetting

        Stop
        'Examine the graphics area
        'Press F5 to continue

        'Close the part document without saving
        'changes
        swApp.CloseDoc("usb_cover1")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
