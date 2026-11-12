---
title: "Get DimXpert Display Dimensions and Feature (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm"
---

# Get DimXpert Display Dimensions and Feature (C#)

This example shows how to find out if an annotation is a DimXpert display dimension, and, if so, how to get its DimXpert feature.

```vb
//---------------------------------------------------------------------------
// Preconditions:
// 1. Add SolidWorks.Interop.swdimxpert.dll as a reference
//   (in the Project Explorer, right-click References and click Add Reference).
// 2. Open public_documents\samples\tutorial\api\plate_tolstatus.sldprt.
// 3. Click View > Toolbars > DimXpert.
// 4. Click Auto Dimension Scheme on the DimXpert toolbar.
// 5. Make sure Chamfer is selected in Feature Filters
//    on the Auto Dimension Scheme PropertyManager page, then
//    click the checkmark to close the page.
//
// Postconditions: Adds DimXpert display dimensions o the model.
//
// NOTE: Because this part document is used elsewhere, do not save changes.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdimxpert;
using System;
using System.Diagnostics;
namespace GetDimXpertFeatureAnnotationCSharp.csproj
{
partial class SolidWorksMacro
{
    public void Main()
    {
        ModelDoc2 swPart = default(ModelDoc2);
        Annotation swAnnotation = default(Annotation);
        DisplayDimension swDisplayDimension = default(DisplayDimension);

        swPart = (ModelDoc2)swApp.ActiveDoc;
        swAnnotation = (Annotation)swPart.GetFirstAnnotation2();
        while (((swAnnotation != null)))
        {
            Debug.Print(" ");
            Debug.Print("Annotation name = " + swAnnotation.GetName());
            int AnnotationType = (int)swDimensionType_e.swDimensionTypeUnknown;
            AnnotationType = swAnnotation.GetType();
            if (AnnotationType == (int)swAnnotationType_e.swDisplayDimension)
            {
                Debug.Print(" Is a display dimension? True");
                swDisplayDimension = (DisplayDimension)swAnnotation.GetSpecificAnnotation();
                switch ((swDisplayDimension.Type2))
                {
                    case (int)swDimensionType_e.swOrdinateDimension:
                        Debug.Print(" Display dimension type = base ordinate and its subordinates");
                        break;
                    case (int)swDimensionType_e.swLinearDimension:
                        Debug.Print(" Display dimension type = linear");
                        break;
                    case (int)swDimensionType_e.swAngularDimension:
                        Debug.Print(" Display dimension type  = angular");
                        break;
                    case (int)swDimensionType_e.swArcLengthDimension:
                        Debug.Print(" Display dimension type = arc length");
                        break;
                    case (int)swDimensionType_e.swRadialDimension:
                        Debug.Print(" Display dimension type = radial");
                        break;
                    case (int)swDimensionType_e.swDiameterDimension:
                        Debug.Print(" Display dimension type = diameter");
                        break;
                    case (int)swDimensionType_e.swHorOrdinateDimension:
                        Debug.Print(" Display dimension type = horizontal ordinate");
                        break;
                    case (int)swDimensionType_e.swVertOrdinateDimension:
                        Debug.Print(" Display dimension type = vertical ordinate");
                        break;
                    case (int)swDimensionType_e.swZAxisDimension:
                        Debug.Print(" Display dimension type = z-axis");
                        break;
                    case (int)swDimensionType_e.swChamferDimension:
                        Debug.Print(" Display dimension type = chamfer dimension");
                        break;
                    case (int)swDimensionType_e.swHorLinearDimension:
                        Debug.Print(" Display dimension type = horizontal linear");
                        break;
                    case (int)swDimensionType_e.swVertLinearDimension:
                        Debug.Print(" Display dimension type = vertical linear");
                        break;
                    case (int)swDimensionType_e.swScalarDimension:
                        Debug.Print(" Display dimension type = scalar");
                        break;
                    default:
                        Debug.Print(" Display dimension type = unknown");
                        break;
                }
                Debug.Print(" Is a DimXpert display dimension? " + (swDisplayDimension.IsDimXpert() == false ? "False" : "True"));
                if (swAnnotation.IsDimXpert())
                {
                    DimXpertFeature DimXpertFeat = default(DimXpertFeature);
                    string FeatName = null;
                    DimXpertFeat = (DimXpertFeature)swAnnotation.GetDimXpertFeature();
                    if ((DimXpertFeat != null))
                    {
                        FeatName = DimXpertFeat.Name;
                        Debug.Print(" DimXpert feature name = " + FeatName);
                        switch ((DimXpertFeat.Type))
                        {
                            case swDimXpertFeatureType_e.swDimXpertFeature_Plane:
                                Debug.Print(" DimXpert feature type = plane");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_Cylinder:
                                Debug.Print(" DimXpert feature type = cylinder");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_Cone:
                                Debug.Print(" DimXpert feature type = cone");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_Extrude:
                                Debug.Print(" DimXpert feature type = extrude");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_Fillet:
                                Debug.Print(" DimXpert feature type = fillet");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_Chamfer:
                                Debug.Print(" DimXpert feature type = chamfer");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole:
                                Debug.Print(" DimXpert feature type = compound hole");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth:
                                Debug.Print(" DimXpert feature type = compound width");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch:
                                Debug.Print(" DimXpert feature type = compound notch");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D:
                                Debug.Print(" DimXpert feature type = compound closed-slot 3D");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint:
                                Debug.Print(" DimXpert feature type = intersect point");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine:
                                Debug.Print(" DimXpert feature type = intersect line");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle:
                                Debug.Print(" DimXpert feature type = intersect circle");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane:
                                Debug.Print(" DimXpert feature type = intersect plane");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_Pattern:
                                Debug.Print(" DimXpert feature type = pattern");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_Sphere:
                                Debug.Print(" DimXpert feature type = sphere");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane:
                                Debug.Print(" DimXpert feature type = best-fit plane");
                                break;
                            case swDimXpertFeatureType_e.swDimXpertFeature_Surface:
                                Debug.Print(" DimXpert feature type = surface");
                                break;
                            default:
                                Debug.Print(" DimXpert feature type = unknown");
                                break;
                        }
                    }
                }
            }
            else
            {
                Debug.Print(" Not a display dimension");
            }
            swAnnotation = (Annotation)swAnnotation.GetNext3();
        }
    }
    /// <summary>
    /// The SldWorks swApp variable is pre-assigned for you.
    /// </summary>
    public SldWorks swApp;
}
}
```
