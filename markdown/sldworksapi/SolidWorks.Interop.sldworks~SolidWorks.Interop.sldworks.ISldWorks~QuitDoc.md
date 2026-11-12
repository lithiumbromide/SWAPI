---
title: "QuitDoc Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "QuitDoc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.html"
---

# QuitDoc Method (ISldWorks)

Closes the specified document without saving changes.

## Syntax

### Visual Basic (Declaration)

```vb
Sub QuitDoc( _
   ByVal Name As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Name As System.String

instance.QuitDoc(Name)
```

### C#

```csharp
void QuitDoc(
   System.string Name
)
```

### C++/CLI

```cpp
void QuitDoc(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of document to close

## VBA Syntax

See [SldWorks::QuitDoc](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~QuitDoc.html).

## Examples

[Save Rolledbacked Part as Parasolid File (VBA)](Save_Roll_Backed_Part_as_Parasolid_File_Example_VB.htm)
[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)
[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)

## Remarks

If you are closing the only document in the SOLIDWORKS Design session and the SOLIDWORKS Design session is a background session, then calling [ISldWorks::CloseDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CloseDoc.html) or this method results in the SOLIDWORKS Design session closing.

You can create a background SOLIDWORKS Design session when the starting a SOLIDWORKS Design session in your application and the session is controlled by the user ([ISldWorks::UserControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~UserControl.html) set to false). To keep the SOLIDWORKS Design session open, set ISldWorks::UserControl to true, which makes the session visible, or you can close your documents at the end of your application's execution.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::ExitApp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExitApp.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::GetOpenFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html)
[ISldWorks::LoadFile4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.html)
[ISldWorks::OpenDoc6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html)
[ISldWorks::ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html)
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.html)
