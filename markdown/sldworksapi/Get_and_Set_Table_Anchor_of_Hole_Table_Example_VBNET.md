---
title: "Get and Set Table Anchor of Hole Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm"
---

# Get and Set Table Anchor of Hole Table Example (VB.NET)

This example shows how to get and set the table anchor of a hole table in a drawing.

```vb
 '-----------------------------------------------------------------
 ' Preconditions: Verify that the specified drawing to open exists.
 '
 ' Postconditions:
 ' 1. Opens the drawing.
 ' 2. At Stop, examine the position of the hole table
 '    in the drawing.
 ' 2. Click the Continue button in the SOLIDWORKS Visual Studio Tools for
 '    Applications IDE.
 ' 4. Sets the position of the hole table's anchor
 '    to the specified location.
 ' 5. Examine the hole table in the drawing.
 '
 ' NOTE: If prompted, do not save changes when closing the drawing.
 '------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim filename As String
         filename =  "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\SimpleHole.slddrw"

         Dim model As ModelDoc2
         Dim errors As Integer
         Dim warnings As Integer
         model = swApp.OpenDoc6(filename, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

         If model Is Nothing Then  Exit  Sub

         Stop

         Dim swTable As TableAnnotation

         ' If document is a drawing, then continue
         Select Case model.GetType
             Case swDocumentTypes_e.swDocDRAWING
                 Dim drw As DrawingDoc
                 drw = model

                 ' Get the current sheet
                 Dim drwSheet As Sheet
                 drwSheet = drw.GetCurrentSheet

                 ' Select the Sheet2 feature
                 Dim modeldocext As ModelDocExtension
                 Dim status As Boolean
                 modeldocext = model.Extension
                 status = modeldocext.SelectByID2("Sheet2", "SHEET", 0, 0, 0, False, 0, Nothing, 0)

                 ' Get the views on Sheet2
                 Dim views As Object
                 views = drwSheet.GetViews

                 Dim vView As Object
                 For Each vView In views
                     Dim drwView As View
                     drwView = vView

                     Dim viewFeature As Feature
                     viewFeature = drw.FeatureByName(drwView.Name)

                     ' Traverse the features in the view
                     Dim subFeature As Feature
                     subFeature = viewFeature.GetFirstSubFeature

                     ' If the feature is HoleTableFeat, then get the table annotations
                     Do Until subFeature Is Nothing
                         If subFeature.GetTypeName2 = "HoleTableFeat" Then
                             Dim swHoleTable As HoleTable

                             swHoleTable = subFeature.GetSpecificFeature2
                             Dim holeTables As Object
                             holeTables = swHoleTable.GetTableAnnotations

                             ' If the annotation is a hole table, then continue
                             If Not holeTables Is Nothing Then
                                 Dim table As Object
                                 For Each table In holeTables
                                     swTable = table

                                     ' If the hole table is anchored, then continue
                                     If swTable.Type = swTableAnnotationType_e.swTableAnnotation_HoleChart Then
                                         If swTable.Anchored <> False Then
                                              Dim holeTableAnchor As TableAnchor
                                             holeTableAnchor = drwView.Sheet.TableAnchor(swTableAnnotationType_e.swTableAnnotation_HoleChart)

                                             ' Get the position of the table anchor
                                              Dim anchorPosition As Object
                                              anchorPosition = holeTableAnchor.Position

                                             ' Determine type of table anchor
                                              Dim newCorner As swBOMConfigurationAnchorType_e

                                             Dim corner As String
                                              Select Case swTable.AnchorType
                                                 Case swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomLeft
                                                     corner =  "  Bottom-left "
                                                      newCorner = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopRight
                                                 Case swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomRight
                                                     corner =  "  Bottom-right "
                                                      newCorner = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft
                                                 Case swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft
                                                     corner =  "  Top-left "
                                                      newCorner = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomRight
                                                 Case swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopRight
                                                     corner =  "  Top-right "
                                                      newCorner = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomLeft
                                             End Select

                                              swTable.AnchorType = newCorner

                                             ' Set the new position of the table anchor
                                              Dim dNewPosition(0 To 1) As Double
                                              dNewPosition(0) = 0.0#
                                             dNewPosition(1) = 0.0#

                                             holeTableAnchor.Position = dNewPosition
                                         End If
                                     End If
                                 Next
                             End If
                         End If

                         subFeature = subFeature.GetNextSubFeature
                     Loop

                 Next

             Case swDocumentTypes_e.swDocASSEMBLY, swDocumentTypes_e.swDocPART

         End Select

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End  Class
```
