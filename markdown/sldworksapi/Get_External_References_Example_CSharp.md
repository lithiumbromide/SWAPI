---
title: "Get External References (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_External_References_Example_CSharp.htm"
---

# Get External References (C#)

This example shows how to get a list of the external references for a selected component, selected feature, or document.

```vb
 //----------------------------------------------------------
 //  Preconditions:
 //  1. Open an assembly or part document.
 //  2. Select:
 //     * a component in an assembly document.
 //       - or -
 //     * a feature in an assembly or part document.
 //       - or -
 //     * Nothing in either type of document.
//  3. Modify namespace as necessary.
 //
 // Postconditions: Examine the Immediate window
 // to see the name of the part or assembly document
 // and the external references for the selected
 // component, feature, or document.
 //----------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;

 namespace ListExternalFileReferencesCSharp.csproj
 {

     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModDocExt =  default(ModelDocExtension);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             Component2 swComp = default(Component2);
             object vModelPathName = null;
             object vComponentPathName = null;
             object vFeature = null;
             object vDataType = null;
             object vStatus = null;
             object vRefEntity = null;
             object vFeatComp = null;
            object vConfigOpt = null;
             object vConfigName = null;
             int nConfigOpt = 0;
             string sConfigName = null;
             int nRefCount = 0;
             int nSelType = 0;
             int i = 0;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             swModDocExt = (ModelDocExtension)swModel.Extension;
             nSelType = swSelMgr.GetSelectedObjectType3(1, -1);

             switch (nSelType)
             {

                 // Selected component in an assembly document
                 case (int)swSelectType_e.swSelCOMPONENTS:
                     swComp = (Component2)swSelMgr.GetSelectedObjectsComponent3(1, -1);
                     nRefCount = swComp.ListExternalFileReferencesCount();
                     swComp.ListExternalFileReferences2(out vModelPathName, out vComponentPathName, out vFeature, out vDataType, out vStatus, out vRefEntity, out vFeatComp, out nConfigOpt, out sConfigName);

                     swModel = (ModelDoc2)swComp.GetModelDoc2();
              Debug.Print("Model name = " + swModel.GetPathName());
             Debug.Print("    Reference count        = " + System.Convert.ToString(nRefCount));

             if (nRefCount >= 1)
             {
                 object[] ModelPathName = new object[nRefCount - 1];
                 object[] ComponentPathName = new object[nRefCount - 1];
                 object[] Feature = new object[nRefCount - 1];
                 object[] DataType = new object[nRefCount - 1];
                 int[] Status = new int[nRefCount - 1];
                 object[] RefEntity = new object[nRefCount - 1];
                 object[] FeatComp = new object[nRefCount - 1];

                 ModelPathName = (object[])vModelPathName;
                 ComponentPathName = (object[])vComponentPathName;
                 Feature = (object[])vFeature;
                 DataType = (object[])vDataType;
                 Status = (int[])vStatus;
                 RefEntity = (object[])vRefEntity;
                 FeatComp = (object[])vFeatComp;

                 Debug.Print("");
                 for (i = 0; i <= nRefCount - 1; i++)
                 {
                     Debug.Print("    Model path + name      = " + ModelPathName[i]);
                     Debug.Print("    Component path + name  = " + ComponentPathName[i]);
                     Debug.Print("    Feature                = " + Feature[i]);
                     Debug.Print("    Data type              = " + DataType[i]);
                     Debug.Print("    Status                 = " + System.Convert.ToString(Status[i]));
                     Debug.Print("    Reference entity       = " + RefEntity[i]);
                     Debug.Print("    Feature component      = " + FeatComp[i]);

                     Debug.Print(" ");
                 }
                Debug.Print("    Config option          = " + nConfigOpt);
                 Debug.Print("    Config name            = " + sConfigName);
             }

                     break;
                 // Selected feature in a part or assembly document
                 case (int)swSelectType_e.swSelBODYFEATURES:
                 case (int)swSelectType_e.swSelSKETCHES:
                     swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                     nRefCount = swFeat.ListExternalFileReferencesCount();
                     swFeat.ListExternalFileReferences2(out vModelPathName, out vComponentPathName, out vFeature, out vDataType, out vStatus, out vRefEntity, out vFeatComp, out nConfigOpt, out sConfigName);
             Debug.Print("Model name = " + swModel.GetPathName());
             Debug.Print("    Reference count        = " + System.Convert.ToString(nRefCount));

             if (nRefCount >= 1)
             {
                 object[] ModelPathName = new object[nRefCount - 1];
                 object[] ComponentPathName = new object[nRefCount - 1];
                 object[] Feature = new object[nRefCount - 1];
                 object[] DataType = new object[nRefCount - 1];
                 int[] Status = new int[nRefCount - 1];
                 object[] RefEntity = new object[nRefCount - 1];
                 object[] FeatComp = new object[nRefCount - 1];

                 ModelPathName = (object[])vModelPathName;
                 ComponentPathName = (object[])vComponentPathName;
                 Feature = (object[])vFeature;
                 DataType = (object[])vDataType;
                 Status = (int[])vStatus;
                 RefEntity = (object[])vRefEntity;
                 FeatComp = (object[])vFeatComp;

                 Debug.Print("");
                 for (i = 0; i <= nRefCount - 1; i++)
                 {
                     Debug.Print("    Model path + name      = " + ModelPathName[i]);
                     Debug.Print("    Component path + name  = " + ComponentPathName[i]);
                     Debug.Print("    Feature                = " + Feature[i]);
                     Debug.Print("    Data type              = " + DataType[i]);
                     Debug.Print("    Status                 = " + System.Convert.ToString(Status[i]));
                     Debug.Print("    Reference entity       = " + RefEntity[i]);
                     Debug.Print("    Feature component      = " + FeatComp[i]);

                     Debug.Print(" ");
                 }
                Debug.Print("    Config option          = " + nConfigOpt);
                 Debug.Print("    Config name            = " + sConfigName);
             }

                     break;

                 // Part or assembly
                 default:
                     nRefCount = swModDocExt.ListExternalFileReferencesCount();
                     swModDocExt.ListExternalFileReferences2(out vModelPathName, out vComponentPathName, out vFeature, out vDataType, out vStatus, out vRefEntity, out vFeatComp, out vConfigOpt, out vConfigName);
             Debug.Print("Model name = " + swModel.GetPathName());
             Debug.Print("    Reference count        = " + System.Convert.ToString(nRefCount));

             if (nRefCount >= 1)
             {
                 object[] ModelPathName = new object[nRefCount - 1];
                 object[] ComponentPathName = new object[nRefCount - 1];
                 object[] Feature = new object[nRefCount - 1];
                 object[] DataType = new object[nRefCount - 1];
                 int[] Status = new int[nRefCount - 1];
                 object[] RefEntity = new object[nRefCount - 1];
                 object[] FeatComp = new object[nRefCount - 1];
                int[] ConfigOpt = new int[nRefCount - 1];
                object[] ConfigName = new object[nRefCount - 1];

                 ModelPathName = (object[])vModelPathName;
                 ComponentPathName = (object[])vComponentPathName;
                 Feature = (object[])vFeature;
                 DataType = (object[])vDataType;
                 Status = (int[])vStatus;
                 RefEntity = (object[])vRefEntity;
                 FeatComp = (object[])vFeatComp;
                ConfigOpt = (int[])vConfigOpt;
                ConfigName = (object[])vConfigName;

                 Debug.Print("");
                 for (i = 0; i <= nRefCount - 1; i++)
                 {
                     Debug.Print("    Model path + name      = " + ModelPathName[i]);
                     Debug.Print("    Component path + name  = " + ComponentPathName[i]);
                     Debug.Print("    Feature                = " + Feature[i]);
                     Debug.Print("    Data type              = " + DataType[i]);
                     Debug.Print("    Status                 = " + System.Convert.ToString(Status[i]));
                     Debug.Print("    Reference entity       = " + RefEntity[i]);
                     Debug.Print("    Feature component      = " + FeatComp[i]);
                     Debug.Print("    Config option          = " + ConfigOpt[i]);
                     Debug.Print("    Config name            = " + ConfigName[i]);
                     Debug.Print(" ");
                 }
             }

                     break;
             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
