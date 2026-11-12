---
title: "ActiveDoc Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ActiveDoc"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html"
---

# ActiveDoc Property (ISldWorks)

Gets the currently active document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ActiveDoc As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Object

value = instance.ActiveDoc
```

### C#

```csharp
System.object ActiveDoc {get;}
```

### C++/CLI

```cpp
property System.Object^ ActiveDoc {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) or Nothing or null if the operation fails

## VBA Syntax

See [SldWorks::ActiveDoc](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ActiveDoc.html).

## Examples

[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)

## Remarks

If no document is active, then Nothing or null is returned. This is a read-only property.

The currently active document cannot be the document that is being edited by the end-user. For example, you can use in-context editing to modify an assembly component. The currently active document is the assembly, but the edit target is the assembly component. For assemblies, you can determine the edit target by using the [IAssemblyDoc::GetEditTarget](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetEditTarget.html) or [IAssemblyDoc::IGetEditTarget2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IGetEditTarget2.html) method.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.html)
[ISldWorks::ActivateDoc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc2.html)
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::GetOpenedFileInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenedFileInfo.html)
[ISldWorks::GetOpenFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName.html)
[ISldWorks::IActivateDoc3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActivateDoc3.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html)
[ISldWorks::OpenDoc6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html)
