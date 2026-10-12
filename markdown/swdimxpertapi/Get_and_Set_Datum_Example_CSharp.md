---
title: "Get and Set Datum Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Datum_Example_CSharp.htm"
---

# Get and Set Datum Example (C#)

This example shows how to get and set DimXpert datum annotations.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\dimxpert\bracket_auto_manual.sldprt.
 // 2. Select a face.
 // 3. Open an Immediate window.
 // 4. Ensure that the SOLIDWORKS DimXpert interop assembly is referenced:
 //    a. Right-click the project in Project Explorer.
 //    b. Select Add Reference.
 //    c. Click the Browse tab.
 //    d. Find and select install_dir\api\redist\swdimxpert.dll.
 //
 // Postconditions:
 // 1. Inspect the Immediate window.
 // 2. Observe Plane1 and datum G on the DimXpertManager tab.
 //
 // NOTE: Because this part is elsewhere, do not save changes.
 //-------------------------------------------------- ------------------------
```

```vb
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swdimxpert;
 using System;
 using System.Diagnostics;
 namespace InsertDatum_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         DimXpertPart dimXpertPart;

         public void Main()
         {

             ModelDoc2 swModelDoc = default(ModelDoc2);
             swModelDoc = (ModelDoc2)swApp.ActiveDoc;

             if (swModelDoc == null)
             {
                 return;
             }

             DimXpertManager dimXpertMgr = default(DimXpertManager);
             dimXpertMgr = swApp.IActiveDoc2.Extension.get_DimXpertManager(swApp.IActiveDoc2.IGetActiveConfiguration().Name, true);
             Debug.Print("Model: " + swApp.IActiveDoc2.GetPathName());

             DimXpertPart dimXpertPartObj = default(DimXpertPart);

             dimXpertPartObj = (DimXpertPart)dimXpertMgr.DimXpertPart;
             dimXpertPart = dimXpertPartObj;

             DimXpertDimensionOption dimOption = default(DimXpertDimensionOption);
             dimOption = dimXpertPart.GetDimOption();
             dimOption.DatumLength = 0.06;
             int[] dimarray = new int[1];
             dimarray[0] = 0;
             object dimvar = null;
             dimvar = dimarray;
             dimOption.FeatureSelectorOptions = dimvar;

             // Insert datum
             dimXpertPart.InsertDatum(dimOption);

             object[] vAnnotations = null;
             vAnnotations = (object[])dimXpertPart.GetAnnotations();

             Debug.Print("------------------------");
             Debug.Print("Annotations...");
             Debug.Print("------------------------");

             DimXpertAnnotation annotationTemp = default(DimXpertAnnotation);
             int annotationIndex = 0;
             for (annotationIndex = 0; annotationIndex <= vAnnotations.GetUpperBound(0); annotationIndex++)
             {
                 annotationTemp = (DimXpertAnnotation)vAnnotations[annotationIndex];
                 AnnotationData(annotationTemp);

             }
         }
         public void AnnotationData(DimXpertAnnotation annotation)
         {

             swDimXpertAnnotationType_e annoType = 0;

             //general info
             GeneralInfo(annotation);
             annoType = annotation.Type;

             if (annoType == swDimXpertAnnotationType_e.swDimXpertDatum)
             {

                 DatumData((DimXpertDatum)annotation);

             }
         }

         private void GeneralInfo(DimXpertAnnotation annotation)
         {

             string annoType = null;
             object modelObj = null;
             Feature modelFeature = default(Feature);

             Debug.Print("");
             Debug.Print("Name: " + annotation.Name);

             annoType = annotationTypeNameFromObject(annotation);

             Debug.Print("Type: " + annoType);
             Debug.Print("Display Entity: " + DisplayEntity(annotation));

             modelObj = annotation.GetModelFeature();
             modelFeature = (Feature)modelObj;

             if ((modelFeature != null))
             {
                 Debug.Print("ModelFeature: " + modelFeature.Name +  " (" + modelFeature.GetTypeName2() + ")");

             }
         }

         private void DatumData(DimXpertDatum annotation)
         {

             // the datum letter
             Debug.Print("");

             Debug.Print("Datum Letter: " + annotation.Identifier);
         }

         private string annotationTypeNameFromObject(DimXpertAnnotation anno)
         {
             return annotationTypeNameFromTypeNumber(anno.Type);
         }

         private string annotationTypeNameFromTypeNumber(swDimXpertAnnotationType_e annoTypeIndex)
         {
             string functionReturnValue = null;
             switch (annoTypeIndex)
             {

                 case swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween:
                     functionReturnValue =  "DistanceBetween Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterBore:
                     functionReturnValue =  "CounterBore Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_Depth:
                     functionReturnValue =  "Depth Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkDiameter:
                     functionReturnValue =  "CounterSinkDiameter Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_ChamferDimension:
                     functionReturnValue =  "ChamferDimension Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween:
                     functionReturnValue =  "AngleBetween Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkAngle:
                     functionReturnValue =  "CounterSinkAngle Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_ConeAngle:
                     functionReturnValue =  "ConeAngle Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_Diameter:
                     functionReturnValue =  "Diameter Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_Length:
                     functionReturnValue =  "Length Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_Radius:
                     functionReturnValue =  "Radius Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_Width:
                     functionReturnValue =  "Width Dim";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_CompositeDistanceBetween:
                     functionReturnValue =  "CompositeDistanceBetween Dim";

                     break;
                 case swDimXpertAnnotationType_e.swDimXpertDatum:
                     functionReturnValue =  "Datum";

                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_Position:
                     functionReturnValue =  "Position Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositePosition:
                     functionReturnValue =  "CompositePosition Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_Symmetry:
                     functionReturnValue =  "Symmetry Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_Concentricity:
                     functionReturnValue =  "Concentricity Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_LineProfile:
                     functionReturnValue =  "LineProfile Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeLineProfile:
                     functionReturnValue =  "CompositeLineProfile Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_SurfaceProfile:
                     functionReturnValue =  "SurfaceProfile Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeSurfaceProfile:
                     functionReturnValue =  "CompositeSurfaceProfile Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity:
                     functionReturnValue =  "Angularity Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism:
                     functionReturnValue =  "Parallelism Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity:
                     functionReturnValue =  "Perpendicularity Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_TotalRunout:
                     functionReturnValue =  "TotalRunout Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_CircularRunout:
                     functionReturnValue =  "CircularRunout Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_Flatness:
                     functionReturnValue =  "Flatness Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_Circularity:
                     functionReturnValue =  "Circularity Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_Cylindricity:
                     functionReturnValue =  "Cylindricity Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_Straightness:
                     functionReturnValue =  "Straightness Tol";
                     break;
                 case swDimXpertAnnotationType_e.swDimXpertGeoTol_Tangency:
                     functionReturnValue =  "Tangency Tol";
                     break;
                 default:
                     functionReturnValue =  "<unknown> " + annoTypeIndex.ToString();

                     break;
             }

             return functionReturnValue;
         }
         private string DisplayEntity(DimXpertAnnotation annotation)
         {

             string str = null;
             object dispEnt = null;
             Annotation swAnnot = default(Annotation);
             str = null;
             dispEnt = annotation.GetDisplayEntity();
             if ((dispEnt != null))
             {
                 if (dispEnt is Annotation)
                 {
                     swAnnot = (Annotation)dispEnt;
                     str = swAnnot.GetName();
                 }
             }
             return str;
         }

         public SldWorks swApp;

     }
 }
```
