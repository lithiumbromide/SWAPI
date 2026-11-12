---
title: "Get and Set Datum Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Datum_Example_VB.htm"
---

# Get and Set Datum Example (VBA)

This example shows how to get and set DimXpert datum annotations.

'---------------------------------------------------------------------------
' Preconditions:
' 1. Open: `public_documents`**\samples\tutorial\dimxpert\bracket_auto_manual.sldprt.**
' 2. Select a face.
' 3. Open an Immediate window.
' 4. Ensure that the latest SOLIDWORKS DimXpert type library is loaded:
' a. click **Tools > References**.
' b. Click Browse.
' c. Find and select `install_dir`**\swdimxpert.tlb**.
'
' Postconditions:
' 1. Inspect the Immediate window.
' 2. Observe Plane1 and Datum G on the DimXpertManager tab.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'--------------------------------------------------------------------------------------

```vb
Option Explicit
 Dim dimXpertPart As dimXpertPart
Sub Main()
    Dim swapp As SldWorks.SldWorks
     Set swapp = Application.SldWorks
     Dim swModelDoc As SldWorks.ModelDoc2
     Set swModelDoc = swapp.ActiveDoc
   If swModelDoc Is Nothing Then
      Exit Sub
    End If
    Dim dimXpertMgr As SldWorks.DimXpertManager
     Set dimXpertMgr = swapp.IActiveDoc2.Extension.DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name, True)
     Debug.Print "Model: " & swapp.IActiveDoc2.GetPathName
    Dim dimXpertPartObj As dimXpertPart
    Set dimXpertPartObj = dimXpertMgr.dimXpertPart
     Set dimXpertPart = dimXpertPartObj

    Dim dimOption As DimXpertDimensionOption
     Set dimOption = dimXpertPart.GetDimOption
     dimOption.DatumLength = 0.06
     Dim dimarray(0) As Long
     dimarray(0) = 0
     Dim dimvar As Variant
     dimvar = dimarray
     dimOption.FeatureSelectorOptions = dimvar
    ' Insert datum
     dimXpertPart.InsertDatum dimOption

    Dim vAnnotations As Variant
     vAnnotations = dimXpertPart.GetAnnotations()
    Debug.Print "------------------------"
     Debug.Print "Annotations..."
     Debug.Print "------------------------"
    Dim annotationTemp As DimXpertAnnotation
     Dim annotationIndex As Long
     For annotationIndex = 0 To UBound(vAnnotations)
         Set annotationTemp = vAnnotations(annotationIndex)
         Call AnnotationData(annotationTemp)
     Next
End Sub
 Public Sub AnnotationData(annotation As DimXpertAnnotation)
    Dim annoType As Long
    'general info
     Call GeneralInfo(annotation)
     annoType = annotation.Type
    If annoType = swDimXpertDatum Then
         Call DatumData(annotation)
    End If
End Sub

Private Sub GeneralInfo(annotation As DimXpertAnnotation)
    Dim annoType As String
     Dim modelObj As Object
     Dim modelFeature As SldWorks.Feature
    Debug.Print ("")
     Debug.Print ("Name: " + annotation.Name)
    annoType = annotationTypeNameFromObject(annotation)
    Debug.Print ("Type: " + annoType)
     Debug.Print ("Display Entity: " + DisplayEntity(annotation))

     Set modelObj = annotation.GetModelFeature
     Set modelFeature = modelObj
    If Not (modelFeature Is Nothing) Then
         Debug.Print ("ModelFeature: " + modelFeature.Name + " (" + modelFeature.GetTypeName2() + ")")
     End If
End Sub
Private Sub DatumData(annotation As DimXpertDatum)
    ' the datum letter
     Debug.Print ("")
     Debug.Print ("Datum Letter:  " + annotation.Identifier)
End Sub
Private Function annotationTypeNameFromObject(anno As DimXpertAnnotation) As String
     annotationTypeNameFromObject = annotationTypeNameFromTypeNumber(anno.Type)
 End Function
Private Function annotationTypeNameFromTypeNumber(annoTypeIndex As Long) As String
     Select Case annoTypeIndex
    Case swDimXpertDimTol_DistanceBetween
         annotationTypeNameFromTypeNumber = "DistanceBetween Dim"
     Case swDimXpertDimTol_CounterBore
         annotationTypeNameFromTypeNumber = "CounterBore Dim"
     Case swDimXpertDimTol_Depth
         annotationTypeNameFromTypeNumber = "Depth Dim"
     Case swDimXpertDimTol_CounterSinkDiameter
         annotationTypeNameFromTypeNumber = "CounterSinkDiameter Dim"
     Case swDimXpertDimTol_ChamferDimension
         annotationTypeNameFromTypeNumber = "ChamferDimension Dim"
     Case swDimXpertDimTol_AngleBetween
         annotationTypeNameFromTypeNumber = "AngleBetween Dim"
     Case swDimXpertDimTol_CounterSinkAngle
         annotationTypeNameFromTypeNumber = "CounterSinkAngle Dim"
     Case swDimXpertDimTol_ConeAngle
         annotationTypeNameFromTypeNumber = "ConeAngle Dim"
     Case swDimXpertDimTol_Diameter
         annotationTypeNameFromTypeNumber = "Diameter Dim"
     Case swDimXpertDimTol_Length
         annotationTypeNameFromTypeNumber = "Length Dim"
     Case swDimXpertDimTol_Radius
         annotationTypeNameFromTypeNumber = "Radius Dim"
     Case swDimXpertDimTol_Width
         annotationTypeNameFromTypeNumber = "Width Dim"
     Case swDimXpertDimTol_CompositeDistanceBetween
         annotationTypeNameFromTypeNumber = "CompositeDistanceBetween Dim"
    Case swDimXpertDatum
         annotationTypeNameFromTypeNumber = "Datum"
    Case swDimXpertGeoTol_Position
         annotationTypeNameFromTypeNumber = "Position Tol"
     Case swDimXpertGeoTol_CompositePosition
         annotationTypeNameFromTypeNumber = "CompositePosition Tol"
     Case swDimXpertGeoTol_Symmetry
         annotationTypeNameFromTypeNumber = "Symmetry Tol"
     Case swDimXpertGeoTol_Concentricity
         annotationTypeNameFromTypeNumber = "Concentricity Tol"
     Case swDimXpertGeoTol_LineProfile
         annotationTypeNameFromTypeNumber = "LineProfile Tol"
     Case swDimXpertGeoTol_CompositeLineProfile
         annotationTypeNameFromTypeNumber = "CompositeLineProfile Tol"
     Case swDimXpertGeoTol_SurfaceProfile
         annotationTypeNameFromTypeNumber = "SurfaceProfile Tol"
     Case swDimXpertGeoTol_CompositeSurfaceProfile
         annotationTypeNameFromTypeNumber = "CompositeSurfaceProfile Tol"
     Case swDimXpertGeoTol_Angularity
         annotationTypeNameFromTypeNumber = "Angularity Tol"
     Case swDimXpertGeoTol_Parallelism
         annotationTypeNameFromTypeNumber = "Parallelism Tol"
     Case swDimXpertGeoTol_Perpendicularity
         annotationTypeNameFromTypeNumber = "Perpendicularity Tol"
     Case swDimXpertGeoTol_TotalRunout
         annotationTypeNameFromTypeNumber = "TotalRunout Tol"
     Case swDimXpertGeoTol_CircularRunout
         annotationTypeNameFromTypeNumber = "CircularRunout Tol"
     Case swDimXpertGeoTol_Flatness
         annotationTypeNameFromTypeNumber = "Flatness Tol"
     Case swDimXpertGeoTol_Circularity
         annotationTypeNameFromTypeNumber = "Circularity Tol"
     Case swDimXpertGeoTol_Cylindricity
         annotationTypeNameFromTypeNumber = "Cylindricity Tol"
     Case swDimXpertGeoTol_Straightness
         annotationTypeNameFromTypeNumber = "Straightness Tol"
     Case swDimXpertGeoTol_Tangency
         annotationTypeNameFromTypeNumber = "Tangency Tol"
     Case Else
         annotationTypeNameFromTypeNumber = "<unknown> " & CStr(annoTypeIndex)
    End Select

    ' returns a string containing the names of the SW display entities
 End Function
 Private Function DisplayEntity(annotation As DimXpertAnnotation) As String
    Dim str As String
     Dim dispEnt As Object
     Dim swAnnot As SldWorks.annotation
     Set dispEnt = annotation.GetDisplayEntity
     If Not dispEnt Is Nothing Then
         If TypeOf dispEnt Is SldWorks.annotation Then
             Set swAnnot = dispEnt
             str = swAnnot.GetName
         End If
     End If
     DisplayEntity = str
 End Function
```
