---
title: "IActivateDoc3 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IActivateDoc3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActivateDoc3.html"
---

# IActivateDoc3 Method (ISldWorks)

Activates a document that has already been loaded. This file becomes the active document, and this method returns a pointer to that document object.

## Syntax

### Visual Basic (Declaration)

```vb
Function IActivateDoc3( _
   ByVal Name As System.String, _
   ByVal Silent As System.Boolean, _
   ByRef Errors As System.Integer _
) As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Name As System.String
Dim Silent As System.Boolean
Dim Errors As System.Integer
Dim value As ModelDoc2

value = instance.IActivateDoc3(Name, Silent, Errors)
```

### C#

```csharp
ModelDoc2 IActivateDoc3(
   System.string Name,
   System.bool Silent,
   out System.int Errors
)
```

### C++/CLI

```cpp
ModelDoc2^ IActivateDoc3(
   System.String^ Name,
   System.bool Silent,
   [Out] System.int Errors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of document to activate
- `Silent`: True if dialogs and warning messages should be avoided; false if dialogs and warning messages should be displayed to the end-user
- `Errors`: Status of the document activate operation as defined in [swActivateDocError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swActivateDocError_e.html); if no errors or warnings are encountered, this value is set to 0

### Return Value

[Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [SldWorks::IActivateDoc3](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IActivateDoc3.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)

## Remarks

This file becomes the active document, and this method returns a pointer to that document object.

If you do not specify a file extension in the name parameter, the document activated is based on its name and ignores the file extension. This can cause problems if you have two different document types with the same name loaded; for example, 12345.sldprt and 12345.sldasm.

If you do not specify the filename extension in your call to this method, then you cannot be sure which document is activated. To avoid this problem, you can specify the file name extension in the name parameter or you can check the document type after it is activated using [IModelDoc2::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetType.html).

In some instances, a document requires a rebuild when it is activated. If this is the case and you have passed True for the silent argument, then the activated document is not rebuilt and swDocNeedsRebuildWarning is returned in the errors argument. You can then programmatically rebuild the document using the [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) method.

If the document needs a rebuild upon activation and you have passed false for the Silent argument, then a dialog is displayed to the users asking them if they want to rebuild the document.

| If the user answers... | Then the activated document is... |
| --- | --- |
| No | Not rebuilt and swDocNeedsRebuildWarning is returned in the errors argument. |
| Yes | Rebuilt immediately and this warning is not returned. |

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::ActivateDoc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc2.html)
[ISldWorks::ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html)
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::GetOpenFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
