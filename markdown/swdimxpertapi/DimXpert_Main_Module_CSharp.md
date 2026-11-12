---
title: "DimXpert Main Module Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/DimXpert_Main_Module_CSharp.htm"
---

# DimXpert Main Module Example (C#)

```vb
// This module is a component of
// Get DimXpert Features and Annotations in a Model Example (C#).

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdimxpert;
using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Collections.ObjectModel;
namespace DimXpert_text_v2_cs.csproj
{
    partial class SolidWorksMacro
    {
        //This application allows the user to view all of the DimXpert feature and annotation objects in a model.
        public void Main()
        {
            ModelDoc2 swModelDoc = default(ModelDoc2);
            swModelDoc = (ModelDoc2)swApp.ActiveDoc;
            if (swModelDoc == null)
            {
                return;
            }
            Scripting.FileSystemObject f = new Scripting.FileSystemObject();
            Scripting.TextStream textStr = default(Scripting.TextStream);
            textStr = f.CreateTextFile("C:\\temp\\dimXpertInfo.txt", true, false);
            if (textStr == null)
            {
                Debug.Print("Error creating temp file.");
                return;
            }
            log("Starting DimXpert log...", textStr);
            retrieve_info_text(swApp, textStr);
            textStr.Close();
        }
        private void log(string text, Scripting.TextStream textStr)
        {
            Debug.Print(text);
            textStr.WriteLine(text);
        }
        private void retrieve_info_text(SldWorks swapp, Scripting.TextStream textStr)
        {
            DimXpertManager dimXpertMgr = default(DimXpertManager);
            ModelDocExtension modelDocExtension = default(ModelDocExtension);
            modelDocExtension = swapp.IActiveDoc2.Extension;
            dimXpertMgr = modelDocExtension.get_DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name,
     true);
            log("Model: " + swapp.IActiveDoc2.GetPathName(), textStr);
            DimXpertPart dimXpertPartObj = default(DimXpertPart);
            dimXpertPartObj = (DimXpertPart)dimXpertMgr.DimXpertPart;
            SolidWorks.Interop.swdimxpert.DimXpertPart dimXpertPart = default(SolidWorks.Interop.swdimxpert.DimXpertPart);
            dimXpertPart = dimXpertPartObj;
            object[] vFeatures = null;
            object[] vAnnotations = null;
            vFeatures = (object[])dimXpertPart.GetFeatures();
            vAnnotations = (object[])dimXpertPart.GetAnnotations();
            log("------------------------", textStr);
            log("Features...", textStr);
            log("------------------------", textStr);
            DimXpertFeature featTemp = default(DimXpertFeature);
            long featureIndex = 0;
            for (featureIndex = 0; featureIndex <= vFeatures.GetUpperBound(0); featureIndex++)
            {
                featTemp = (DimXpertFeature)vFeatures[featureIndex];
                DimXpertFeatureData FeatureData = new DimXpertFeatureData();
                Collection<string> featureDataText = default(Collection<string>);
                featureDataText = FeatureData.FeatureData(featTemp);
                int featureTextIndex = 0;
                log("DimXpertFeature...", textStr);
                for (featureTextIndex = 0; featureTextIndex <= featureDataText.Count - 1; featureTextIndex++)
                {
                    log(featureDataText[featureTextIndex], textStr);
                }
                log(" ", textStr);
                log(" ", textStr);
            }
            log("------------------------", textStr);
            log("Annotations...", textStr);
            log("------------------------", textStr);
            DimXpertAnnotation annotationTemp = default(DimXpertAnnotation);
            long annotationIndex = 0;
            for (annotationIndex = 0; annotationIndex <= vAnnotations.GetUpperBound(0); annotationIndex++)
            {
                annotationTemp = (DimXpertAnnotation)vAnnotations[annotationIndex];
                Debug.Print(annotationTemp.Name);
                DimXpertAnnotationData AnnotationData = new DimXpertAnnotationData();
                Collection<string> AnnotationDataText = default(Collection<string>);
                AnnotationDataText = AnnotationData.AnnotationData(annotationTemp, dimXpertPart);
                int annotationTextIndex = 0;
                log("DimXpertAnnotation...", textStr);
                for (annotationTextIndex = 0; annotationTextIndex <= AnnotationDataText.Count - 1; annotationTextIndex++)
                {
                    log(AnnotationDataText[annotationTextIndex], textStr);
                }
                log(" ", textStr);
                log(" ", textStr);
            }
            log("------------------------", textStr);
            log("Block Tolerances...", textStr);
            log("------------------------", textStr);
            listBlockTolerances_text(dimXpertPart, textStr);
        }
        private void listBlockTolerances_text(SolidWorks.Interop.swdimxpert.DimXpertPart dimXpertPart, Scripting.TextStream textStr)
        {
            SolidWorks.Interop.swdimxpert.DimXpertBlockTolerances blockTols = default(SolidWorks.Interop.swdimxpert.DimXpertBlockTolerances);
            bool boolstatus = false;
            double lin1 = 0;
            int lin1prec = 0;
            double lin2 = 0;
            int lin2prec = 0;
            double lin3 = 0;
            int lin3prec = 0;
            double ang = 0;
            SolidWorks.Interop.swdimxpert.swDimXpertISO2768PartType_e isoCode = default(SolidWorks.Interop.swdimxpert.swDimXpertISO2768PartType_e);
            blockTols = dimXpertPart.GetBlockTolerances();
            if ((blockTols != null))
            {
                switch (blockTols.Type)
                {
                    case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch:
                        boolstatus = blockTols.GetToleranceValues(ref lin1, ref lin1prec, ref lin2, ref lin2prec, ref lin3, ref lin3prec, ref ang);
                        log("swDimXpertBlockToleranceType_ASMEInch", textStr);
                        log("Linear1: " + System.String.Format("{0:D}", lin1prec.ToString()) +
                            " Places = " + System.String.Format("{0:D}", lin1.ToString()) + " " +
                            "Linear2: " + System.String.Format("{0:D}", lin2prec.ToString()) +
                            " Places = " + System.String.Format("{0:D}", lin2.ToString()) + " " +
                            "Linear3: " + System.String.Format("{0:D}", lin3prec.ToString()) +
                            " Places = " + System.String.Format("{0:D}", lin3.ToString()) + " " +
                            "Angular = " + System.String.Format("{0:D}", (ang * 57.2957795130823).ToString()), textStr);
                        break;
                    case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768:
                        log("swDimXpertBlockToleranceType_ISO2768", textStr);
                        boolstatus = blockTols.GetISO2768PartType(ref isoCode);
                        switch (isoCode)
                        {
                            case swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_Fine:
                                log("General Tolerance: Fine", textStr);
                                break;
                            case swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_Medium:
                                log("General Tolerance: Medium", textStr);
                                break;
                            case swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_Coarse:
                                log("General Tolerance: Coarse", textStr);
                                break;
                            case swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_VeryCoarse:
                                log("General Tolerance: Very Coarse", textStr);
                                break;
                        }
                        break;
                }
            }
        }

        public SldWorks swApp;
    }
}
```
