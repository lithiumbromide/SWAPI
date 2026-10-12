---
title: "DModelViewEvents_PrintNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_PrintNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_PrintNotify2EventHandler.html"
---

# DModelViewEvents_PrintNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when a document is printed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_PrintNotify2EventHandler( _
   ByVal pDC As System.Long, _
   ByVal bPreview As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_PrintNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_PrintNotify2EventHandler(
   System.long pDC,
   System.bool bPreview
)
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_PrintNotify2EventHandler(
   System.int64 pDC,
   System.bool bPreview
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `pDC`: Pointer to the printer device context used to print the document (**see Remarks**)
- `bPreview`: True to preview the document, false to not

## VBA Syntax

See [PrintNotify2 Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~PrintNotify2_EV.html).

## Remarks

Always return S_OK in the swViewPrintNotify2 event handler.

If developing a C++ application, use [swViewPrintNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

pDC is the address of an MFC CDC instance, and it can be cast to a CDC*. C++ applications wanting to use this CDC* need to dynamically link to the MFC DLLs and use the same version of the Visual C++ compiler that SOLIDWORKS uses.

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
