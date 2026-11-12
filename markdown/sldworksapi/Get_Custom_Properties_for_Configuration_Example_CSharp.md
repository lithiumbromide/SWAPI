---
title: "Get Custom Properties for Configuration Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Custom_Properties_for_Configuration_Example_CSharp.htm"
---

# Get Custom Properties for Configuration Example (C#)

This example shows how to get the names, types, values, and evaluated values of the active configuration's custom properties. It also shows how to add a custom property to the configuration.

```vb
//---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Adds a date custom property to the part's configuration.
 // 2. Tests whether the custom property is editable, and if so,
 //    edits it.
 // 3. Gets all custom properties in the configuration.
 // 4. Deletes a custom property.
 // 5. Examine the Immediate window.
 //---------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;

 namespace IsCustomPropEditable_CSharp
 {
     public partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel;
             Configuration config;
             CustomPropertyManager cusPropMgr;
             int lRetVal;
             object vPropNames = null;
             string[] propNames;
             object vPropTypes = null;
             object vPropValues = null;
             object[] propValues;
             string ValOut;
             string ResolvedValOut;
             bool wasResolved;
             bool linkToProp;
             object resolved = null;
             object linkProp = null;
             int nNbrProps;
             int j;
             int custPropType;

             bool bRet;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             config = (Configuration)swModel.GetActiveConfiguration();

             cusPropMgr = config.CustomPropertyManager;

             lRetVal = cusPropMgr.Add3("ADATE", (int)swCustomInfoType_e.swCustomInfoDate, "4-13-59", (int)swCustomPropertyAddOption_e.swCustomPropertyDeleteAndAdd);
             lRetVal = cusPropMgr.Get6("ADATE", false, out ValOut, out ResolvedValOut, out wasResolved, out linkToProp);
             bRet = cusPropMgr.IsCustomPropertyEditable("ADATE", config.Name);
             if (bRet == true)
             {
                 Debug.Print("ADATE is editable. Change the date.");
                 lRetVal = cusPropMgr.Set2("ADATE", "4-13-89");
             }
             else
             {
                 Debug.Print("ADATE is not editable.");
             }

             lRetVal = cusPropMgr.Get6("ADATE", false, out ValOut, out ResolvedValOut, out wasResolved, out linkToProp);

             // Get the number of custom properties for this configuration
             nNbrProps = cusPropMgr.Count;
             Debug.Print("Number of custom properties for this configuration:            " + nNbrProps);

             // Get the custom properties
             lRetVal = cusPropMgr.GetAll3(ref vPropNames, ref vPropTypes, ref vPropValues, ref resolved, ref linkProp);
             propValues = (object[])vPropValues;
             propNames = (string[])vPropNames;
             // For each custom property, print its name, type, and evaluated value
             for (j = 0; j <= nNbrProps - 1; j++)
             {
                 custPropType = cusPropMgr.GetType2(propNames[j]);
                 Debug.Print("Name, swCustomInfoType_e value, and resolved value:  " + propNames[j] + ", " + custPropType + ", " + propValues[j]);
             }

             lRetVal = cusPropMgr.Delete2("ADATE");

             // Get the number of custom properties for this configuration
             nNbrProps = cusPropMgr.Count;
             Debug.Print("Number of custom properties for this configuration:            " + nNbrProps);
         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```
