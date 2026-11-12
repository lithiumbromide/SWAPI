---
title: "Get and Set Datum Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Datum_Example_VBNET.htm"
---

# Get and Set Datum Example (VB.NET)

This example shows how to get and set DimXpert datum annotations.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\dimxpert\bracket_auto_manual.sldprt.
 ' 2. Select a face.
 ' 3. Open an Immediate window.
 ' 4. Ensure that the latest SOLIDWORKS DimXpert interop assembly is referenced:
 '    a. Right-click the project in Project Explorer.
 '    b. Select Add Reference.
 '    c. Click the Browse tab.
 '    d. Find and select install_dir\api\redist\swdimxpert.dll.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window.
 ' 2. Observe Plane1 and datum G on the DimXpertManager tab.
 '
 ' NOTE: Because this part is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swdimxpert
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim dimXpertPart As dimXpertPart

     Sub Main()

         Dim swModelDoc As ModelDoc2
         swModelDoc = swapp.ActiveDoc

         If swModelDoc Is Nothing Then
             Exit Sub
         End If

         Dim dimXpertMgr As DimXpertManager
         dimXpertMgr = swapp.IActiveDoc2.Extension.DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name, True)
         Debug.Print("Model: " & swapp.IActiveDoc2.GetPathName)

         Dim dimXpertPartObj As dimXpertPart

         dimXpertPartObj = dimXpertMgr.dimXpertPart
         dimXpertPart = dimXpertPartObj

         Dim dimOption As DimXpertDimensionOption
         dimOption = dimXpertPart.GetDimOption
         dimOption.DatumLength = 0.06
         Dim dimarray(0) As Long
         dimarray(0) = 0
         Dim dimvar As Object
         dimvar = dimarray
         dimOption.FeatureSelectorOptions = dimvar

         ' Insert datum
         dimXpertPart.InsertDatum(dimOption)

         Dim vAnnotations As Object
         vAnnotations = dimXpertPart.GetAnnotations()

         Debug.Print("------------------------")
         Debug.Print("Annotations...")
         Debug.Print("------------------------")

         Dim annotationTemp As DimXpertAnnotation
         Dim annotationIndex As Long
         For annotationIndex = 0 To UBound(vAnnotations)
             annotationTemp = vAnnotations(annotationIndex)
             Call AnnotationData(annotationTemp)
         Next

     End Sub
     Public Sub AnnotationData(ByVal annotation As DimXpertAnnotation)

         Dim annoType As Long

         'general info
         Call GeneralInfo(annotation)
         annoType = annotation.Type

         If annoType = swDimXpertAnnotationType_e.swDimXpertDatum  Then
             Call DatumData(annotation)

         End If

     End Sub

     Private Sub GeneralInfo(ByVal annotation As DimXpertAnnotation)

         Dim annoType As String
         Dim modelObj As Object
         Dim modelFeature As Feature

         Debug.Print("")
         Debug.Print("Name: " + annotation.Name)

         annoType = annotationTypeNameFromObject(annotation)

         Debug.Print("Type: " + annoType)
         Debug.Print("Display Entity: " + DisplayEntity(annotation))

         modelObj = annotation.GetModelFeature
         modelFeature = modelObj

         If Not (modelFeature Is  Nothing)  Then
             Debug.Print("ModelFeature: " + modelFeature.Name +  " (" + modelFeature.GetTypeName2() + ")")
         End If

     End Sub

     Private Sub DatumData(ByVal annotation As DimXpertDatum)

         ' the datum letter
         Debug.Print("")
         Debug.Print("Datum Letter:  " + annotation.Identifier)

     End Sub

     Private Function annotationTypeNameFromObject(ByVal anno As DimXpertAnnotation) As String
         annotationTypeNameFromObject = annotationTypeNameFromTypeNumber(anno.Type)
     End Function

     Private Function annotationTypeNameFromTypeNumber(ByVal annoTypeIndex As Long) As  String
         Select Case annoTypeIndex

             Case swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween
                 annotationTypeNameFromTypeNumber =  "DistanceBetween Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterBore
                 annotationTypeNameFromTypeNumber =  "CounterBore Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_Depth
                 annotationTypeNameFromTypeNumber =  "Depth Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkDiameter
                 annotationTypeNameFromTypeNumber =  "CounterSinkDiameter Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_ChamferDimension
                 annotationTypeNameFromTypeNumber =  "ChamferDimension Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween
                 annotationTypeNameFromTypeNumber =  "AngleBetween Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkAngle
                 annotationTypeNameFromTypeNumber =  "CounterSinkAngle Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_ConeAngle
                 annotationTypeNameFromTypeNumber =  "ConeAngle Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_Diameter
                 annotationTypeNameFromTypeNumber =  "Diameter Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_Length
                 annotationTypeNameFromTypeNumber =  "Length Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_Radius
                 annotationTypeNameFromTypeNumber =  "Radius Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_Width
                 annotationTypeNameFromTypeNumber =  "Width Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_CompositeDistanceBetween
                 annotationTypeNameFromTypeNumber =  "CompositeDistanceBetween Dim"

             Case swDimXpertAnnotationType_e.swDimXpertDatum
                 annotationTypeNameFromTypeNumber =  "Datum"

             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Position
                 annotationTypeNameFromTypeNumber =  "Position Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositePosition
                 annotationTypeNameFromTypeNumber =  "CompositePosition Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Symmetry
                 annotationTypeNameFromTypeNumber =  "Symmetry Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Concentricity
                 annotationTypeNameFromTypeNumber =  "Concentricity Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_LineProfile
                 annotationTypeNameFromTypeNumber =  "LineProfile Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeLineProfile
                 annotationTypeNameFromTypeNumber =  "CompositeLineProfile Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_SurfaceProfile
                 annotationTypeNameFromTypeNumber =  "SurfaceProfile Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeSurfaceProfile
                 annotationTypeNameFromTypeNumber =  "CompositeSurfaceProfile Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity
                 annotationTypeNameFromTypeNumber =  "Angularity Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism
                 annotationTypeNameFromTypeNumber =  "Parallelism Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity
                 annotationTypeNameFromTypeNumber =  "Perpendicularity Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_TotalRunout
                 annotationTypeNameFromTypeNumber =  "TotalRunout Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CircularRunout
                 annotationTypeNameFromTypeNumber =  "CircularRunout Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Flatness
                 annotationTypeNameFromTypeNumber =  "Flatness Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Circularity
                 annotationTypeNameFromTypeNumber =  "Circularity Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Cylindricity
                 annotationTypeNameFromTypeNumber =  "Cylindricity Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Straightness
                 annotationTypeNameFromTypeNumber =  "Straightness Tol"
             Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Tangency
                 annotationTypeNameFromTypeNumber =  "Tangency Tol"
             Case Else
                 annotationTypeNameFromTypeNumber = "<unknown> " & CStr(annoTypeIndex)

         End Select

     End Function
     Private Function DisplayEntity(ByVal annotation As DimXpertAnnotation) As String

         Dim str As String
         Dim dispEnt As Object
         Dim swAnnot As Annotation
         str = Nothing
         dispEnt = annotation.GetDisplayEntity
         If Not dispEnt Is  Nothing  Then
             If TypeOf dispEnt Is Annotation Then
                 swAnnot = dispEnt
                 str = swAnnot.GetName
             End If
         End If
         DisplayEntity = str
     End Function

     Public swApp As SldWorks

 End  Class
```
