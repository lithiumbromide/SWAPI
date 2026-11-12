---
title: "Get Components in Drawing View (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Components_in_Drawing_View_Example_CSharp.htm"
---

# Get Components in Drawing View (C#)

This example shows how to get the components in a drawing view and how to change their line font styles.

```vb
 //------------------------------------------------------------------
 // Preconditions:
 // 1. Drawing document opened by the macro exists.
 // 2. Drawing view is selected.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Specified drawing document is opened.
 // 2. Drawing View1 is selected.
 // 3. Gets the root and children components for Drawing
 //    View1.
 // 4. For each component:
 //    a. Prints whether a drawing component is selected,
 //       the name of the component, and the name of the
 //       configuration to the Immediate window.
 //    b. Disables the use of the document defaults for the
 //       the component's line font style.
 //    c. Sets new line style and line thickness for the component's
 //       visible edges and prints the new settings and values to
 //       the Immediate window.
 //    d. Prints the file name of the component to the Immediate window.
 //------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;

 namespace LineFontsDrawingComponentCSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             DrawingDoc swDraw = default(DrawingDoc);
             SelectionMgr swSelMgr = default(SelectionMgr);
              SelectData swSelData =  default(SelectData);
             ModelDocExtension swModelDocExt =  default(ModelDocExtension);
             View swView = default(View);
             DrawingComponent swRootDrawComp =  default(DrawingComponent);
             object[] vDrawChildCompArr = null;
             DrawingComponent swDrawComp = default(DrawingComponent);
             Component2 swComp = default(Component2);
             ModelDoc2 swCompModel = default(ModelDoc2);
             string assemblyDrawing = null;
             bool status = false;
             int errors = 0;
             int warnings = 0;
             int lineWeight = 0;
             double lineThickness = 0;

             assemblyDrawing =  "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\driveworksxpress\\mobile gantry.slddrw";
             swModel = (ModelDoc2)swApp.OpenDoc6(assemblyDrawing, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

             swDraw = (DrawingDoc)swModel;
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swSelData = (SelectData)swSelMgr.CreateSelectData();

             status = swDraw.ActivateView("Drawing View4");
             status = swModelDocExt.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0.104008832128, 0.1163870710783, 0, false, 0, null, 0);
             swView = (View)swSelMgr.GetSelectedObject6(1, -1);
             swModel.ViewZoomtofit2();
             swRootDrawComp = (DrawingComponent)swView.RootDrawingComponent;

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  View = " + swView.Name);

             vDrawChildCompArr = (object[])swRootDrawComp.GetChildren();
             foreach (object vDrawChildComp in vDrawChildCompArr)
             {
                 swDrawComp = (DrawingComponent)vDrawChildComp;

                  // Drawing component selected?
                 Debug.Print(" Drawing component selected = " + swDrawComp.Select(true, null));

                 // Returns NULL if underlying model is open in a different configuration
                 swComp = (Component2)swDrawComp.Component;

                 if ((null != swComp))
                 {
                     // Returns NULL if drawing is lightweight
                     swCompModel = (ModelDoc2)swComp.GetModelDoc2();

                     Debug.Print("      Component                            = " + swComp.Name2);
                     Debug.Print("      Configuration                        = " + swComp.ReferencedConfiguration);

                     // Turn off using document default settings for component's line font style
                     swDrawComp.UseDocumentDefaults = false;
                     Debug.Print("      Default component line font in use   = " + swDrawComp.UseDocumentDefaults);
                     // Set new line style for visible edges
                     swDrawComp.SetLineStyle((int)swDrawingComponentLineFontOption_e.swDrawingComponentLineFontVisible, (int)swLineStyles_e.swLineCHAIN);
                     Debug.Print("        Line style for visible edges                      = " + swDrawComp.GetLineStyle((int)swDrawingComponentLineFontOption_e.swDrawingComponentLineFontVisible));
                     // Set new line thickness for visible edges
                     swDrawComp.SetLineThickness((int)swDrawingComponentLineFontOption_e.swDrawingComponentLineFontVisible, (int)swLineWeights_e.swLW_CUSTOM, 0.0003);
                     lineWeight = swDrawComp.GetLineThickness((int)swDrawingComponentLineFontOption_e.swDrawingComponentLineFontVisible, out lineThickness);
                     Debug.Print("        Line weight style and thickness for visible edges = " + lineWeight + ", " + lineThickness * 1000 + " mm");

                     if ((null != swCompModel))
                     {
                         Debug.Print("      File                                 = " + swCompModel.GetPathName());
                         Debug.Print(" ");
                     }

                 }

             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
