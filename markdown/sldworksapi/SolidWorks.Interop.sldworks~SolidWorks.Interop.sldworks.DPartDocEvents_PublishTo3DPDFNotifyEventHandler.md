---
title: "DPartDocEvents_PublishTo3DPDFNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_PublishTo3DPDFNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PublishTo3DPDFNotifyEventHandler.html"
---

# DPartDocEvents_PublishTo3DPDFNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when publishing a part document to SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_PublishTo3DPDFNotifyEventHandler( _
   ByVal Path As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_PublishTo3DPDFNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_PublishTo3DPDFNotifyEventHandler(
   System.string Path
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_PublishTo3DPDFNotifyEventHandler(
   System.String^ Path
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Path`: Path where SOLIDWORKS MBD 3D PDF is saved

## VBA Syntax

See [PublishTo3DPDFNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~PublishTo3DPDFNotify_EV.html).

## Examples

[Fire Notification When Publishing Part to MBD 3D PDF (C#)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_CSharp.htm)
[Fire Notification When Publishing Part to MBD 3D PDF (VB.NET)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VBNET.htm)
[Fire Notification When Publishing Part to MBD 3D PDF (VBA)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VB.htm)

## Remarks

If developing a C++ application, use [swPartPublishTo3DPDFNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
