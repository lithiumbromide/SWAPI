---
title: "DPartDocEvents_RenamedDocumentNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_RenamedDocumentNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenamedDocumentNotifyEventHandler.html"
---

# DPartDocEvents_RenamedDocumentNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when saving a document in which a renamed part file is referenced by other documents.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_RenamedDocumentNotifyEventHandler( _
   ByRef RenamedDocumentInterface As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_RenamedDocumentNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_RenamedDocumentNotifyEventHandler(
   ref System.object RenamedDocumentInterface
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_RenamedDocumentNotifyEventHandler(
   System.Object^% RenamedDocumentInterface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RenamedDocumentInterface`: [RenamedDocumentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html) object

## VBA Syntax

See [RenamedDocumentNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~RenamedDocumentNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartRenamedDocumentNotify](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
