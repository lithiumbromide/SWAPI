---
title: "DAssemblyDocEvents_RenamedDocumentNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_RenamedDocumentNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RenamedDocumentNotifyEventHandler.html"
---

# DAssemblyDocEvents_RenamedDocumentNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when saving an assembly document in which a renamed component file is referenced by other assembly documents.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_RenamedDocumentNotifyEventHandler( _
   ByRef RenamedDocumentInterface As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_RenamedDocumentNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_RenamedDocumentNotifyEventHandler(
   ref System.object RenamedDocumentInterface
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_RenamedDocumentNotifyEventHandler(
   System.Object^% RenamedDocumentInterface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RenamedDocumentInterface`: [RenamedDocumentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html) object

## VBA Syntax

See [RenamedDocumentNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~RenamedDocumentNotify_EV.html).

## Examples

[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

## Remarks

If developing a C++ application, use [swAssemblyRenamedDocumentNotify](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

| To... | Use... |
| --- | --- |
| Rename a component file | IModelDocExtension::RenameDocument |
| Get whether an assembly document has renamed components | IModelDocExtension::HasRenamedDocuments |

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
