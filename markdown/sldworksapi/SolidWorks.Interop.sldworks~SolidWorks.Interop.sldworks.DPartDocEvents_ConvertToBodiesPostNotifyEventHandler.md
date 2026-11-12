---
title: "DPartDocEvents_ConvertToBodiesPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ConvertToBodiesPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ConvertToBodiesPostNotifyEventHandler.html"
---

# DPartDocEvents_ConvertToBodiesPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired after the Convert to Bodies dialog closes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ConvertToBodiesPostNotifyEventHandler( _
   ByVal FileName As System.String, _
   ByVal SaveOption As System.Integer, _
   ByVal PreserveGeometryAndSketches As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ConvertToBodiesPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ConvertToBodiesPostNotifyEventHandler(
   System.string FileName,
   System.int SaveOption,
   System.bool PreserveGeometryAndSketches
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ConvertToBodiesPostNotifyEventHandler(
   System.String^ FileName,
   System.int SaveOption,
   System.bool PreserveGeometryAndSketches
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: File name of the part to convert to a body
- `SaveOption`: Save option as defined in [swFileSaveTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileSaveTypes_e.html):

  - swFileSaveAs
  - swFileSaveAsCopy
  - swFileSaveAsCopyAndOpen
- `PreserveGeometryAndSketches`: True to preserve geometry and sketches, false to not

## VBA Syntax

See [ConvertToBodiesPostNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ConvertToBodiesPostNotify_EV.html).

## Remarks

This event is triggered after the user clicks **OK** or **Cancel** in the Convert to Bodies dialog and before user interface validation. FileName, SaveOption and PreserveGeometryAndSketches contain the values selected in the dialog.

If developing a C++ application, use [swPartConvertToBodiesPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
