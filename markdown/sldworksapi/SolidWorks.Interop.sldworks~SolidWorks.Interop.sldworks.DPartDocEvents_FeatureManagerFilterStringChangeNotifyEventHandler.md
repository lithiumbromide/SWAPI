---
title: "DPartDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler.html"
---

# DPartDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when text is typed in the FeatureManager design tree filter or [IModelDocExtension::FeatureManagerFilterString](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~FeatureManagerFilterString.html) is called.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler( _
   ByVal FilterString As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler(
   System.string FilterString
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler(
   System.String^ FilterString
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilterString`: String

## VBA Syntax

See [FeatureManagerFilterStringChangeNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FeatureManagerFilterStringChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartFeatureManagerFilterStringChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
