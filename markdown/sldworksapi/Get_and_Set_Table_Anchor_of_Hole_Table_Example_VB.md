---
title: "Get and Set Table Anchor of Hole Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm"
---

# Get and Set Table Anchor of Hole Table Example (VBA)

This example shows how to get and set the table anchor of a hole table in a drawing.

```
'-----------------------------------------------------------------
' Preconditions: Verify that the specified drawing to open exists.
'
' Postconditions:
' 1. Opens the drawing.
' 2. At Stop, examine the position of the hole table
'    in the drawing.
' 3. Click the Continue button in the SOLIDWORKS Microsoft Basic
'    for Applications IDE.
' 4. Sets the position of the hole table's anchor
'    to the specified location.
' 5. Examine the hole table in the drawing.
'
' NOTE: If prompted, do not save changes when closing the drawing.
'------------------------------------------------------------------
Option Explicit
```

```
Sub main()
    Dim swApp As SldWorks.SldWorks
    Set swApp = Application.SldWorks
```

```
    Dim filename As String
    filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\SimpleHole.slddrw"
```

```
    Dim model As ModelDoc2
    Dim errors As Long
    Dim warnings As Long
    Set model = swApp.OpenDoc6(filename, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    If model Is Nothing Then Exit Sub
```

```
    Stop
```

```
    Dim swTable As TableAnnotation
```

```
    ' If document is a drawing, then continue
    Select Case model.GetType
    Case swDocDRAWING
        Dim drw As DrawingDoc
        Set drw = model
```

```
        ' Get the current sheet
        Dim drwSheet As Sheet
        Set drwSheet = drw.GetCurrentSheet
```

```
        ' Select the Sheet2 feature
        Dim modeldocext As SldWorks.ModelDocExtension
        Dim status As Boolean
        Set modeldocext = model.Extension
        status = modeldocext.SelectByID2("Sheet2", "SHEET", 0, 0, 0, False, 0, Nothing, 0)
```

```
        ' Get the views on Sheet2
        Dim views As Variant
        views = drwSheet.GetViews
```

```
        Dim vView As Variant
        For Each vView In views
            Dim drwView As View
            Set drwView = vView
```

```
            Dim viewFeature As Feature
            Set viewFeature = drw.FeatureByName(drwView.Name)
```

```
            ' Traverse the features in the view
            Dim subFeature As Feature
            Set subFeature = viewFeature.GetFirstSubFeature
```

```
            ' If the feature is HoleTableFeat, then get the table annotations
            Do Until subFeature Is Nothing
                If subFeature.GetTypeName2 = "HoleTableFeat" Then
                    Dim swHoleTable As HoleTable
```

```
                    Set swHoleTable = subFeature.GetSpecificFeature2
                    Dim holeTables
                    holeTables = swHoleTable.GetTableAnnotations
```

```
                    ' If the annotation is a hole table, then continue
                    If Not IsEmpty(holeTables) Then
                        Dim table As Variant
                        For Each table In holeTables
                            Set swTable = table
```

```
                            ' If the hole table is anchored, then continue
                            If swTable.Type = swTableAnnotation_HoleChart Then
                                If swTable.Anchored <> False Then
                                    Dim holeTableAnchor As TableAnchor
                                    Set holeTableAnchor = drwView.Sheet.TableAnchor(swTableAnnotation_HoleChart)
```

```
                                    ' Get the position of the table anchor
                                    Dim anchorPosition
                                    anchorPosition = holeTableAnchor.Position
```

```
                                     ' Determine type of table anchor
                                    Dim newCorner As swBOMConfigurationAnchorType_e
```

```
                                    Dim corner As String
                                    Select Case swTable.AnchorType
                                    Case swBOMConfigurationAnchor_BottomLeft
                                        corner = "  Bottom-left "
                                        newCorner = swBOMConfigurationAnchor_TopRight
                                    Case swBOMConfigurationAnchor_BottomRight
                                        corner = "  Bottom-right "
                                        newCorner = swBOMConfigurationAnchor_TopLeft
                                    Case swBOMConfigurationAnchor_TopLeft
                                        corner = "  Top-left "
                                        newCorner = swBOMConfigurationAnchor_BottomRight
                                    Case swBOMConfigurationAnchor_TopRight
                                        corner = "  Top-right "
                                        newCorner = swBOMConfigurationAnchor_BottomLeft
                                    End Select
```

```
                                    swTable.AnchorType = newCorner
```

```
                                    ' Set the new position of the table anchor
                                    Dim dNewPosition(0 To 1) As Double
                                    dNewPosition(0) = 0#
                                    dNewPosition(1) = 0#
```

```
                                    holeTableAnchor.Position = dNewPosition
                                End If
                            End If
                        Next
                    End If
                End If
```

```
                Set subFeature = subFeature.GetNextSubFeature
            Loop
```

```
        Next
```

```
    Case swDocASSEMBLY, swDocPART
```

```
    End Select
```

```
End Sub
```
