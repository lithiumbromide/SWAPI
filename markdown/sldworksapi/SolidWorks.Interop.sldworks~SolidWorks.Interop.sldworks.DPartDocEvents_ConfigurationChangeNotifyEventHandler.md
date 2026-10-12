---
title: "DPartDocEvents_ConfigurationChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ConfigurationChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ConfigurationChangeNotifyEventHandler.html"
---

# DPartDocEvents_ConfigurationChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Gets information about an object or feature that has had one if its configurable parameters changed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ConfigurationChangeNotifyEventHandler( _
   ByVal ConfigurationName As System.String, _
   ByVal Object As System.Object, _
   ByVal ObjectType As System.Integer, _
   ByVal changeType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ConfigurationChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ConfigurationChangeNotifyEventHandler(
   System.string ConfigurationName,
   System.object Object,
   System.int ObjectType,
   System.int changeType
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ConfigurationChangeNotifyEventHandler(
   System.String^ ConfigurationName,
   System.Object^ Object,
   System.int ObjectType,
   System.int changeType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigurationName`: Name of the configuration that has changed
- `Object`: Object that has changed
- `ObjectType`: Type of the object that has changed as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

  - swSelDIMENSIONS
  - swSelDATUMPOINTS
  - swSelDATUMPLANES
  - swSelDATUMAXES
  - swSelHELIX
  - swSelBODYFEATURES
  - swSelMATEGROUP
  - swSelMATES
  - swSelCOORDSYS
  - swSelCOMPONENTS
  - swSelCONFIGURATIONS
  - swSelSKETCHES
  - swSelREFCURVES
  - swSelDISPLAYSTATE

  All other types are returned as swSelUNSUPPORTED.
- `changeType`: Type of change as defined by [swConfigurationChangeTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationChangeTypes_e.html)

## VBA Syntax

See [ConfigurationChangeNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ConfigurationChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartConfigurationChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
