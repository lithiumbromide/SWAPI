---
title: "ISWPropertySheet Interface"
project: "SOLIDWORKS API Help"
interface: "ISWPropertySheet"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.html"
---

# ISWPropertySheet Interface

Allows applications to add pages to certain property sheets that are exported by the SOLIDWORKS Design application.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISWPropertySheet
```

### Visual Basic (Usage)

```vb
Dim instance As ISWPropertySheet
```

### C#

```csharp
public interface ISWPropertySheet
```

### C++/CLI

```cpp
public interface class ISWPropertySheet
```

## VBA Syntax

See [SWPropertySheet](ms-its:sldworksapivb6.chm::/sldworks~SWPropertySheet.html).

## Remarks

See [swPropSheetType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropSheetType_e.html) for a list of the property sheets that support this functionality.

An example of a property sheet is the dialog that is displayed when you click Tools > Options. This dialog consists of a base property sheet and property pages stacked on top of it. To display a specific property page, click its tab.

The MFC class that implements a property sheet is CPropertysheet, and the MFC class that implements a property page is CPropertyPage. ISWPropertySheet is a OLE wrapper class over the SOLIDWORKS CPropertysheet class. This means that SOLIDWORKS API programmers can add their own CPropertyPages to a SOLIDWORKS Design property sheet.

A SOLIDWORKS Design property sheet is different from an [IPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2.html) page. A PropertyManager page is displayed when the PropertyManager tab is selected on the left-side panel. PropertyManager pages have replaced numerous dialogs.

**Creating PropertyPages**

When a property sheet is created that can have pages added to it, the notification swAppPropertySheetCreateNotify is sent via the [ISldWorks](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks.html) interface. This notification is sent as swAppPropertySheetCreateNotify( LPDISPATCH sheet, long type) where sheet is the IDispatch interface of a ISWPropertySheet object and type is an enumerated constant of type swPropSheetType_e.

When the application receives this notification, it can check the type of the sheet from the type argument. If pages are to be added, then the sequence of operations is:

- Ensure that the application resources will be used to make the page (for example by calling AfxSetResourceHandle())
- Create the CPropertyPage-derived class
- For 32-bit applications, pass the CPropertyPage object to [ISWPropertySheet::AddPage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet~AddPage.html), casting the CPropertyPage* to a long
- For 64-bit applications, pass the CPropertyPage object to [ISWPropertySheet::AddPagex64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet~AddPagex64.html), casting the CPropertyPage* to a long long
- Reset the resources to their previous state

**Destroying PropertyPages**

The CPropertyPage PostNcDestroy function is called by the SOLIDWORKS Design application when the property sheet is being destroyed. At this point, the application should delete any objects (for example the CPropertyPage object.)

Events are implemented with delegates in the Microsoft .NET Framework. See the [Overview](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks_namespace.html) topic for a list of delegates for this interface.

## Access Diagram

[SWPropertySheet](SWObjectModel.pdf#SWPropertySheet)

## See Also

[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
