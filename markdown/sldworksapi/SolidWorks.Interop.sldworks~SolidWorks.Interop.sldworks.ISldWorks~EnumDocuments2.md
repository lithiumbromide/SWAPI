---
title: "EnumDocuments2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "EnumDocuments2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.html"
---

# EnumDocuments2 Method (ISldWorks)

Gets a list of documents currently open in the application.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumDocuments2() As EnumDocuments2
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As EnumDocuments2

value = instance.EnumDocuments2()
```

### C#

```csharp
EnumDocuments2 EnumDocuments2()
```

### C++/CLI

```cpp
EnumDocuments2^ EnumDocuments2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Documents enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDocuments2.html)

## VBA Syntax

See [SldWorks::EnumDocuments2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~EnumDocuments2.html).

## Examples

[Get List of Open Documents (C++)](Get_List_of_Open_Documents_Example_CPlusPlus_COM.htm)

## Remarks

The list of [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) objects contained in the [IEnumDocuments2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDocuments2.html) object contain any open IModelDoc2 pointer. This includes IModelDoc2 objects that may have been opened as file references, for example, from an assembly or drawing.

You might want to use the [IModelDoc::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~Visible.html) property to determine if a particular document has its own window and is visible to the user.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks:GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks:GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks:CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html)
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
