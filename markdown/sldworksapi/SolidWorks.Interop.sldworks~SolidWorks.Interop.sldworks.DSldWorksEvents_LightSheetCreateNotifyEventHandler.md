---
title: "DSldWorksEvents_LightSheetCreateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_LightSheetCreateNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_LightSheetCreateNotifyEventHandler.html"
---

# DSldWorksEvents_LightSheetCreateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a lighting sheet has been created.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_LightSheetCreateNotifyEventHandler( _
   ByVal NewSheet As System.Object, _
   ByVal sheetType As System.Integer, _
   ByVal LightId As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_LightSheetCreateNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_LightSheetCreateNotifyEventHandler(
   System.object NewSheet,
   System.int sheetType,
   System.int LightId
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_LightSheetCreateNotifyEventHandler(
   System.Object^ NewSheet,
   System.int sheetType,
   System.int LightId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewSheet`: New lighting sheet
- `sheetType`: Type of the new lighting sheet
- `LightId`: Light sheet ID

## VBA Syntax

See [LightSheetCreateNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~LightSheetCreateNotify_EV.html).

## Remarks

If developing a C++ application, use [swAppLightSheetCreateNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
