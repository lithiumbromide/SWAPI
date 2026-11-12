---
title: "DSldWorksEvents_PropertySheetCreateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_PropertySheetCreateNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PropertySheetCreateNotifyEventHandler.html"
---

# DSldWorksEvents_PropertySheetCreateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when an exported [ISWPropertySheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet.html) is created so that the application can add pages to it.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_PropertySheetCreateNotifyEventHandler( _
   ByVal Sheet As System.Object, _
   ByVal sheetType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_PropertySheetCreateNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_PropertySheetCreateNotifyEventHandler(
   System.object Sheet,
   System.int sheetType
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_PropertySheetCreateNotifyEventHandler(
   System.Object^ Sheet,
   System.int sheetType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: [Property sheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet.html)
- `sheetType`: Type of the property sheet as defined in [swPropSheetType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropSheetType_e.html)

## VBA Syntax

See [PropertySheetCreateNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~PropertySheetCreateNotify_EV.html).

## Remarks

If developing a C++ application, use [swAppPropertySheetCreateNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
