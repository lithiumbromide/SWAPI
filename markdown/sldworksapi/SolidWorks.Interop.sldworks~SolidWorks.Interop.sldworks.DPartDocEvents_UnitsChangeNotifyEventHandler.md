---
title: "DPartDocEvents_UnitsChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_UnitsChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UnitsChangeNotifyEventHandler.html"
---

# DPartDocEvents_UnitsChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Generated when document units change.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_UnitsChangeNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_UnitsChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_UnitsChangeNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_UnitsChangeNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [UnitsChangeNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~UnitsChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartUnitsChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
