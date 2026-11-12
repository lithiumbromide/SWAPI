---
title: "DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler.html"
---

# DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when text is typed in the FeatureManager design tree filter or [IModelDocExtension::FeatureManagerFilterString](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~FeatureManagerFilterString.html) is called.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler( _
   ByVal FilterString As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler(
   System.string FilterString
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler(
   System.String^ FilterString
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilterString`: String

## VBA Syntax

See [FeatureManagerFilterStringChangeNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FeatureManagerFilterStringChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFeatureManagerFilterStringChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
