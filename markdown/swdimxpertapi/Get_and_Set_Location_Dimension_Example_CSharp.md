---
title: "Get and Set Location Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Location_Dimension_Example_CSharp.htm"
---

# Get and Set Location Dimension Example (C#)

This example shows how to get and set DimXpert distance-between or angle-between dimensions.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\dimxpert\bracket_ads_plusminus.sldprt.
 // 2. Multi-select two faces that:
 //    a. share a common edge to get the angle-between dimension.
 //    b. do not share a common edge to get the distance-between dimension.
 // 3. Open an Immediate window.
 // 4. Ensure that the latest SOLIDWORKS DimXpert interop assembly is referenced:
 //    a. Right-click the project in Project Explorer.
 //    b. Select Add Reference.
 //    c. Click the Browse tab.
 //    d. Find and select install_dir\api\redist\swdimxpert.dll.
 //
 // Postconditions:
 // 1. Inspect the Immediate window.
 // 2. Observe the DistanceBetween1 or AngleBetween1 annotation on
 //      the DimXpertManager tab.
 //
 // NOTE: Because this part is used elsewhere, do not save changes.
 //--------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swdimxpert;
 using System;
 using System.Diagnostics;

 namespace InsertLocationDimension_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         DimXpertPart dimXpertPart;
         public void Main()
         {

             ModelDoc2 swModelDoc = default(ModelDoc2);
             swModelDoc = (ModelDoc2)swApp.ActiveDoc;
             swDimXpertAnnotationType_e annoType = 0;

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

             // The following line applies to linear location dimensions only.
             dimOption.DimensionPositionOption = 0; // Specify a dimension aint the normal to the face

             // Insert the dimension
             dimXpertPart.InsertLocationDimension(dimOption);

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
                 GeneralInfo(annotationTemp);
                 annoType = annotationTemp.Type;
                 DimensionToleranceData((DimXpertDimensionTolerance)annotationTemp);
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

         private void DimensionToleranceData(DimXpertDimensionTolerance annotation)
         {

             bool isAngleType = false;
             swDimXpertAnnotationType_e annoType = default(swDimXpertAnnotationType_e);

             double upper = 0;
             double lower = 0;
             double plus = 0;
             double minus = 0;
             bool boolstatus = false;

             DimXpertAnnotation anno = (DimXpertAnnotation)annotation;
             annoType = anno.Type;
             isAngleType = false;

             Debug.Print(annoType.ToString());

             Debug.Print("");
             Debug.Print("Dimension Tolerance Compartment");

             if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween)
             {
                 DimXpertDistanceBetweenDimTol distancebetween = default(DimXpertDistanceBetweenDimTol);
                 distancebetween = (DimXpertDistanceBetweenDimTol)annotation;
                 DistanceBetweenData(distancebetween);
             }
             else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween)
             {
                 isAngleType = true;
                 IDimXpertAngleBetweenDimTol angleBetween = default(IDimXpertAngleBetweenDimTol);
                 angleBetween = (DimXpertAngleBetweenDimTol)annotation;

                 // the origin and tolerance feature
                 Debug.Print("Origin Feature: " + angleBetween.OriginFeature.Name);

                 // is supplement angle
                 Debug.Print("Supplement Angle: " + (angleBetween.Supplement ? "True" : "False"));
             }

             // conversion from radians to degrees when dimension type is angle

             double dbl = 0;
             if (isAngleType)
             {
                 dbl = 57.2957795130823;
             }
             else
             {
                 dbl = 1.0;
             }

             // the nominal, and upper and lower limits of size of the dimension

             Debug.Print("");
             Debug.Print("Compute Nominal Dimension: " + FormatDouble(annotation.GetNominalValue() * dbl));
             boolstatus = annotation.GetUpperAndLowerLimit(ref upper, ref lower);
             Debug.Print("Get Upper Limit: " + FormatDouble(upper * dbl));
             Debug.Print("Get Lower Limit: " + FormatDouble(lower * dbl));

             // the upper and lower tolerance value by type
             switch (annotation.DimensionType)
             {
                 case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockTolerance:
                     Debug.Print("Dimension Type: Block Tolerance");
                     break;
                 // block tolerance
                 case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal:
                     DimXpertBlockTolerances blockTols = default(DimXpertBlockTolerances);
                     blockTols = dimXpertPart.GetBlockTolerances();
                     switch (blockTols.Type)
                     {
                         case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch:
                             Debug.Print("Dimension Type: Block Tolerance No Nominal");
                             if (isAngleType)
                             {
                                 Debug.Print("Angular Block Tolerance");
                             }
                             else
                             {
                                 Debug.Print("Block Tolerance Decimal Places: " + (annotation.BlockToleranceDecimalPlaces.ToString()));
                             }
                             break;
                         case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768:
                             Debug.Print("Dimension Type: General Tolerance");
                             break;
                     }
                     break;
                 case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFits:
                     Debug.Print("Dimension Type: Limits and Fits");
                     break;
                 // limits and fits tolerance
                 case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFitsNoNominal:
                     Debug.Print("Dimension Type: Limits and Fits No Nominal");
                     Debug.Print("Limits and Fits: " + annotation.LimitsAndFitsCode);
                     break;
                 // limit dimension
                 case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_LimitDimension:
                     Debug.Print("Dimension Type: Limit Dimension");
                     boolstatus = annotation.GetUpperAndLowerLimit(ref upper, ref lower);
                     Debug.Print("Get Upper Limit: " + FormatDouble(upper * dbl));
                     Debug.Print("Get Lower Limit: " + FormatDouble(lower * dbl));
                     break;
                 case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MAXTolerance:
                     Debug.Print("Dimension Type: MAXTolerance");
                     break;
                 case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MINTolerance:
                     Debug.Print("Dimension Type: MINTolerance");
                     break;
                 case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_NoTolerance:
                     Debug.Print("Dimension Type: NoTolerance");
                     break;
                 case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusDimension:
                     Debug.Print("Dimension Type: Plus Minus Dimension");
                     break;
                 // plus and minus dimension
                 case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal:
                     Debug.Print("Dimension Type: Plus Minus No Nominal");
                     boolstatus = annotation.GetPlusAndMinusTolerance(ref plus, ref minus);
                     Debug.Print("Plus Tolerance: " + FormatDouble(plus * dbl));
                     Debug.Print("Minus Tolerance: " + FormatDouble(minus * dbl));
                     break;
             }
         }

         private void DistanceBetweenData(DimXpertDistanceBetweenDimTol annotation)
         {
             DimXpertFeature feature = default(DimXpertFeature);
             swDimXpertDistanceFosUsage_e featureFosUsage = 0;
             double I = 0;
             double J = 0;
             double K = 0;
             bool boolstatus = false;

             feature = null;
             // the origin and tolerance feature aint with their feature of size usage (min, max, center)
             boolstatus = annotation.GetOriginFeature(ref feature, ref featureFosUsage);

             Debug.Print("");
             Debug.Print("Origin Feature: " + feature.Name +  " @ " + FosUsage(featureFosUsage));
             boolstatus = annotation.GetFeature(ref feature, ref featureFosUsage);
             Debug.Print("Tolerance Feature: " + feature.Name +  " @ " + FosUsage(featureFosUsage));

             // The direction vector

             boolstatus = annotation.GetDirectionVector(ref I, ref J, ref K);
             Debug.Print("");
             Debug.Print("Direction Vector: " + FormatVector(I, J, K));
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
                 case swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween:
                     functionReturnValue =  "AngleBetween Dim";
                     break;
                 default:
                     functionReturnValue =  "Unknown";
                     break;
             }
             return functionReturnValue;
         }

         private string DisplayEntity(DimXpertAnnotation annotation)
         {
             string str = null;
             object dispEnt = null;
             Annotation swAnnot = default(Annotation);

             dispEnt = annotation.GetDisplayEntity();

             str = null;
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

         private string FosUsage(swDimXpertDistanceFosUsage_e value)
         {
             string str = null;
             switch (value)
             {
                 case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_Center:
                     str = "Center";
                     break;
                 case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MaximumSide:
                     str = "Max";
                     break;
                 case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MinimumSide:
                     str = "Min";
                     break;
                 default:
                     str = "N/A";
                     break;
             }
             return str;
         }

         private string FormatVector(double I, double J, double K)
         {
             string str = null;
             str = FormatDouble(I) + ", " + FormatDouble(J) + ", " + FormatDouble(K);
             return str;
         }

         private string FormatDouble(double value)
         {
             string str = null;
             str = value.ToString();
             return str;
         }

         private string RadiansToDegrees(double value)
         {
             string str = null;
             str = (value * 57.2957795130823).ToString();
             return str;
         }
         public SldWorks swApp;
     }
 }
```
