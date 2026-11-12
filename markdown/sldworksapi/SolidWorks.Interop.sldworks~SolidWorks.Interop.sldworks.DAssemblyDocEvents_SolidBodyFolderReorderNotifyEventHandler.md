---
title: "DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler.html"
---

# DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired with a solid body folder is reordered, e.g., using [IModelDocExtension::ReorderFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler( _
   ByVal Component As System.String, _
   ByVal Source As System.String, _
   ByVal Target As System.String, _
   ByVal ReorderLocation As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler(
   System.string Component,
   System.string Source,
   System.string Target,
   System.int ReorderLocation
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler(
   System.String^ Component,
   System.String^ Source,
   System.String^ Target,
   System.int ReorderLocation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Component`: Name of component
- `Source`: Item to move to a location with respect to the Target item
- `Target`: Item around which to move the Source item; could be a body folder
- `ReorderLocation`: Move location as defined by [swMoveLocation_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMoveLocation_e.html)

## VBA Syntax

See [SolidBodyFolderReorderNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~SolidBodyFolderReorderNotify_EV.html).

## Remarks

The Source and Target items can be these types:

- swSelectType_e.swSelBODYFOLDER
- swSelectType_e.swSelSUBWELDFOLDER
- swSelectType_e.swSelSUBATOMFOLDER
- swSelectType_e.swSelSOLIDBODIES

If developing a C++ application, use [swAssemblySolidBodyFolderReorderNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
