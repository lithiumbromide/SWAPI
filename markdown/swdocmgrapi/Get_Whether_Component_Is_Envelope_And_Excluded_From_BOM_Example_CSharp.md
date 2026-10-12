---
title: "Get Whether Component Is Envelope And Excluded From BOM (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_CSharp.htm"
---

# Get Whether Component Is Envelope And Excluded From BOM (C#)

This example shows how to find out if a component is an envelope and whether the component is included in the bill of materials (BOM).

```vb
 //---------------------------------------------------------------------------
// Preconditions:
// 1. Open SOLIDWORKS and copy the code below to a C# macro.
// 2. Ensure that the  specified file exists.
// 3. Specify your_license_key.
// 4. Open an Immediate window.
//
// Postconditions: Inspect the Immediate window.
//
// NOTE: ISwDMComponent5::ExcludeFromBom and ISwDMComponent5::IsEnvelope print
// to the Immediate Window for each component.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using SwDocumentMgr;
using System.Diagnostics;
namespace ExampleCS.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            SwDocumentMgr.SwDMClassFactory swClassFact;
            SwDocumentMgr.SwDMApplication swDocMgr;
            SwDocumentMgr.SwDMDocument7 swDoc;
            SwDocumentMgr.SwDMConfigurationMgr swCfgMgr;
            SwDMConfiguration7 swConfiguration7;

            string sDocFileName;
            SwDocumentMgr.SwDmDocumentType nDocType;
            SwDocumentMgr.SwDmDocumentOpenError nRetVal;
            string sLicenseKey;
            sLicenseKey = "your_license_key";
            sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\98food processor.sldasm";
            nDocType = SwDocumentMgr.SwDmDocumentType.swDmDocumentAssembly;
            swClassFact = new SwDMClassFactory();
            swDocMgr = swClassFact.GetApplication(sLicenseKey);
            swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, true, out nRetVal) as SwDMDocument7;
            swCfgMgr = swDoc.ConfigurationManager;
            string[] SWConfigNames;
            SWConfigNames = (string[])swCfgMgr.GetConfigurationNames();
            for (int j = 0; j < SWConfigNames.Length; j++)
            {
                swConfiguration7 = swCfgMgr.GetConfigurationByName(SWConfigNames[j]) as SwDMConfiguration7;
                object[] swComponents;
                swComponents = (object[])swConfiguration7.GetComponents();
                Debug.Print("Configuration Name = " + SWConfigNames[j]);
                for (int I = 0; I < swComponents.Length; I++)
                {
                    SwDMComponent5 comp;
                    comp = swComponents[I] as SwDMComponent5;
                    Debug.Print("Component Name = " + comp.Name);
                    Debug.Print("       IsEnvelope = " + comp.IsEnvelope().ToString());
                    Debug.Print("       ExcludeFromBOM = " + comp.ExcludeFromBOM.ToString());
                }
                Debug.Print("_______________________________________________________");
            }
            swDoc.CloseDoc();
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
