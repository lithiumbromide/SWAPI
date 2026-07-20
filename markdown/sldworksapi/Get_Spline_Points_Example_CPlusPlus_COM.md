---
title: "Get Spline Points Example (C++)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Spline_Points_Example_CPlusPlus_COM.htm"
---

# Get Spline Points Example (C++)

This example shows how to get the points on a spline.

//------------------------------------------------------- // Preconditions: // 1. Start up SOLIDWORKS and open a new part
document. // 2. Sketch a
spline. // 3. Select the
Sketch1 feature of the spline in the FeatureManager design tree. // // NOTE: Do not select the spline in the graphics
area. This // causes an
assert, which results in you having to abort and // terminate the debug session. // // 4. Start Microsoft Visual Studio 2019 or later. // a. Click File > New >
Project > (C++ Windows) Console App . // b. Click Next . // c. Type the name of your project
in Project Name . // d. Click Create . // e. Right-click project, select Add , New Item , Select ATL > ATL Suppor t,
Click Add . // f. Click Project >
projectname Properties > Configuration Properties > // C/C++ and type the path to sldworks.tlb and swconst.tlb , // typically C:\Program
Files\SOLIDWORKS Corp\SOLIDWORK S, // in Additional
Include Directories. //
g. Click Apply or OK . // 5. Replace the code in the code window with This code. // 6. Click Debug > Start Debugging . // // Postconditions: // 1. Prints to the Output Window the number of spline
points followed by //
the x, y, z values of each point in the spline. // 2. Examine the Output Window. //------------------------------------------------------- // This code #include
"framework.h" #import "sldworks.tlb" raw_interfaces_only, raw_native_types,
no_namespace, named_guids // SOLIDWORKS type library #import "swconst.tlb"
raw_interfaces_only, raw_native_types, no_namespace, named_guids // SOLIDWORKS
constants type library #include <iostream> #include <sstream> int
_tmain(int argc, _TCHAR* argv[]) { // Initialize
COM // Do this before
using ATL smart pointers so that // COM is available ::CoInitialize(NULL); { //Use ATL smart pointers CComPtr<ISldWorks> pSwApp; if
(pSwApp.CoCreateInstance(L"Sldworks.Application", NULL, CLSCTX_LOCAL_SERVER) !=
S_OK) { return(0); } CComPtr<IModelDoc2> pSwModel; pSwApp->get_IActiveDoc2(&pSwModel); //Get the
selected sketch feature CComPtr<ISelectionMgr> pSwSelMgr; pSwModel->get_ISelectionManager(&pSwSelMgr); IDispatch* pDisp; pSwSelMgr->GetSelectedObject6(1, -1, &pDisp); CComPtr<IFeature> pSwFeat; if (S_OK == pDisp->QueryInterface(IID_IFeature, (void**)&pSwFeat)); pDisp =
NULL; //Get the sketch feature pSwFeat->GetSpecificFeature2(&pDisp); CComPtr<ISketch> pSwSketch; if (S_OK == pDisp->QueryInterface(IID_ISketch,
(void**)&pSwSketch)); pDisp = NULL; //Gets
the spline points by interpolation VARIANT vSplines; ::VariantInit(&vSplines); pSwSketch->GetSplinesInterpolate(&vSplines); CComPtr<IDispatch> pDispatchSafeArray = NULL; CComPtr<ISafeArrayUtility>
pSwSafeArray = NULL; HRESULT hres; hres =
pSwApp->GetSafeArrayUtility(&pDispatchSafeArray); hres =
pDispatchSafeArray.QueryInterface<ISafeArrayUtility>(&pSwSafeArray); //First value in vSplines array is the number of //sketch (or spline) points, followed by the x, y, z //coordinates of each point in the spline, so
calculate //the size of
the array long nbrSketchPoints; pSwSketch->GetSketchPointsCount2(&nbrSketchPoints); long splineArraySize = 1
+ (nbrSketchPoints * 3); //Print to the
Immediate Window the //number of spline points followed by the //x, y, z values of each of point in the spline for (int idx = 0; idx < splineArraySize; idx++) { double sketchPointValue; pSwSafeArray->GetDouble(vSplines, idx, &sketchPointValue); _bstr_t s; s =
(double)sketchPointValue; OutputDebugString(s + "\n"); } } //Uninitialize COM ::CoUninitialize(); return(0);}
