---
title: "DSldWorksEvents_NonNativeFileOpenNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_NonNativeFileOpenNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_NonNativeFileOpenNotifyEventHandler.html"
---

# DSldWorksEvents_NonNativeFileOpenNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when non-native SOLIDWORKS files are opened.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_NonNativeFileOpenNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_NonNativeFileOpenNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_NonNativeFileOpenNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_NonNativeFileOpenNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the opened file

## VBA Syntax

See [NonNativeFileOpenNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~NonNativeFileOpenNotify_EV.html).

## Remarks

This event occurs after automatic healing if it is enabled. To enable automatic healing, set swImportAutoRunImportDiagnosticsPersist and swImportAutoRunImportDiagnostics to True. See [swUserPreferenceToggle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html), Import for details about these two enumerators.

The file types handled include files with these extensions: .dxf, .dwg, .igs, .sat, .step, .vda, .wrl, and .dll.

On receiving this event, you can call [ISldWorks::ActiveDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActiveDoc.html) or [ISldWorks::IActiveDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActiveDoc2.html) to get the active [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) pointer.

In an environment when multiple applications are simultaneously loaded and have access to the SOLIDWORKS application through its APIs, exercise caution when this notification is processed. The active IModelDoc2 may not be the one that corresponds to the FileName argument. For example, this can occur when one of the translator DLL's receives this event and picks up the non-native file and generates a new SOLIDWORKS document. This could happen prior to your application receiving this event.

If developing a C++ application, use [swAppNonNativeFileOpenNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
