---
title: "CreatePropertyManagerPage Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "CreatePropertyManagerPage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreatePropertyManagerPage.html"
---

# CreatePropertyManagerPage Method (ISldWorks)

Creates a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePropertyManagerPage( _
   ByVal Title As System.String, _
   ByVal Options As System.Integer, _
   ByVal Handler As System.Object, _
   ByRef Errors As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Title As System.String
Dim Options As System.Integer
Dim Handler As System.Object
Dim Errors As System.Integer
Dim value As System.Object

value = instance.CreatePropertyManagerPage(Title, Options, Handler, Errors)
```

### C#

```csharp
System.object CreatePropertyManagerPage(
   System.string Title,
   System.int Options,
   System.object Handler,
   out System.int Errors
)
```

### C++/CLI

```cpp
System.Object^ CreatePropertyManagerPage(
   System.String^ Title,
   System.int Options,
   System.Object^ Handler,
   [Out] System.int Errors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Title`: Title of the page
- `Options`: Options as defined in [swPropertyManagerPageOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageOptions_e.html)
- `Handler`: Pointer to the event handler for this page ([IPropertyManagerPage2Handler5](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5.html))
- `Errors`: Status of the creation as defined in [swPropertyManagerPageStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageStatus_e.html)

### Return Value

[PropertyManager page](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2.html)

## VBA Syntax

See [SldWorks::CreatePropertyManagerPage](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~CreatePropertyManagerPage.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Examples

[Cut Body In Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)
[Create PropertyManager Page (VBA)](Create_PropertyManager_Page_Example_VB.htm)

## Remarks

Specify swPropertyManagerPageOptions_e.swPropertyManagerOptions_LockedPage in the Options parameter when you create your PropertyManager page. It is important that when a handler (such as [IPropertyManagerPage2Handler5::OnButtonPress](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnButtonPress.html) or [IPropertyManagerPage2Handler5::OnClose](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnClose.html)) is finished and control returns to SOLIDWORKS that the PropertyManager page is still there. If the PropertyManager page is not there, SOLIDWORKS might crash. Some methods try to close the PropertyManager page, but you can avoid this scenario by creating the PropertyManager page as Locked.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::ICreatePropertyManagerPage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICreatePropertyManagerPage.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
