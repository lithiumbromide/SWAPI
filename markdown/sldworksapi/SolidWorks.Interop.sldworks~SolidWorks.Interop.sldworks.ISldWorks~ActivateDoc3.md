---
title: "ActivateDoc3 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ActivateDoc3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc3.html"
---

# ActivateDoc3 Method (ISldWorks)

Activates a loaded document and rebuilds it as specified.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateDoc3( _
   ByVal Name As System.String, _
   ByVal UseUserPreferences As System.Boolean, _
   ByVal Option As System.Integer, _
   ByRef Errors As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Name As System.String
Dim UseUserPreferences As System.Boolean
Dim Option As System.Integer
Dim Errors As System.Integer
Dim value As System.Object

value = instance.ActivateDoc3(Name, UseUserPreferences, Option, Errors)
```

### C#

```csharp
System.object ActivateDoc3(
   System.string Name,
   System.bool UseUserPreferences,
   System.int Option,
   out System.int Errors
)
```

### C++/CLI

```cpp
System.Object^ ActivateDoc3(
   System.String^ Name,
   System.bool UseUserPreferences,
   System.int Option,
   [Out] System.int Errors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the loaded document to activate (see **Remarks**)
- `UseUserPreferences`: True to rebuild as per the [swRebuildOnActivation](ms-its:swconst.chm::/SO_Miscellaneous.htm#rebuild) system option; false to rebuild as per Option
- `Option`: Rebuild option as defined in [swRebuildOnActivation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRebuildOnActivation_e.html) (see **Remarks**)
- `Errors`: Status of the activate operation as defined in [swActivateDocError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swActivateDocError_e.html); if
  no errors or warnings are encountered, then this value is 0 (see **Remarks**)

### Return Value

[Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [SldWorks::ActivateDoc3](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ActivateDoc3.html).

## Examples

[Rebuild Document on Activation (VBA)](Rebuild_Document_on_Activation_Example_VB.htm)
[Rebuild Document on Activation (VB.NET)](Rebuild_Document_on_Activation_Example_VBNET.htm)
[Rebuild Document on Activation (C#)](Rebuild_Document_on_Activation_Example_CSharp.htm)

## Remarks

This method brings the document specified in Name to the foreground of SOLIDWORKS and returns a pointer to the document.

If you do not specify a file extension in Name, the document activated is based on its filename without the file extension. This can cause problems if you have loaded two different document types with the same name (e.g., **12345.sldprt** and **12345.sldasm)**. To avoid this problem, specify the file extension in Name or check the document type after it is activated using [IModelDoc2::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetType.html).

If the document needs a rebuild upon activation, and you have specified Option with [swRebuildOnActivation_e.swDontRebuildActiveDoc](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRebuildOnActivation_e.html), then the activated document is not rebuilt, and Errors contains [swActivateDocError_e.swDocNeedsRebuildWarning](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swActivateDocError_e.html). You can then rebuild the document using [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html).

If the document needs a rebuild upon activation, and you have specified Option with [swRebuildOnActivation_e.swUserDecision](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRebuildOnActivation_e.html), then a dialog displays asking whether to rebuild the document.

| If the user answers... | Then the activated document is... |
| --- | --- |
| No | Not rebuilt, and Errors contains swActivateDocError_e.swDocNeedsRebuildWarning |
| Yes | Rebuilt immediately |

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IActivateDoc3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActivateDoc3.html)
[ISldWorks::ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html)
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::CloseAndReopen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::GetOpenFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html)
[ISldWorks::LoadFile4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.html)
[ISldWorks::OpenDoc7 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
