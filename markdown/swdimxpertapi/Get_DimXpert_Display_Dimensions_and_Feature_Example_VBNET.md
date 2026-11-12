---
title: "Get DimXpert Display Dimensions and Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm"
---

# Get DimXpert Display Dimensions and Feature Example (VB.NET)

This example shows how to find out if an annotation is a DimXpert display dimension, and, if so, how to get its DimXpert feature.

```vb
'---------------------------------------------------------------------------
' Preconditions:
' 1. Add SolidWorks.Interop.swdimxpert.dll as a reference
'    (in the Project Explorer, right-click References and click Add Reference >
'     .NET tab).
' 2. Open public_documents\samples\tutorial\api\plate_tolstatus.sldprt
' 3. Click View > Toolbars > DimXpert.
' 4. Click Auto Dimension Scheme on the DimXpert toolbar.
' 5. Make sure Chamfer is selected in Feature Filters
'    on the Auto Dimension Scheme PropertyManager page,
'    then click the checkmark to close the page.
'
' Postconditions: Adds DimXpert display dimensions to the model.
'
' NOTE: Because this part document is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swdimxpert
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swPart As ModelDoc2
        Dim swAnnotation As Annotation
        Dim swDisplayDimension As DisplayDimension

        swPart = swApp.ActiveDoc
        swAnnotation = swPart.GetFirstAnnotation2
        Do While (Not (swAnnotation Is Nothing))
            Debug.Print(" ")
            Debug.Print("Annotation name = " & swAnnotation.GetName)
            If swAnnotationType_e.swDisplayDimension = swAnnotation.GetType Then
                Debug.Print("  Is a display dimension? True")
                swDisplayDimension = swAnnotation.GetSpecificAnnotation
                Select Case (swDisplayDimension.Type2)
                    Case swDimensionType_e.swOrdinateDimension
                        Debug.Print("  Display dimension type = base ordinate and its subordinates")
                    Case swDimensionType_e.swLinearDimension
                        Debug.Print("  Display dimension type = linear")
                    Case swDimensionType_e.swAngularDimension
                        Debug.Print("  Display dimension type  = angular")
                    Case swDimensionType_e.swArcLengthDimension
                        Debug.Print("  Display dimension type = arc length")
                    Case swDimensionType_e.swRadialDimension
                        Debug.Print("  Display dimension type = radial")
                    Case swDimensionType_e.swDiameterDimension
                        Debug.Print("  Display dimension type = diameter")
                    Case swDimensionType_e.swHorOrdinateDimension
                        Debug.Print("  Display dimension type = horizontal ordinate")
                    Case swDimensionType_e.swVertOrdinateDimension
                        Debug.Print("  Display dimension type = vertical ordinate")
                    Case swDimensionType_e.swZAxisDimension
                        Debug.Print("  Display dimension type = z-axis")
                    Case swDimensionType_e.swChamferDimension
                        Debug.Print("  Display dimension type = chamfer dimension")
                    Case swDimensionType_e.swHorLinearDimension
                        Debug.Print("  Display dimension type = horizonal linear")
                    Case swDimensionType_e.swVertLinearDimension
                        Debug.Print("  Display dimension type = vertical linear")
                    Case swDimensionType_e.swScalarDimension
                        Debug.Print("  Display dimension type = scalar")
                    Case Else
                        Debug.Print("  Display dimension type = unknown")
                End Select
                Debug.Print("  Is a DimXpert display dimension? " & IIf(swDisplayDimension.IsDimXpert = False, "False", "True"))
                If swAnnotation.IsDimXpert Then
                    Dim DimXpertFeat As DimXpertFeature
                    Dim FeatName As String
                    DimXpertFeat = swAnnotation.GetDimXpertFeature()
                    If Not DimXpertFeat Is Nothing Then
                        FeatName = DimXpertFeat.Name
                        Debug.Print("  DimXpert feature name = " & FeatName)
                        Select Case (DimXpertFeat.Type)
                            Case swDimXpertFeatureType_e.swDimXpertFeature_Plane
                                Debug.Print("  DimXpert feature type = plane")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_Cylinder
                                Debug.Print("  DimXpert feature type = cylinder")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_Cone
                                Debug.Print("  DimXpert feature type = cone")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_Extrude
                                Debug.Print("  DimXpert feature type = extrude")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_Fillet
                                Debug.Print("  DimXpert feature type = fillet")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_Chamfer
                                Debug.Print("  DimXpert feature type = chamfer")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole
                                Debug.Print("  DimXpert feature type = compound hole")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth
                                Debug.Print("  DimXpert feature type = compound width")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch
                                Debug.Print("  DimXpert feature type = compound notch")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D
                                Debug.Print("  DimXpert feature type = compound closed-slot 3D")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint
                                Debug.Print("  DimXpert feature type = intersect point")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine
                                Debug.Print("  DimXpert feature type = intersect line")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle
                                Debug.Print("  DimXpert feature type = intersect circle")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane
                                Debug.Print("  DimXpert feature type = intersect plane")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_Pattern
                                Debug.Print("  DimXpert feature type = pattern")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_Sphere
                                Debug.Print("  DimXpert feature type = sphere")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane
                                Debug.Print("  DimXpert feature type = best-fit plane")
                            Case swDimXpertFeatureType_e.swDimXpertFeature_Surface
                                Debug.Print("  DimXpert feature type = surface")
                            Case Else
                                Debug.Print("  DimXpert feature type = unknown")
                        End Select
                    End If
                End If
            Else
                Debug.Print("  Not a display dimension")
            End If
            swAnnotation = swAnnotation.GetNext3
        Loop
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
