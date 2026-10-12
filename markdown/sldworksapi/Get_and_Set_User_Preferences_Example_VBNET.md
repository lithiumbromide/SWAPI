---
title: "Get and Set User Preferences Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_User_Preferences_Example_VBNET.htm"
---

# Get and Set User Preferences Example (VB.NET)

This sample code demonstrates how to get and set various system options and document properties.

'---------------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing document.
' 2. Create a layer named **test** in the document.
' 3. Open an Immediate window.
'
' Postconditions:
' 1. Observe the new settings in the Immediate window.
' 2. Maps the value returned by the GetUserPreferenceInteger method
' to the corresponding enumerator member in the enumerator online help.
' 3. Click **Tools > Options** in SOLIDWORKS Design and verify the new settings.
'----------------------------------------------------------------------------

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro
    Public Sub main()
        Dim Part As Object
        Dim boolstatus As Boolean
        Dim swTextFormat As TextFormat
        Dim TextFormatObj As Object
        Dim ModelDocExtension As ModelDocExtension

        Part = swApp.ActiveDoc
        ModelDocExtension = Part.Extension

        'The following call demonstrates how to get and set a Tools > Options > System Options > General option

        'Custom property used as component description
        boolstatus = swApp.SetUserPreferenceStringValue(swUserPreferenceStringValue_e.swCustomPropertyUsedAsComponentDescription, "Status")
        Debug.Print("Tools > Options > System Options > General > Custom property used as component description: " & swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swCustomPropertyUsedAsComponentDescription))

        'The following calls demonstrate how to get and set Tools > Options > System Options > View options

        'Reverse mouse wheel zoom direction
        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swViewReverseWheelZoomDirection, True)
        Debug.Print("Tools > Options > System Options > View > Reverse mouse wheel zoom direction: " & swApp.GetUserPreferenceToggle(swUserPreferenceToggle_e.swViewReverseWheelZoomDirection))
        'View rotation - Arrow keys
        boolstatus = swApp.SetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewRotationArrowKeys, 0.2268928027593)
         '1 radian = 180º/p = 57.295779513º or approximately 57.3º
        Debug.Print("Tools > Options > System Options > View > Arrow keys: " & swApp.GetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewRotationArrowKeys) * 57.3) 'Convert to degrees
        'View rotation - Mouse speed
        boolstatus = swApp.SetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swViewRotationMouseSpeed, 56)
        Debug.Print("Tools > Options > System Options > View > Mouse speed: " & swApp.GetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swViewRotationMouseSpeed))
        'Transitions - View transition
        boolstatus = swApp.SetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewAnimationSpeed, 2.5)
        Debug.Print("Tools > Options > System Options > View > View transition: " & swApp.GetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewAnimationSpeed))
        'Transitions - Hide/show component
        boolstatus = swApp.SetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewTransitionHideShowComponent, 0.8000000119209)
        Debug.Print("Tools > Options > System Options > View > Hide/show component: " & swApp.GetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewTransitionHideShowComponent))
        'Transitions - Isolate
        boolstatus = swApp.SetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewTransitionIsolate, 1.222222208977)
        Debug.Print("Tools > Options > System Options > View > Isolate: " & swApp.GetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewTransitionIsolate))

        'The following calls demonstrate how to set the Tools > Options > Document Properties > Drafting Standard option using
        'SetUserPreferenceInteger
        'Maps the value returned by the GetUserPreferenceInteger method to the corresponding enumerator member in the enumerator online help.

        'Overall drafting standard
        boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingDimensionStandard, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDetailingStandard_e.swDetailingStandardISO)
        Dim sText As String
        sText = "Tools > Options > Document Properties > Drafting Standard > Overall drafting standard is "
        Select Case ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingDimensionStandard, swUserPreferenceOption_e.swDetailingNoOptionSpecified)
            Case 1
                Debug.Print(sText & "ANSI")
            Case 2
                Debug.Print(sText & "ISO")
            Case 3
                Debug.Print(sText & "DIN")
            Case 4
                Debug.Print(sText & "JIS")
            Case 5
                Debug.Print(sText & "BS")
            Case 6
                Debug.Print(sText & "GOST")
            Case 7
                Debug.Print(sText & "GB")
            Case 8
                Debug.Print(sText & "User Defined")
        End Select

        'The following calls demonstrate how to set and get Tools > Options > Document Properties > Annotations > Balloons options
        'Maps the value returned by the GetUserPreferenceInteger method to the corresponding enumerator member in the enumerator online help

        'Leader style - Leader Thickness
        boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBalloonLeaderLineThickness, 0, swLineWeights_e.swLW_NUMBER)
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Leader Thickness: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBalloonLeaderLineThickness, 0))
        'Leader style - Custom leader thickness
        boolstatus = ModelDocExtension.SetUserPreferenceDouble(swUserPreferenceDoubleValue_e.swDetailingBalloonLeaderLineThicknessCustom, 0, 0.00028)
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Custom Leader Thickness: " & ModelDocExtension.GetUserPreferenceDouble(swUserPreferenceDoubleValue_e.swDetailingBalloonLeaderLineThicknessCustom, 0))
        'Frame style - Frame Thickness
        boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBalloonFrameLineThickness, 0, swLineWeights_e.swLW_NUMBER)
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Frame Thickness: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBalloonFrameLineThickness, 0))
        'Frame style - Custom frame thickness
        boolstatus = ModelDocExtension.SetUserPreferenceDouble(swUserPreferenceDoubleValue_e.swDetailingBalloonFrameLineThicknessCustom, 0, 0.00028)
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Custom Frame Thickness: " & ModelDocExtension.GetUserPreferenceDouble(swUserPreferenceDoubleValue_e.swDetailingBalloonFrameLineThicknessCustom, 0))
        'Text - Upper - Custom property
        boolstatus = ModelDocExtension.SetUserPreferenceString(swUserPreferenceStringValue_e.swDetailingBOMUpperCustomProperty, 0, "Source")
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Text Upper Custom property: " & ModelDocExtension.GetUserPreferenceString(swUserPreferenceStringValue_e.swDetailingBOMUpperCustomProperty, 0))
        'Single balloon - Style
        boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMBalloonStyle, 0, swBalloonStyle_e.swBS_Triangle)
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Single balloon - Style: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMBalloonStyle, 0))
        'Single balloon - Size
        boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMBalloonFit, 0, swBalloonFit_e.swBF_3Chars)
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Single balloon - Size: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMBalloonFit, 0))
        'Stacked balloons - Style
        boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonStyle, 0, swBalloonStyle_e.swBS_Triangle)
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Stacked balloons - Style: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonStyle, 0))
        'Stacked balloons - Size
        boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonFit, 0, swBalloonFit_e.swBF_3Chars)
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Stacked balloons - Size: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonFit, 0))
        'Auto balloon layout
        boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingAutoBalloonLayout, 0, swBalloonLayoutType_e.swDetailingBalloonLayout_Right)
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Auto balloon layout: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingAutoBalloonLayout, 0))
        'Leader display - Use document leader length
        boolstatus = ModelDocExtension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swDetailingBalloonUseDocBentLeaderLength, 0, True)
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Leader display - Use document leader length: " & ModelDocExtension.GetUserPreferenceToggle(swUserPreferenceToggle_e.swDetailingBalloonUseDocBentLeaderLength, 0))
        'Layer
        boolstatus = ModelDocExtension.SetUserPreferenceString(swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingBalloon, "test")
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Layer: " & ModelDocExtension.GetUserPreferenceString(swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingBalloon))
        'Font...
        TextFormatObj = ModelDocExtension.GetUserPreferenceTextFormat(swUserPreferenceTextFormat_e.swDetailingBalloonTextFormat, 0)
        swTextFormat = TextFormatObj
        swTextFormat.Italic = True
        swTextFormat.Bold = True
        boolstatus = ModelDocExtension.SetUserPreferenceTextFormat(swUserPreferenceTextFormat_e.swDetailingBalloonTextFormat, 0, swTextFormat)
        Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Font is italic and bold: " & boolstatus)
    End Sub

    Public swApp As SldWorks
End Class
```
