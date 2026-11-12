---
title: "Syntax Conventions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "apihelp/Syntax_Conventions.htm"
---

# Syntax Conventions

[See Also](sldworksAPIProgGuide.chm::/Overview/Unmanaged_CPP_and_CPP_CLI_Code_Differences.htm)

This topic explains the syntax conventions used with the API Help:

- [Notation](#Notation)
- [Methods and arguments](#Arguments)
- [Return values](#Return)
- [Interfaces](#Interfaces)
- [Properties](#Properties)
- [Availability links](#Availability)

#### Notation

All SOLIDWORKS and add-in API functions support the COM interface. If you are using COM, the SOLIDWORKS or add-in API function returns an [HRESULT, and any additional return values](sldworksAPIProgGuide.chm::/Overview/Return_Values.htm) are passed by reference as arguments.

#### Back to top

#### Methods and arguments

The following syntax uses the SOLIDWORKS method, [IModelDocExtension::SelectByID2](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html), which is a function that returns a BOOLEAN value. It passes nine arguments to the function.

| Visual Basic .NET | Dim boolstatus As Boolean = false boolstatus = swModelExtension.SelectByID2("Point1", "SKETCHPPOINT", .2, .3, 0, False, 0, Nothing, swSelectOptionDefault) |
| --- | --- |
| Visual Basic for Applications (VBA): | Dim Result as Boolean Result = swModelExtension.SelectByID2("Point1", "SKETCHPOINT", .2, .3, 0, False, 0, Nothing, swSelectOptionDefault) |
| C# | bool boolstatus = false; boolstatus = swModelExtension.SelectByID2("Point1", "SKETCHPOINT", .2, .3, 0, false, 0, null, swSelectOptionDefault); |
| Unmanaged C++ Dispatch: | BOOL Result = FALSE; Result = swModelExtension.SelectByID2(_T("Point1"),_T("SKETCHPOINT"), .2, .3, 0,0,0,0,swSelectOptionDefault); |
| Unmanaged C++ COM: | VARIANT_BOOL Result = FALSE; HRESULT hres = swModelExtension->SelectByID2(_T("Point1"),_T("SKETCHPOINT"),.2,.3, 0,0,0,0,swSelectOptionDefault,&result); |
| C++/CLI | bool bSelected = swModelExtension->SelectByID2(swBody->Name, "SOLIDBODY", 0.0, 0.0, 0.0, true, 0, nullptr, (int)swSelectOption_e::swSelectOptionDefault); |

NOTE: The return value in the Visual Basic (Usage) section in the Help is always shown as value. Because some methods and properties contain an argument named Value, SOLIDWORKS recommends that you rename the return value variable value to something meaningful to avoid an error in your code and for clarity.

The next example uses the SOLIDWORKS method, [IDrawingDoc::EditSheet](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.html), which is a subroutine which returns nothing (void). The method accepts no arguments.

| Visual Basic .NET | swDrawing.EditSheet() |
| --- | --- |
| Visual Basic for Applications (VBA): | swDrawing.EditSheet (see the Note below this table) |
| C# | swDrawing.EditSheet(); |
| Unmanaged C++ Dispatch: | swDrawing.EditSheet(); |
| Unmanaged C++ COM: | HRESULT hres = swDrawing->EditSheet(); |
| C++/CLI | swDrawing->EditSheet(); |

**NOTE:** Some methods are subroutines (that return nothing (**void**)) that also pass arguments. The VBA syntax for those methods is slightly different, despite what the Visual Basic for Applications (VBA) Syntax section of the help indicates. The help shows parentheses in the method signatures of all VBA methods. In practice, parentheses are not used in the VBA method signature of subroutines that return nothing. For example, IModelDoc2::SetUnits is a subroutine that returns nothing but passes arguments. The correct way to call IModelDoc2::SetUnits in VBA:

Part.SetUnits swINCHES, swFRACTION, 16, 0, False

#### Back to top

#### Return values

The following syntax uses the SOLIDWORKS method, [IModelDoc2::GetType](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetType.html), which is a subroutine that returns a long value. This function takes no arguments. Instead, it uses the current [IModelDoc2](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html) object and returns its type.

| Visual Basic .NET | int docType = 0; docType = swModel .GetType(); |
| --- | --- |
| Visual Basic for Applications (VBA): | Dim docType As Long docType = swModel.GetType |
| C# | int docType = 0; docType = swModel .GetType(); |
| Unmanaged C++ Dispatch: | long docType = 0; docType = swModel .GetType(); |
| Unmanaged C++ COM: | long docType = 0; HRESULT hres = swModel ->GetType( &docType ); |
| C++/CLI | swDocumentTypes_e nDocumentType; nDocumentType = (swDocumentTypes_e)swModel->GetType(); |

#### Back to top

#### Interfaces

Some functions have different versions of syntax. A function has multiple interfaces only when required. Always check the See Also link near the bottom of topic to see if a function has multiple interfaces (e.g., [IBody2::GetFirstFace](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.html) and [IBody2::IGetFirstFace](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.html)).

| Visual Basic .NET | Dim swFace as Face2 = Nothing swFace = swBody.GetFirstFace |
| --- | --- |
| Visual Basic for Applications (VBA): | Dim swFace As Object Set swFace = swBody.GetFirstFace |
| C# | Face2 swFace = null; swFace = (Face2) swBody.GetFirstFace(); |
| Unmanaged C++ Dispatch: | IDispatch* faceDisp = NULL; faceDisp = swBody.GetFirstFace(); IFace2 swFace(faceDisp); |
| Unmanaged C++ COM: | LPFACE2 swFace = NULL; HRESULT hres = swBody->IGetFirstFace( &swFace ); |
| C++/CLI | IFace2^ swFace = nullptr; swFace = (IFace2^)swBody->GetFirstFace(); - or - IFace2^ swFace = nullptr; swFace = swBody->IGetFirstFace(); |

The Dispatch interface returns a Dispatch pointer, while the COM interface returns an LPFACE2 pointer. The COM interface uses object pointers instead of Dispatch pointers and pointers instead of VARIANT SafeArrays. Because the argument types are different, any API function that handles objects or arrays has two distinct interfaces, one for COM and one for Dispatch.

#### Back to top

#### Properties

The following syntax uses the SOLIDWORKS property [IFeature::Name](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.html) to get and set the name of a feature.

| Visual Basic .NET | get: set: | featName = swFeat.Name swFeat.Name = featName |
| --- | --- | --- |
| Visual Basic for Applications (VBA): | get: set: | featName = swFeat.Name swFeat.Name = featName |
| C# | get: set: | featName = swFeat.Name; swFeat.Name = featName; |
| Unmanaged C++ Dispatch: | get: set: | featName = swFeat.GetName(); swFeat.SetName(featName); |
| Unmanaged C++ COM: | get: set: | hres = swFeat->get_Name(&featName); hres = swFeat->put_Name(featName); |
| C++/CLI | get: set: | featName = swFeat->Name; swFeat->Name = featName; |

[Back to top](#Top)

#### Availability links

The Availability links appearing at the bottom of a method, property, and delegate topic identifies the release in which the method, property, or delegate was introduced. Topics in the API Help lacking Availability links indicate that the method, property, or delegate was introduced prior to the SOLIDWORKS 98Plus release.

[Back to top](#Top)
