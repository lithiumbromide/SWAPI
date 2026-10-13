---
title: "CloseDoc Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "CloseDoc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html"
---

# CloseDoc Method (ISldWorks)

Closes the specified document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CloseDoc( _
   ByVal Name As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Name As System.String

instance.CloseDoc(Name)
```

### C#

```csharp
void CloseDoc(
   System.string Name
)
```

### C++/CLI

```cpp
void CloseDoc(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of document (see **Remarks**)

## VBA Syntax

See [SldWorks::CloseDoc](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~CloseDoc.html).

## Examples

[Close Document (VBA)](Close_Document_Example_VB.htm)
[Get Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)
[Run or Attach to a SOLIDWORKS Session (VBA)](SOLIDWORKS_Visible_or_BackGround_Example_VB.htm)
[Get Names of Creators of Features (C++)](Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm)
[Get Names of Creators of Features (VBA)](Get_Names_of_Creators_of_Features_Example_VB.htm)
[Get Names of Creators of Features (VB.NET)](Get_Names_of_Creators_of_Features_Example_VBNET.htm)
[Get Names of Creators of Features (C#)](Get_Names_of_Creators_of_Features_Example_CSharp.htm)

## Remarks

If Name is specified with:

- the name of a document that is not open, then this method does nothing.
- an empty string (""), then the active document is closed without saving.
- the name of a document in the dirty state (modified, but not saved), then this method closes the document without saving it.

This method also closes any non-active hidden documents.

For documents referenced by other documents loaded in memory, call this method to release user-interface resources while keeping the model data loaded.

If you are closing the only document open in the SOLIDWORKS Design session and this SOLIDWORKS Design session is a background session, then calling this method, or calling [ISldWorks::QuitDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~QuitDoc.html), results in the SOLIDWORKS Design session being closed.

A background SOLIDWORKS Design session can be created when the SOLIDWORKS Design session is started by your application and the session is not controlled by the user; i.e., [ISldWorks::UserControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~UserControl.html) set to false.

To keep the SOLIDWORKS Design session open, set ISldWorks::UserControl to True, which makes the session visible, or you can close your documents at the end of your program execution.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::OpenDoc6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html)
[ISldWorks::ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html)
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::GetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocuments.html)
[ISldWorks::GetDocumentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentCount.html)
[ISldWorks::IGetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocuments.html)
[ISldWorks::CloseAndReopen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen.html)
