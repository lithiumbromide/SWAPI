---
title: "Get and Override Mass Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm"
---

# Get and Override Mass Properties Example (C#)

This example shows how to get and override some mass properties of a part.

```vb
 // -----------------------------------------------------------------------
 // Preconditions:
 // 1. Ensure the specified document exists.
 // 2. Open the Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
 // ----------------------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows;
 using System.Windows.Forms;

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;

 namespace MassProperty2_CSharp
 {

          partial  class  SolidWorksMacro
         {
              private  ModelDocExtension Extn;
              private  MassProperty2 MyMassProp;
               private   MassPropertyOverrideOptions OvProp;
              private  ModelDoc2 swModelDoc;
              private  double[] pmoi;
              private  double[] vValue;
              private  double[] value =  new  double[3];
              private  int errors;
              private  int warnings;
              private  double val;

              public  void Main()
             {
                 swModelDoc = swApp.OpenDoc6(@"C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\advdrawings\98food processor.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent,   "",  ref errors,  ref warnings);
                 Extn = swModelDoc.Extension;

                  // Create mass properties and override options
                 MyMassProp = (MassProperty2)Extn.CreateMassProperty2();
                 OvProp = (MassPropertyOverrideOptions)MyMassProp.GetOverrideOptions();
                 OvProp.OverrideMass =  true;
                 OvProp.SetOverrideMassValue(100);
                  double[] comArr =  new  double[9];
                 comArr[0] = 0.1677;
                 comArr[1] = 0;
                 comArr[2] = 0;
                 comArr[3] = 0;
                 comArr[4] = 0.21358;
                 comArr[5] = 0;
                 comArr[6] = 0;
                 comArr[7] = 0;
                 comArr[8] = 0.34772;
                 OvProp.OverrideMomentsOfInertia =  true;
                 OvProp.SetOverrideMomentsOfInertiaValue(0, comArr,  "");

                  // Use document property units (MKS)
                 MyMassProp.UseSystemUnits =  false;

                  Debug.Print("Mass properties before override");
                  Debug.Print("");

                 val = MyMassProp.Mass;
                  Debug.Print("Mass: " + val);
                 val = MyMassProp.Volume;
                  Debug.Print("Volume: " + val);
                 val = MyMassProp.Density;
                  Debug.Print("Density: " + val);
                 val = MyMassProp.SurfaceArea;
                  Debug.Print("Surface area: " + val);
                 pmoi = (double[])MyMassProp.PrincipalMomentsOfInertia;
                  Debug.Print("Principal moments of inertiae: Px: " + pmoi[0] +   ", Py: " + pmoi[1] +  ", and Pz: " + pmoi[2]);
                 vValue = (double[])MyMassProp.GetMomentOfInertia(0);
                  Debug.Print("Moments of inertia: Lxx: " + vValue[0] +   ", Lxy: " + vValue[1] +  ", Lxz: " + vValue[2] +  ", Lyx: " + vValue[3] +   ", Lyy: " + vValue[4] +  ", Lyz: " + vValue[5] +  ", Lzx: " + vValue[6] +   ", Lzy: " + vValue[7] +  ", Lzz: " + vValue[8]);

                 MyMassProp.SetOverrideOptions(OvProp, (int)swInConfigurationOpts_e.swThisConfiguration,  null);
                 MyMassProp.Recalculate();

                  Debug.Print("");
                  Debug.Print("Mass properties after override");
                  Debug.Print("");

                 val = MyMassProp.Mass;
                  Debug.Print("Mass: " + val);
                 val = MyMassProp.Volume;
                  Debug.Print("Volume: " + val);
                 val = MyMassProp.Density;
                  Debug.Print("Density: " + val);
                 val = MyMassProp.SurfaceArea;
                  Debug.Print("Surface area: " + val);
                 pmoi = (double[])MyMassProp.PrincipalMomentsOfInertia;
                  Debug.Print("Principal moments of inertia: Px: " + pmoi[0] +   ", Py: " + pmoi[1] +  ", and Pz: " + pmoi[2]);
                 vValue = (double[])MyMassProp.GetMomentOfInertia(0);
                  Debug.Print("Moments of inertia: Lxx: " + vValue[0] +   ", Lxy: " + vValue[1] +  ", Lxz: " + vValue[2] +  ", Lyx: " + vValue[3] +   ", Lyy: " + vValue[4] +  ", Lyz: " + vValue[5] +  ", Lzx: " + vValue[6] +   ", Lzy: " + vValue[7] +  ", Lzz: " + vValue[8]);
             }
              ///  <summary>
              ///     ''' The SldWorks swApp variable is pre-assigned for you.
              ///     '''   </summary>
              public  SldWorks swApp;
         }
```

}
