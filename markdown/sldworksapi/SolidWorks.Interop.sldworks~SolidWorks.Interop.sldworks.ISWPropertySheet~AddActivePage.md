---
title: "AddActivePage Method (ISWPropertySheet)"
project: "SOLIDWORKS API Help"
interface: "ISWPropertySheet"
member: "AddActivePage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddActivePage.html"
---

# AddActivePage Method (ISWPropertySheet)

Adds a third-party CPropertyPage to [ISWPropertySheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet.html) and adds an ActiveX control on top of the page.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddActivePage( _
   ByVal Title As System.String, _
   ByVal ProgId As System.String, _
   ByVal LicenseKey As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISWPropertySheet
Dim Title As System.String
Dim ProgId As System.String
Dim LicenseKey As System.String
Dim value As System.Integer

value = instance.AddActivePage(Title, ProgId, LicenseKey)
```

### C#

```csharp
System.int AddActivePage(
   System.string Title,
   System.string ProgId,
   System.string LicenseKey
)
```

### C++/CLI

```cpp
System.int AddActivePage(
   System.String^ Title,
   System.String^ ProgId,
   System.String^ LicenseKey
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Title`: Title of CPropertyPage
- `ProgId`: Name, ProgID, or CLSID of the ActiveX control (see Remarks)
- `LicenseKey`: License key for the ActiveX control

### Return Value

Index of CPropertyPage on ISWPropertySheet

## VBA Syntax

See [SWPropertySheet::AddActivePage](ms-its:sldworksapivb6.chm::/sldworks~SWPropertySheet~AddActivePage.html).

## Examples

```
'VBA Main module
```

```
Dim swApp As SldWorks.SldWorks
Option Explicit
Sub main()
    UserForm1.Show (swModeLess)
End Sub
```

```
'Insert UserForm module to VBA application
```

```
Option Explicit
```

```
Public WithEvents swAppEvents As SldWorks.SldWorks
Dim swApp As SldWorks.SldWorks
```

```
Private Function swAppEvents_PropertySheetCreateNotify(ByVal Sheet As Object, ByVal sheetType As Long) As Long
    Dim msrcSWPropertySheet As SWPropertySheet
    Set msrcSWPropertySheet = Sheet
    Call msrcSWPropertySheet.AddActivePage("PropertySheetExample2", "", "")
End Function
```

```
Private Sub UserForm_Initialize()
    Set swApp = Application.SldWorks
    Set swAppEvents = swApp
End Sub
```

## Remarks

Typically, this method is called from the ISldWorks [PropertySheetCreateNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_PropertySheetCreateNotifyEventHandler.html) event handler. See the Example section.

The ProgID argument accepts any of these values:

- OLE short name or ProgID for the class; for example, "MSCAL.Calendar". The name must match the name registered by the control.

- String form of a CLSID, contained within braces, for example, "{9DBAFCCF-592F-101B-85CE-00608CEC297B}".

See also [Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages](sldworksapiprogguide.chm::/overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm).

## See Also

[ISWPropertySheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.html)
[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
